from dash import html, dcc
from dash.dependencies import Input, Output

from . import ids
from ...data.loader import DataSchema


def render(app, revenue_data, spendings_data) -> html.Div:
    # renders year dropdown component
    all_years: list[str] = (
        revenue_data[DataSchema.YEAR].unique().tolist()
        + spendings_data[DataSchema.YEAR].unique().tolist()
    )
    unique_years = sorted(set(all_years), key=int)

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
    )
    def select_all_years(n_clicks):
        return unique_years

    return html.Div(
        children=[
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in all_years],
                value=all_years,
                placeholder="Selecione um ano...",
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Selecionar todos"],
                id=ids.SELECT_ALL_YEARS_BUTTON,
            ),
        ]
    )
