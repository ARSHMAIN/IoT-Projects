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
                html.P('Profile', style={'textAlign': 'center', 'color': 'white'})
            ],
            style={'flex': 1, 'backgroundColor': 'blue'}
        ),
        html.Div(
            id='phases-container',
            children=[
                html.Div(
                    id='left-phases',
                    children=[
                        html.Div(
                            id='phase1',
                            children=[
                                html.P('Phase 1', style={'textAlign': 'center'})
                            ],
                            style={'flex': 1, 'backgroundColor': 'red'}
                        ),
                        html.Div(
                            id='phase2',
                            children=[
                                html.P('Phase 2', style={'textAlign': 'center'})
                            ],
                            style={'flex': 1, 'backgroundColor': 'yellow'}
                        )
                    ],
                    style={'display': 'flex', 'flexDirection': 'column', 'flex': 1}
                ),
                html.Div(
                    id='right-phases',
                    children=[
                        html.Div(
                            id='phase3',
                            children=[
                                html.P('Phase 3', style={'textAlign': 'center'})
                            ],
                            style={'flex': 1, 'backgroundColor': 'purple'}
                        ),
                        html.Div(
                            id='phase4',
                            children=[
                                html.P('Phase 4', style={'textAlign': 'center'})
                            ],
                            style={'flex': 1, 'backgroundColor': 'orange'}
                        )
                    ],
                    style={'display': 'flex', 'flexDirection': 'column', 'flex': 1}
                )
            ],
            style={'display': 'flex', 'flex': 1}
        )
    ],
    style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh', 'margin': 0, 'padding': 0}
)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
