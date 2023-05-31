from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids
from ...data.loader import DataSchema


def render(app, revenue_data, spendings_data):
    # renders bar chart component

    return html.Div(id=ids.BAR_CHART)
