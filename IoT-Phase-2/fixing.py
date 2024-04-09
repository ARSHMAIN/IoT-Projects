import smtplib
import time
import Freenove_DHT as DHT
import dash_daq as daq
import dash_core_components as dcc
from dash import Dash, html, Input, Output, callback

DHTPin = 11

app = Dash(__name__)

# GPIO.setmode(GPIO.BCM)
# LED_PIN = 17
# GPIO.setup(LED_PIN, GPIO.OUT)

app.layout = html.Div([
    html.Div(
        'IoT Phase 2 Project',
        style={'text-align': 'center', 'margin': '10px'}
    ),
    html.Div(
        id='email-state',
        style={'text-align': 'center', 'margin-top': '20px'}
    ),
    daq.Thermometer(
        id='temperature-gauge',
        label='Temperature',
        labelPosition='top',
        showCurrentValue=True,
        units="C",
        value=6,
        min=-30,
        max=40,
        style={'margin-bottom': '5%'}
    ),
    html.Img(
        id='fan',
        src='assets/fan on.png',
        alt='Fan',
        style={'display': 'block', 'margin': 'auto'}
    ),
    daq.Gauge(
        color={"gradient": True, "ranges": {"green": [0, 18], "yellow": [18, 24], "red": [24, 30]}},
        id='humidity-gauge',
        label="Humidity",
        value=6,
        max=50,
        min=0,
    ),
    dcc.Interval(
        id='interval-component',
        interval=2000,  # Update every 2 seconds
        n_intervals=0
    ),
])


@callback(
    [Output('temperature-gauge', 'value'), Output('humidity-gauge', 'value')],
    Input('interval-component', 'n_intervals'),
    prevent_initial_call=True
)
def update_temperature_gauge(n):
    array = [20, 25, 23, 19, 21]
    for i in range(len(array)):
        if array[i] > 22:
            return array[i]
    return 'csc'
    # if temperature > 22:

def send_email():
    if

def update_humidity_gauge(n):
    return 'csc'


if __name__ == '__main__':
    app.run(debug=True)
