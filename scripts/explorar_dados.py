import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados

# Puxa as tabelas da pasta que contém as tabelas
df_sellers = pd.read_csv("../dados/brutos/olist_sellers_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")

print(checar_nulos(df_sellers))
print(checar_duplicados(df_sellers, "seller_id"))
print(checar_orfaos(df_order_items, df_sellers, "seller_id"))