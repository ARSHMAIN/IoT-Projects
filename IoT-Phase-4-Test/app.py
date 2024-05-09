# noinspection PyUnresolvedReferences
import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import Dash, html, callback, Input, Output, dcc

import re
import Email_System as Email
import RPi.GPIO as GPIO
import Freenove_DHT as DHT
import MQTT_Sub as MQTT_Sub
from time import sleep

# Setup start
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

is_email_sent = False

DHTPin = 11  # GPIO 17
LED_PIN = 40  # GPIO 21
Motor1 = 33  # Enable Pin GPIO 13
Motor2 = 35  # Input Pin GPIO 19
Motor3 = 37  # Input Pin GPIO 26

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(Motor3, GPIO.OUT)
# Setup end


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
        html.Div(
            id='profile',
            children=[
                html.P('Profile',
                       style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'fontSize': '40px'}),
                html.Img(src='/assets/my_sunshine.jpg',
                         style={'width': '150px', 'height': '150px', 'borderRadius': '50%', 'margin': '0 auto',
                                'display': 'block'}),
                html.Label('User ID', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block',
                                             'font-family': 'Verdana'}),
                dcc.Input(id='user-id', type='text', value='',
                          style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Name', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block',
                                          'font-family': 'Verdana'}),
                dcc.Input(id='name', type='text', value='',
                          style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Temp. Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block',
                                                     'font-family': 'Verdana'}),
                dcc.Input(id='temp-threshold', type='number', value=0,
                          style={'width': '100%', 'margin-bottom': '20px', 'height': '50px', 'font-family': 'Verdana'}),
                html.Label('Humidity Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block',
                                                        'font-family': 'Verdana'}),
                dcc.Input(id='humidity-threshold', type='number', value=0,
                          style={'width': '100%', 'margin-bottom': '20px', 'height': '50px', 'font-family': 'Verdana'}),
                html.Label('Light Intensity Threshold',
                           style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block',
                                  'font-family': 'Verdana'}),
                dcc.Input(id='light-intensity-threshold', type='number', value=0,
                          style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Button('Submit Changes', id='submit-button', n_clicks=0,
                            style={'width': '100%', 'height': '50px', 'backgroundColor': 'lightblue',
                                   'margin-top': '20px', 'font-family': 'Verdana'}),
                # Toast
                dbc.Toast(
                    [html.P("Email has been sent!", className="mb-0")],
                    id="message",
                    duration=3000,
                    is_open=False,
                    style={'position': 'fixed', 'top': '70px', 'left': '20px', 'width': '300px'}
                ),
                dbc.Button(
                    "Email Status",
                    id="button_toggle",
                    color="secondary",
                    className="mb-3",
                    n_clicks=0,
                    style={'position': 'fixed', 'top': '20px', 'left': '20px'}
                ),
            ],
            style={'flex': 1, 'width': '200%', 'borderRadius': '10px', 'padding': '20px', 'textAlign': 'center', }
        ),

        html.Div(
            id='phases-container',
            children=[
                html.Div(
                    id='right-phases',
                    children=[
                        html.Div(
                            id='phase2',
                            children=[
                                html.Div([
                                    html.Div(
                                        daq.Thermometer(
                                            id='temperature-gauge',
                                            label='Temperature',
                                            labelPosition='top',
                                            showCurrentValue=True,
                                            value=0,
                                            min=-0,
                                            max=40,
                                            style={'width': '350px', 'height': '325px', 'margin-right': '30px',
                                                   'margin-left': '10px', 'border': '5px solid lightgrey',
                                                   'backgroundColor': 'rgb(129, 133, 137)', 'borderRadius': '10px',
                                                   'fontFamily': 'Verdana', 'color': 'white'}
                                        ),
                                        style={'width': '50%', 'display': 'inline-block'}
                                    ),
                                    html.Div(
                                        daq.Gauge(
                                            color={
                                                "gradient": True,
                                                "ranges": {
                                                    "green": [0, 18],
                                                    "yellow": [18, 24],
                                                    "red": [24, 30]
                                                },
                                                "value": "red"
                                            },
                                            id='humidity-gauge',
                                            showCurrentValue=True,
                                            label="Humidity",
                                            value=0,
                                            min=0,
                                            max=50,
                                            style={'width': '350px', 'height': '325px', 'margin-right': '50px',
                                                   'margin-left': '75px', 'border': '5px solid lightgrey',
                                                   'backgroundColor': 'rgb(129, 133, 137)', 'borderRadius': '10px',
                                                   'fontFamily': 'Verdana', 'color': 'white'},
                                        ),
                                        style={'width': '50%', 'display': 'inline-block'}
                                    )
                                ], style={'display': 'flex', 'justifyContent': 'space-between'}),
                            ],
                            style={'flex': 1, 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase3',
                            children=[
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div("Light Control",
                                                         style={'color': 'white', 'textAlign': 'center',
                                                                'font-family': 'Verdana'}),
                                                html.Img(id='led-img',
                                                    src='/assets/led_off.png',
                                                         style={'width': '100px', 'height': '100px',
                                                                'borderRadius': '50%', 'margin-bottom': '20px'}),
                                                daq.BooleanSwitch(
                                                    id='light-switch',
                                                    on=False,
                                                    disabled=True,
                                                    style={'font-family': 'Verdana', 'color': 'green',
                                                           'margin-bottom': '20px'}
                                                ),
                                                html.P('Light Intensity:',
                                                       id='light-intensity',
                                                       style={'color': 'white', 'textAlign': 'center',
                                                              'font-family': 'Verdana', 'margin-bottom': '20px'}),
                                                html.P('Light Status: Off',
                                                       id='light-status',
                                                       style={'color': 'white', 'textAlign': 'center',
                                                                               'font-family': 'Verdana',
                                                                               'margin-bottom': '20px'}),
                                            ],
                                            style={'display': 'inline-block', 'border': '5px solid lightgrey',
                                                   'padding': '20px', 'borderRadius': '10px', 'text-align': 'center',
                                                   'margin-right': '150px', 'width': '350px', 'height': '285px',
                                                   'backgroundColor': 'rgb(129, 133, 137)', 'margin-left': '5px'}
                                        ),

                                        html.Div(
                                            [
                                                html.Div("Fan Control", style={'color': 'white', 'textAlign': 'center',
                                                                               'font-family': 'Verdana'}),
                                                html.Img(id='fan-img',
                                                    src='/assets/fan_off.png',
                                                         style={'width': '100px', 'height': '100px',
                                                                'borderRadius': '50%', 'margin-bottom': '20px'}),
                                                daq.BooleanSwitch(
                                                    id='fan-switch',
                                                    on=False,
                                                    disabled=True,
                                                    style={'font-family': 'Verdana', 'color': 'green',
                                                           'margin-bottom': '20px'}
                                                ),
                                                html.P('Fan Status:', style={'color': 'white', 'textAlign': 'center',
                                                                             'font-family': 'Verdana',
                                                                             'margin-bottom': '20px'}),
                                            ],
                                            style={'display': 'inline-block', 'border': '5px solid lightgrey',
                                                   'padding': '20px', 'borderRadius': '10px', 'text-align': 'center',
                                                   'width': '350px', 'height': '285px',
                                                   'backgroundColor': 'rgb(129, 133, 137)', 'margin-right': '5px'}
                                        ),
                                    ],
                                    style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                                )

                            ],
                            style={'flex': 1, 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase4',
                            children=[
                                html.Img(src='/assets/bluetooth_png.png',
                                         style={'width': '100px', 'height': '35px', 'marginLeft': '10px'}),
                                html.Div([
                                    html.P('Bluetooth Devices Nearby',
                                           style={'color': 'white', 'textAlign': 'center', 'font-family': "Verdana",
                                                  'margin-top': '20px', 'backgroundColor': 'rgb(29, 119, 242)',
                                                  'width': '300px', 'height': '40px', 'lineHeight': '40px',
                                                  'borderRadius': '10px'}),
                                    dcc.Input(id='bluetooth-devices', type='text', value='',
                                              style={'width': '100px', 'margin-top': '20px', 'marginLeft': '20px',
                                                     'height': '30px', 'marginBottom': '15px',
                                                     'border': '5px solid rgb(29, 119, 242)', 'borderRadius': '10px'})
                                ], style={'display': 'flex', 'alignItems': 'center'}),
                                html.Div([
                                    html.P('RSSI Threshold (dBm)',
                                           style={'color': 'white', 'textAlign': 'center', 'font-family': "Verdana",
                                                  'margin-top': '20px', 'backgroundColor': 'rgb(29, 119, 242)',
                                                  'width': '300px', 'height': '40px', 'lineHeight': '40px',
                                                  'borderRadius': '10px'}),
                                    dcc.Input(id='rssi-threshold', type='number', value=0,
                                              style={'width': '100px', 'margin-top': '20px', 'marginLeft': '20px',
                                                     'height': '30px', 'marginBottom': '15px',
                                                     'border': '5px solid rgb(29, 119, 242)', 'borderRadius': '10px'})
                                ], style={'display': 'flex', 'alignItems': 'center'})
                            ],
                            style={'flex': 1, 'padding': '20px'}
                        )
                    ],
                    style={'display': 'flex', 'flexDirection': 'column', 'flex': 1}
                )
            ],
            style={'display': 'flex', 'flex': 1, 'justifyContent': 'flex-end'}
        ),
        dbc.Toast(
            "Email regarding",
            id="email-toast",
            header="New Email",
            is_open=False,
            dismissable=True,
            duration=4000,
            icon="success",
            # top: 66 positions the toast below the navbar
            style={"position": "fixed", "top": 20, "right": 20, "width": 350},
        ),
        dcc.Interval(
            id='interval-component',
            interval=4000,  # Update every 2 seconds
            n_intervals=0
        ),
    ],
    style={'display': 'flex', 'flexDirection': 'row', 'height': '100vh', 'margin': 0, 'padding': 0,
           'backgroundColor': 'rgb(52, 52, 52)'}
)

