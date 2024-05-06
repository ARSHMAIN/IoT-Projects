import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from dash.dependencies import Input, Output
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout using Dash components
app.layout = html.Div(
    children=[
        html.Div(
            id='profile',
            children=[
                html.P('Profile', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana','fontSize': '40px'}),
                html.Img(src='/assets/my_sunshine.jpg', style={'width': '150px', 'height': '150px', 'borderRadius': '50%', 'margin': '0 auto', 'display': 'block'}),
                html.Label('User ID', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block'}),
                dcc.Input(id='user-id', type='text', value='', style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Name', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block'}),
                dcc.Input(id='name', type='text', value='', style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Temp. Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block'}),
                dcc.Input(id='temp-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Humidity Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block'}),
                dcc.Input(id='humidity-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Light Intensity Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block'}),
                dcc.Input(id='light-intensity-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Button('Submit Changes', id='submit-button', n_clicks=0, style={'width': '100%', 'height': '50px', 'backgroundColor': 'lightblue', 'margin-top': '20px'})
            ],
            style={'flex': 1,'width': '20%', 'borderRadius': '10px', 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px', 'textAlign': 'center'}
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
                                html.P('Temperature and Humidity', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"}),
                                html.Div([
                                    daq.Thermometer(
                                        id='temperature-gauge',
                                        label='Temperature',
                                        labelPosition='top',
                                        showCurrentValue=True,
                                        units="C",
                                        value=0,
                                        min=-30,
                                        max=40,
                                        style={'width': '50%', 'margin-right': '5%'}
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
                                        showCurrentValue=True,
                                        label="Humidity",
                                        value=0,
                                        max=50,
                                        min=0,
                                        style={'width': '50%'}
                                    )
                                ], style={'display': 'flex', 'justifyContent': 'space-between'})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase3',
                            children=[
                                html.P('LED and Fan', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"}),
                                html.Div([
                                    html.Img(src='/assets/led_off.jpg', style={'width': '150px', 'height': '150px', 'borderRadius': '50%', 'margin-right': '90px', }),
                                    html.Img(src='/assets/fan_off.png', style={'width': '150px', 'height': '150px', 'borderRadius': '50%', 'margin-left': '90px'})
                                ], style={'display': 'flex', 'justifyContent': 'center'})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase4',
                            children=[
                                html.P('Bluetooth Devices', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)'}
                        )
                    ],
                    style={'display': 'flex', 'flexDirection': 'column', 'flex': 1}
                )
            ],
            style={'display': 'flex', 'flex': 1, 'justifyContent': 'flex-end'}
        )
    ],
    style={'display': 'flex', 'flexDirection': 'row', 'height': '100vh', 'margin': 0, 'padding': 0, 'backgroundColor': 'rgb(52, 52, 52)'}
)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
