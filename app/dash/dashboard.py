from dash import Dash
from .components.layout import create_layout
import dash_bootstrap_components as dbc


def init_dashboard(server, revenue_data, spendings_data):
    external_stylesheets = [dbc.themes.BOOTSTRAP]

    dash_app = Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        url_base_pathname="/dashboard/",
    )
    dash_app.title = "Minhas Finanças"
    dash_app.layout = create_layout(dash_app, revenue_data, spendings_data)

    return dash_app.server
