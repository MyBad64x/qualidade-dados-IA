import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados

# Puxa as tabelas da pasta que contém as tabelas
df_payments = pd.read_csv("../dados/brutos/olist_order_payments_dataset.csv")

pd.set_option("display.max_columns", None)
print(df_payments[df_payments["payment_value"] == 0])