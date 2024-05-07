import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            id='profile',
            children=[
                html.P('Profile', style={'fontSize': '40px'}),
                html.Img(src='/assets/my_sunshine.jpg', style={'width': '150px', 'height': '150px', 'borderRadius': '50%'}),
                html.Label('User ID'),
                dcc.Input(id='user-id', type='text', value=''),
                html.Label('Name'),
                dcc.Input(id='name', type='text', value=''),
                html.Label('Temp. Threshold'),
                dcc.Input(id='temp-threshold', type='number', value=0),
                html.Label('Humidity Threshold'),
                dcc.Input(id='humidity-threshold', type='number', value=0),
                html.Label('Light Intensity Threshold'),
                dcc.Input(id='light-intensity-threshold', type='number', value=0),
                html.Button('Submit Changes', id='submit-button', n_clicks=0)
            ],
            style={'flex': 1, 'width': '20%', 'borderRadius': '10px', 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px', 'textAlign': 'center'}
        ),

        html.Div(
            id='phases-container',
            children=[
                html.Div(
                    className='phase2',
                    children=[
                        html.Div(
                            className='gauge-container',
                            children=[
                                html.Div([
                                    html.Label('Temperature'),
                                    daq.Thermometer(
                                        id='temperature-gauge',
                                        label='Temperature',
                                        labelPosition='top',
                                        showCurrentValue=True,
                                        units="C",
                                        value=0,
                                        min=-30,
                                        max=40,
                                        style={'width': '100%', 'color': 'grey'}
                                    )
                                ], style={'width': '50%'}),
                                html.Div([
                                    html.Label('Humidity'),
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
                                        showCurrentValue=True,
                                        label="Humidity",
                                        value=0,
                                        max=50,
                                        min=0,
                                        style={'width': '100%', 'color': 'grey'}
                                    )
                                ], style={'width': '50%'})
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='phase3',
                    children=[
                        html.Div(
                            className='control-section',
                            children=[
                                html.Div([
                                    html.P('Light Control'),
                                    html.Img(src='/assets/led_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%'}),
                                    dcc.Checklist(id='light-switch', options=[{'label': 'Light Switch', 'value': 'on'}]),
                                    html.P('Light Intensity:'),
                                    html.P('Light Status:')
                                ]),
                                html.Div([
                                    html.P('Fan Control'),
                                    html.Img(src='/assets/fan_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%'}),
                                    dcc.Checklist(id='fan-switch', options=[{'label': 'Fan Switch', 'value': 'on'}]),
                                    html.P('Fan Intensity:')
                                ])
                            ]
                        )
                    ]
                ),
                html.Div(className='phase4', children=[html.P('Phase 4 Placeholder')]),
                html.Div(className='bluetooth', children=[html.P('Bluetooth Placeholder')])
            ],
            style={'flex': 1, 'padding': '20px', 'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'flex-end'}
        )
    ],
    style={'display': 'flex', 'flexDirection': 'row', 'height': '100vh', 'margin': 0, 'padding': 0, 'backgroundColor': 'rgb(52, 52, 52)'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
