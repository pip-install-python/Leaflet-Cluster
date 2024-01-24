# Plotly Dash & Core Imports
import dash
from dash import html, dcc, Input, Output, Dash, State
from flask import Flask

# Layout & Style
import dash_bootstrap_components as dbc

server = Flask(__name__)

chroma = 'https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js'

app = Dash(
    __name__,
    assets_url_path="assets",
    external_stylesheets=[
        dbc.themes.SLATE,
    ],
    external_scripts=[
        chroma
    ],
    use_pages=True,
    server=server,
)

app.layout = html.Div(
    [
        dash.page_container,
    ],
    style={"height": "100vh"},
)


if __name__ == "__main__":
    app.run_server(
        debug=True,
        port=8419,
        threaded=True,
    )
