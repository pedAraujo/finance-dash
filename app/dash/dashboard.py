from dash import Dash
from .components.layout import create_layout
import dash_bootstrap_components as dbc
import logging

my_assets = "./static/css"
URL_BASE_PATHNAME = "/dashboard/"


def init_dashboard(server, revenue_data, spendings_data):
    dash_app = Dash(
        server=server,
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
        assets_folder=my_assets,
        url_base_pathname=URL_BASE_PATHNAME,
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
        ],  # meta tags are required for the app to be mobile responsive
    )
    dash_app.title = "Minhas Finanças"
    dash_app.layout = create_layout(dash_app, revenue_data, spendings_data)

    logging.info("Dashboard initialized")
    return dash_app.server
