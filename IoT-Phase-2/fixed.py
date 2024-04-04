import dash_daq as daq
import random
from dash import Dash, html, callback, Input, Output, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        'IoT Phase 2 Project',
        style={'text-align': 'center', 'margin': '10px'}
    ),
    daq.Thermometer(
        id='temperature-gauge',
        label='Temperature',
        labelPosition='top',
        showCurrentValue=True,
        units="C",
        value=0,
        min=-30,
        max=40,
        style={'margin-bottom': '5%'}
    ),
    daq.Gauge(
        color={
            "gradient": True,
            "ranges": {
                "green": [0, 18],
                "yellow": [18, 24],
                "red": [24, 30]
            }
        },
        id='humidity-gauge',
        label="Humidity",
        value=0,
        max=50,
        min=0,
    ),
    html.Div(
        id='email',
        style={'text-align': 'center', 'margin': '10px'}
    ),
    html.Img(
        id='fan',
        src='assets/fan off.png',
        alt='Fan',
        style={'display': 'block', 'margin': 'auto'}
    ),
    dcc.Interval(
        id='interval-component',
        interval=2000,  # Update every 2 seconds
        n_intervals=0
    ),
])


@callback(
    [Output('humidity-gauge', 'value'),
     Output('temperature-gauge', 'value'),],
    [Input('interval-component', 'n_intervals')],
    prevent_initial_call=True
)
def update_gauges(n_intervals):
    humidity = random.randint(30, 60)
    temperature = random.randint(18, 25)
    return [humidity, temperature]


@callback(
    [Output('email', 'children')],
    [Input('temperature-gauge', 'value')]
)
def send_email(temperature):
    if temperature > 23:
        return [f'Email sent! Temperature is {temperature}!']
    return [f'Email not sent!']


@callback(
    [Output('fan', 'src')],
    [Input('email', 'children')]
)
def receive_email(email):
    if 'Email not sent!' in email:
        print(email)
        return ['assets/fan off.png']
    else:
        return ['assets/fan on.png']


if __name__ == '__main__':
    app.run(debug=True)
