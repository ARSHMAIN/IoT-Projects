import dash
from dash import html, dcc
from dynamic import navbar
import dash_daq as daq
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    navbar.create_navbar()
])

if __name__ == '__main__':
    app.run(debug=True)