MQTT_Sub.start_mqtt_client()

@callback(
    Output("message", "is_open"),
    [Input("button_toggle", "n_clicks")]
)
def open_toast(n):
    if n == 0:
        return dash.no_update
    return True


# Functions

# Motor
@callback(
    [Output('humidity-gauge', 'value'),
     Output('temperature-gauge', 'value')],
    [Input('interval-component', 'n_intervals')],
)
def update_gauges(n):
    dht = DHT.DHT(DHTPin)
    while True:
        dht.readDHT11()
        # print(f'Humidity: {dht.humidity}', f'Temperature: {dht.temperature}')
        return [dht.humidity, dht.temperature]

@callback(
    [Output('fan', 'src')],
    [Input('temperature-gauge', 'value')]
)
def send_email(temperature):
    send_response = Email.send_email_fan(temperature)
    print(send_response)

    receive_response = Email.receive_email_fan()
    print(receive_response)

    if not receive_response or ('Error' in str(receive_response)):
        return ['assets/fan off.png']
    return ['assets/fan on.png']


# Photoresistor
@callback(
    Output('light-intensity', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_light_sensor_value(n):
    # print(MQTT_Sub.get_light_brightness())
    return f"Light Intensity: {MQTT_Sub.get_light_brightness()}%"

@callback(
    [Output('led-img', 'src'),
     Output('light-status', 'children'),
     Output('email-toast', 'children'),
     Output('email-toast', 'is_open')],
    Input('light-intensity', 'children')
)
def update_light_status_and_notify(light_intensity):
    global is_email_sent
    # Get number in string with regex
    match = re.search(r'\d+', light_intensity)
    # Convert to Int
    light_intensity = int(match.group())
    print(int(match.group()))

    if light_intensity < 40:
        if not is_email_sent:
            Email.send_email_light()
            print("Email sent")
            is_email_sent = True
            GPIO.output(LED_PIN, GPIO.HIGH)
            return ["assets/led_on.png", "Light Status: On", "Email regarding light status", True]
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)
            return ["assets/led_on.png", "Light Status: On",  "Email regarding light status", False]
    else:
        if is_email_sent:
            print("Email not sent")
            is_email_sent = False
            GPIO.output(LED_PIN, GPIO.LOW)
            return ["assets/led_off.png", "Light Status: Off",  "Email regarding light status", False]
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            return ["assets/led_off.png", "Light Status: Off",  "Email regarding light status", False]

# Run the Dash app
if __name__ == '__main__':
    app.run(host='192.168.187.68', port=8050, debug=True)
