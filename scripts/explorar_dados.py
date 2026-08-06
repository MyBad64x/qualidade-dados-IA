import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados, checar_fora_do_range

# Puxa as tabelas da pasta que contém as tabelas
df_sellers = pd.read_csv("../dados/brutos/olist_sellers_dataset.csv")
df_products = pd.read_csv("../dados/brutos/olist_products_dataset.csv")
df_orders = pd.read_csv("../dados/brutos/olist_orders_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")
df_reviews = pd.read_csv("../dados/brutos/olist_order_reviews_dataset.csv")
df_geolocation = pd.read_csv("../dados/brutos/olist_geolocation_dataset.csv")
df_translation = pd.read_csv("../dados/brutos/product_category_name_translation.csv")

print(checar_orfaos(df_products.dropna(subset=["product_category_name"]), df_translation, "product_category_name"))