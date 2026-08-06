import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados

# Puxa as tabelas da pasta que contém as tabelas
df_sellers = pd.read_csv("../dados/brutos/olist_sellers_dataset.csv")
df_orders = pd.read_csv("../dados/brutos/olist_orders_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")
df_reviews = pd.read_csv("../dados/brutos/olist_order_reviews_dataset.csv")

print(df_reviews[df_reviews["review_id"].duplicated(keep=False)].sort_values("review_id").head(10))