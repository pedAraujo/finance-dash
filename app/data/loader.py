import pandas as pd


class DataSchema:
    DATE = "Data"
    YEAR = "Ano"
    MONTH = "Mes"
    DAY = "Dia"
    TRANSACTION = "Movimentacao"
    VALUE_BRL = "ValorBRL"
    TRANSACTION_TYPE = "Modalidade"
    CATEGORY = "Categoria"
    SUBCATEGORY = "Subcategoria"
    RECURRENT = "Recorrente"
    DESCRIPTION = "Descrição"
    VALUE_USD = "ValorUSD"
    EXCHANGE_RATE = "CotacaoNaData"


def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.DATE: str,
            DataSchema.YEAR: str,
            DataSchema.MONTH: str,
            DataSchema.DAY: str,
            DataSchema.TRANSACTION: str,
            DataSchema.VALUE_BRL: float,
            DataSchema.TRANSACTION_TYPE: str,
            DataSchema.CATEGORY: str,
            DataSchema.SUBCATEGORY: str,
            DataSchema.RECURRENT: str,
            DataSchema.DESCRIPTION: str,
            DataSchema.VALUE_USD: float,
            DataSchema.EXCHANGE_RATE: float,
        },
        parse_dates=["Data"],
    )
    return data
