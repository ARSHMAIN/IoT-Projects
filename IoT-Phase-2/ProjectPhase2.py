import dash_daq as daq
from dash import Dash, html, Input, Output, callback

# import RPi.GPIO as GPIO

app = Dash(__name__)

# GPIO.setmode(GPIO.BCM)
# LED_PIN = 17
# GPIO.setup(LED_PIN, GPIO.OUT)

app.layout = html.Div([
    html.Div(
        'IoT Phase 2 Project',
        style={'text-align': 'center', 'margin': '10px'}
    ),
    daq.ToggleSwitch(
        id='email-switch',
        value=False,  # state of the button
    ),
    html.Div(
        id='email-state',
        style={'text-align': 'center', 'margin-top': '20px'}

    ),
    daq.Thermometer(
        id='thermometer',
        label='Current Temperature',
        labelPosition='top',
        showCurrentValue=True,
        units="C",
        value=6,
        min=-30,
        max=30,
        style={'margin-bottom': '5%'}
    ),
    html.Img(
        id='fan',
        src='assets/fan on.png',  # image path
        alt='Fan',
        style={'display': 'block', 'margin': 'auto'}
    ),
])


# write the variables in the same order
@callback(
    # Output callbacks (inside the return)
    [Output('email-state', 'children'),
     Output('email-switch', 'color'),
     Output('fan', 'src')],

    # Input callback (inside the function)
    [Input('email-switch', 'value')]
)
def update_output(value):
    if value:
        # GPIO.output(LED_PIN, GPIO.HIGH)
        print('Turn ON on.')
        return 'Turn ON on.', 'blue', 'assets/fan on.png'  # return all output callbacks
    else:
        # GPIO.output(LED_PIN, GPIO.LOW)
        print('Turn OFF fan.')
        return 'Turn OFF fan.', 'none', 'assets/fan off.png'  # return all output callbacks


if __name__ == '__main__':
    app.run(debug=True)
