import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout using Dash components
app.layout = html.Div(
    children=[
        html.Div(
            id='profile',
            children=[
                html.P('Profile', style={'color': 'grey', 'textAlign': 'center', 'font-family': 'Verdana','fontSize': '40px'})
            ],
            style={'flex': 1,'width': '50%', 'borderRadius': '10px', 'border': '5px ridge rgb(128, 0, 32)'}
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
                                html.P('Phase 2', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)'}
                        ),
                        html.Div(
                            id='phase3',
                            children=[
                                html.P('Phase 3', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"})
                            ],
                            style={'flex': 1, 'border': '5px ridge rgb(128, 0, 32)'}
                        ),
                        html.Div(
                            id='phase4',
                            children=[
                                html.P('Phase 4', style={'color': 'grey','textAlign': 'center', 'font-family': "Verdana"})
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
