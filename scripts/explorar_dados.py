import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados

# Puxa as tabelas da pasta que contém as tabelas
df_products = pd.read_csv("../dados/brutos/olist_products_dataset.csv")

print(checar_valores_zerados(df_products, ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]))