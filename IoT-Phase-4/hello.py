import dash
from dash import html, dcc
import dash_daq as daq
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout using Dash components
app.layout = html.Div(
    children=[
        html.Div(
            id='profile',
            children=[
                html.P('Profile', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'fontSize': '40px'}),
                html.Img(src='/assets/my_sunshine.jpg', style={'width': '150px', 'height': '150px', 'borderRadius': '50%', 'margin': '0 auto', 'display': 'block'}),
                html.Label('User ID', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block', 'font-family': 'Verdana'}),
                dcc.Input(id='user-id', type='text', value='', style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Name', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block', 'font-family': 'Verdana'}),
                dcc.Input(id='name', type='text', value='', style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Label('Temp. Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block', 'font-family': 'Verdana'}),
                dcc.Input(id='temp-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px', 'font-family': 'Verdana'}),
                html.Label('Humidity Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block', 'font-family': 'Verdana'}),
                dcc.Input(id='humidity-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px', 'font-family': 'Verdana'}),
                html.Label('Light Intensity Threshold', style={'color': 'grey', 'margin-bottom': '5px', 'display': 'block', 'font-family': 'Verdana'}),
                dcc.Input(id='light-intensity-threshold', type='number', value=0, style={'width': '100%', 'margin-bottom': '20px', 'height': '50px'}),
                html.Button('Submit Changes', id='submit-button', n_clicks=0, style={'width': '100%', 'height': '50px', 'backgroundColor': 'lightblue', 'margin-top': '20px', 'font-family': 'Verdana'})
            ],
            style={'flex': 1, 'width': '20%', 'borderRadius': '10px', 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px', 'textAlign': 'center'}
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
                                        daq.Thermometer(
                                        id='temperature-gauge',
                                        label='Temperature',
                                        labelPosition='top',
                                        showCurrentValue=True,
                                        units="C",
                                        value=0,
                                        min=-30,
                                        max=40,
                                        style={'width': '50%', 'margin-right': '5%', 'color': 'grey', 'height': '100px'}
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
                                        style={'width': '50%', 'color': 'grey', 'height': '100px'}
                                    )


                                ], style={'display': 'flex', 'justifyContent': 'space-between'}),
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase3',
                            children=[
                                html.Div([
                                    html.Div([
                                        html.Div("Light Control", style={'color': 'grey', 'textAlign': 'center', 'margin-right': '175px', 'margin-bottom': '20px', 'font-family': 'Verdana'}),
                                        html.Img(src='/assets/led_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%', 'margin-right': '175px'}),
                                        daq.BooleanSwitch(
                                            id='light-switch',
                                            on=False,
                                            style={'font-family': 'Verdana', 'color': 'green', 'margin-top': '20px', 'margin-right': '175px'}
                                        ),
                                        html.P('Light Intensity:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-right': '175px'}),
                                        html.P('Light Status:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-right': '175px'}),
                                    ], style={'display': 'inline-block'}),

                                    html.Div([
                                        html.Div("Fan Control", style={'color': 'grey', 'textAlign': 'center', 'margin-left': '175px', 'margin-bottom': '20px', 'font-family': 'Verdana'}),
                                        html.Img(src='/assets/fan_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%', 'margin-left': '175px'}),
                                        daq.BooleanSwitch(
                                            id='fan-switch',
                                            on=False,
                                            style={'font-family': 'Verdana', 'color': 'green', 'margin-top': '20px', 'margin-left': '175px'}
                                        ),
                                        html.P('Fan Intensity:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-left': '175px'}),
                                    ], style={'display': 'inline-block'})
                                ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px'}
                        ),
                        html.Div(
                            id='phase4',
                            children=[
                                html.P(style={'color': 'grey', 'textAlign': 'center', 'font-family': "Verdana"})
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
