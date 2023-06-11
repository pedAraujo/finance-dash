from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from . import ids
from ...data.loader import DataSchema


def render(app, revenue_data, spendings_data) -> html.Div:
    # renders month dropdown component
    all_months: list[str] = (
        revenue_data[DataSchema.MONTH].unique().tolist()
        + spendings_data[DataSchema.MONTH].unique().tolist()
    )
    unique_months = sorted(set(all_months), key=int)

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
    )
    def select_all_months(n_clicks):
        return unique_months

    return html.Div(
        children=[
            dbc.Label("Mês"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                className=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                placeholder="Selecione um mês...",
                multi=False,
            ),
            html.Button(
                className="dropdown-button",
                children=["Selecionar todos"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
            ),
        ]
    )
