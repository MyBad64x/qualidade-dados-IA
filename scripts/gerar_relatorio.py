import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos

# Carregando os dados
df_customers = pd.read_csv("../dados/brutos/olist_customers_dataset.csv")
df_orders = pd.read_csv("../dados/brutos/olist_orders_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")

# Montando o conteúdo do relatório
relatorio = "# Relatório de Qualidade de Dados — E-commerce Olist\n\n"

# --- Customers ---
relatorio += "## Tabela: Customers\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_customers))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (customer_id):**\n"
relatorio += f"{checar_duplicados(df_customers, 'customer_id')}\n\n"

# --- Orders ---
relatorio += "## Tabela: Orders\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_orders))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (order_id):**\n"
relatorio += f"{checar_duplicados(df_orders, 'order_id')}\n\n"

relatorio += "**Inconsistência: pedidos entregues com data faltando:**\n"
relatorio += f"{checar_sequencia_status_datas(df_orders)}\n\n"

# --- Order Items ---
relatorio += "## Tabela: Order Items\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_order_items))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (order_id + order_item_id):**\n"
relatorio += f"{checar_duplicados(df_order_items, ['order_id', 'order_item_id'])}\n\n"

relatorio += "**Valores negativos (price, freight_value):**\n```\n"
relatorio += str(checar_valores_negativos(df_order_items, ["price", "freight_value"]))
relatorio += "\n```\n\n"

# --- Relacionamento entre Tabelas ---
relatorio += "## Relacionamento entre Tabelas\n\n"

relatorio += "**Itens de pedido sem pedido correspondente (order_items → orders):**\n"
relatorio += f"{checar_orfaos(df_order_items, df_orders, 'order_id')}\n\n"

relatorio += "**Pedidos sem cliente correspondente (orders → customers):**\n"
relatorio += f"{checar_orfaos(df_orders, df_customers, 'customer_id')}\n\n"

# Salvando o arquivo
with open("../relatorios/relatorio_qualidade.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(relatorio)

print("Relatório gerado com sucesso!")