from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from . import ids
from ...data.loader import DataSchema


def render(app, revenue_data, spendings_data) -> html.Div:
    # renders day dropdown component
    all_days: list[str] = (
        revenue_data[DataSchema.DAY].unique().tolist()
        + spendings_data[DataSchema.DAY].unique().tolist()
    )
    unique_days = sorted(set(all_days), key=int)

    @app.callback(
        Output(ids.DAY_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_DAYS_BUTTON, "n_clicks"),
    )
    def select_all_days(n_clicks):
        return unique_days

    return html.Div(
        children=[
            dbc.Label("Dia"),
            dcc.Dropdown(
                options=[{"label": day, "value": day} for day in unique_days],
                value=[],
                className=ids.DAY_DROPDOWN,
                id=ids.DAY_DROPDOWN,
                placeholder="Selecione um dia...",
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Selecionar todos"],
                id=ids.SELECT_ALL_DAYS_BUTTON,
            ),
        ]
    )
