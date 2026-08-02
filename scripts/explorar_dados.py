import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas

# Puxa as tabelas da pasta que contém as tabelas
df_customers = pd.read_csv("../dados/brutos/olist_customers_dataset.csv")
df_orders = pd.read_csv("../dados/brutos/olist_orders_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")

print(checar_nulos(df_orders))
print(checar_duplicados(df_customers, "customer_id"))
print(checar_duplicados(df_order_items, ["order_id", "order_item_id"]))
print(checar_valores_negativos(df_order_items, ["price", "freight_value"]))
print(checar_sequencia_status_datas(df_orders))