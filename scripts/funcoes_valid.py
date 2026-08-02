'''
funcoes_valid.py

Parte de funções de validação de dados, como checagem de nulos, 
duplicados, tipos de dados, etc.
'''

def checar_nulos(df):
    return df.isnull().sum()

def checar_duplicados(df, colunas):
    return df[colunas].duplicated().sum()

def checar_valores_negativos(df, colunas):
    return (df[colunas] < 0).sum()

def checar_sequencia_status_datas(df):
    return (
        df
        [df["order_status"] == "delivered"]
        [[
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]]
        .isnull()
        .any(axis=1)
        .sum()
    )