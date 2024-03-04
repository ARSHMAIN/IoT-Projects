from dash import Dash, html, Input, Output, callback
import dash_daq as daq
import RPi.GPIO as GPIO

app = Dash(__name__)

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

app.layout = html.Div([
    html.Div('IoT'),
    daq.ToggleSwitch(
        id='my-toggle-switch',
        value=False
    ),
    html.Div(id='my-toggle-switch-output')
])


@callback(
    Output('my-toggle-switch-output', 'children'),
    Input('my-toggle-switch', 'value')
)
def update_output(value):
    if value:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print( 'The light is ON.')
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        print( 'The light is OFF.')


if __name__ == '__main__':
    app.run(debug=True)
