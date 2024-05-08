import dash
from dash import html
from dash import dcc
import dash_daq as daq
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Nav(
        style={'background-color': '#333'},
        children=[
            html.Div(className="nav-wrapper", children=[
                html.A('IoT Final Phase', href="#", className="title"),
                html.Ul(id='nav-mobile', className='left', children=[
                    html.Li(html.Button('Theme', id='theme-toggle', className='btn effect', n_clicks=0,)),
                ]),
            ]),
        ]
    ),

    html.Div(id='main-content', style={'flex': 1, 'display': 'flex', 'flex-direction': 'row'}, children=[
        html.Div(style={'flex': 1, 'width': '200%', 'padding': '20px', 'textAlign': 'center'}, children=[
            html.Div(id='profile', children=[
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
                html.Button('Submit Changes', id='submit-button', n_clicks=0, style={'width': '100%', 'height': '50px', 'backgroundColor': 'lightblue', 'margin-top': '20px', 'font-family': 'Verdana'}),
            ]),
        ]),

        html.Div(style={'display': 'flex', 'flex': 1, 'justifyContent': 'flex-end'}, children=[
            html.Div(id='phases-container', style={'display': 'flex', 'flex': 1, 'flexDirection': 'column'}, children=[
                html.Div(id='right-phases', style={'display': 'flex', 'flexDirection': 'column', 'flex': 1}, children=[
                    html.Div(id='phase2', style={'flex': 1, 'padding': '20px'}, children=[
                        html.Div(style={'display': 'flex', 'justifyContent': 'space-between'}, children=[
                            html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
                                daq.Thermometer(
                                    id='temperature-gauge',
                                    label='Temperature',
                                    labelPosition='top',
                                    showCurrentValue=True,
                                    units="C",
                                    value=0,
                                    min=-30,
                                    max=40,
                                    style={'width': '300px', 'height': '300px', 'margin-right': '5%','backgroundColor': 'lightgrey'}
                                ),
                            ]),
                            html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
                                daq.Gauge(
                                    color={"gradient": True, "ranges": {"green": [0, 18], "yellow": [18, 24], "red": [24, 30]}},
                                    id='humidity-gauge',
                                    showCurrentValue=True,
                                    label="Humidity",
                                    value=0,
                                    max=50,
                                    min=0,
                                    style={'width': '300px', 'height': '300px','backgroundColor': 'lightgrey'}
                                ),
                            ]),
                        ]),
                    ]),

                    html.Div(id='phase3', style={'flex': 1, 'padding': '20px'}, children=[
                        html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}, children=[
                            html.Div(style={'display': 'inline-block', 'border': '5px solid lightgrey', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'margin-right': '150px', 'width': '300px', 'height': '250px', 'backgroundColor': 'lightgrey'}, children=[
                                html.Div("Light Control", style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana'}),
                                html.Img(src='/assets/led_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%', 'margin-bottom': '20px'}),
                                daq.BooleanSwitch(id='light-switch', on=False, style={'font-family': 'Verdana', 'color': 'green', 'margin-bottom': '20px'}),
                                html.P('Light Intensity:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-bottom': '20px'}),
                                html.P('Light Status:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-bottom': '20px'}),
                            ]),

                            html.Div(style={'display': 'inline-block', 'border': '5px solid lightgrey', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'width': '300px', 'height': '250px', 'backgroundColor': 'lightgrey'}, children=[
                                html.Div("Fan Control", style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana'}),
                                html.Img(src='/assets/fan_off.png', style={'width': '100px', 'height': '100px', 'borderRadius': '50%', 'margin-bottom': '20px'}),
                                daq.BooleanSwitch(id='fan-switch', on=False, style={'font-family': 'Verdana', 'color': 'green', 'margin-bottom': '20px'}),
                                html.P('Fan Status:', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana', 'margin-bottom': '20px'}),
                            ]),
                        ]),
                    ]),

                    html.Div(id='phase4', style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)', 'padding': '20px'}, children=[
                        html.Img(src='/assets/bluetooth_png.png', style={'width': '100px', 'height': '35px', 'marginLeft': '10px'}),
                        html.Div(children=[
                            html.P('Bluetooth Devices Nearby', style={'color': 'white', 'textAlign': 'center', 'font-family': "Verdana", 'marginTop': '20px', 'backgroundColor': 'rgb(29, 119, 242)', 'width': '300px', 'height': '40px', 'lineHeight': '40px', 'borderRadius': '10px'}),
                            dcc.Input(id='bluetooth-devices', type='text', value='', style={'width': '100px', 'marginTop': '20px', 'marginLeft': '20px', 'height': '30px', 'marginBottom': '15px', 'border': '5px solid rgb(29, 119, 242)', 'borderRadius': '10px'}),
                        ]),
                        html.Div(children=[
                            html.P('RSSI Threshold (dBm)', style={'color': 'white', 'textAlign': 'center', 'font-family': "Verdana", 'marginTop': '20px', 'backgroundColor': 'rgb(29, 119, 242)', 'width': '300px', 'height': '40px', 'lineHeight': '40px', 'borderRadius': '10px'}),
                            dcc.Input(id='rssi-threshold', type='number', value=0, style={'width': '100px', 'marginTop': '20px', 'marginLeft': '20px', 'height': '30px', 'marginBottom': '15px', 'border': '5px solid rgb(29, 119, 242)', 'borderRadius': '10px'}),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),
])

@app.callback(
    Output('main-content', 'style'),
    [Input('theme-toggle', 'n_clicks')]
)
def toggle_theme(n_clicks):
    if n_clicks is None:
        return {'backgroundColor': 'rgb(52, 52, 52)'}
    elif n_clicks % 2 == 0:
        return {'backgroundColor': 'rgb(52, 52, 52)'}
    else:
        return {'backgroundColor': 'white'}

if __name__ == '__main__':
    app.run_server(debug=True)
