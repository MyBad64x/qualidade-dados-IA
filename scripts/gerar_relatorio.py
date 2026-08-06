import pandas as pd
from funcoes_valid import checar_nulos, checar_duplicados, checar_valores_negativos, checar_sequencia_status_datas, checar_orfaos, checar_valores_zerados

# Carregando os dados
df_customers = pd.read_csv("../dados/brutos/olist_customers_dataset.csv")
df_orders = pd.read_csv("../dados/brutos/olist_orders_dataset.csv")
df_order_items = pd.read_csv("../dados/brutos/olist_order_items_dataset.csv")
df_products = pd.read_csv("../dados/brutos/olist_products_dataset.csv")
df_payments = pd.read_csv("../dados/brutos/olist_order_payments_dataset.csv")
df_sellers = pd.read_csv("../dados/brutos/olist_sellers_dataset.csv")
df_reviews = pd.read_csv("../dados/brutos/olist_order_reviews_dataset.csv")

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

# --- Products ---
relatorio += "## Tabela: Products\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_products))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (product_id):**\n"
relatorio += f"{checar_duplicados(df_products, 'product_id')}\n\n"

relatorio += "**Valores zerados (peso e dimensões):**\n```\n"
relatorio += str(checar_valores_zerados(df_products, ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]))
relatorio += "\n```\n\n"

relatorio += "**Observação:** 610 produtos possuem cadastro de marketing incompleto (categoria, nome, descrição e fotos ausentes simultaneamente). Um produto específico (`product_id: 5eb564652db742ff8f28759cd8d2652a`) está praticamente vazio, sem nenhuma informação de cadastro ou dimensões preenchida.\n\n"

# --- Payments ---
relatorio += "## Tabela: Payments\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_payments))
relatorio += "\n```\n\n"

relatorio += "**Parcelas zeradas (payment_installments):**\n"
relatorio += f"{checar_valores_zerados(df_payments, 'payment_installments')}\n\n"

relatorio += "**Valores de pagamento zerados (payment_value):**\n"
relatorio += f"{checar_valores_zerados(df_payments, 'payment_value')}\n\n"

relatorio += "**Observação:** 2 pagamentos em cartão de crédito (`credit_card`) apresentam 0 parcelas registradas, o que é logicamente inválido — todo pagamento efetuado precisa ter no mínimo 1 parcela. Além disso, dos 9 pagamentos com valor R$ 0,00, 6 são do tipo `voucher` (possivelmente legítimos, representando vouchers sem saldo remanescente usados como pagamento complementar) e 3 são do tipo `not_defined` (suspeitos, já que esse tipo de pagamento não está claramente documentado/classificado).\n\n"

# --- Relacionamento entre Tabelas ---
relatorio += "## Relacionamento entre Tabelas\n\n"

relatorio += "**Itens de pedido sem pedido correspondente (order_items → orders):**\n"
relatorio += f"{checar_orfaos(df_order_items, df_orders, 'order_id')}\n\n"

relatorio += "**Pedidos sem cliente correspondente (orders → customers):**\n"
relatorio += f"{checar_orfaos(df_orders, df_customers, 'customer_id')}\n\n"

# --- Sellers ---
relatorio += "## Tabela: Sellers\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_sellers))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (seller_id):**\n"
relatorio += f"{checar_duplicados(df_sellers, 'seller_id')}\n\n"

relatorio += "**Vendedores órfãos (order_items → sellers):**\n"
relatorio += f"{checar_orfaos(df_order_items, df_sellers, 'seller_id')}\n\n"

relatorio += "**Observação:** tabela sem inconsistências encontradas — nulos, duplicatas e integridade referencial todos limpos.\n\n"

# --- Reviews ---
relatorio += "## Tabela: Reviews\n\n"
relatorio += "**Nulos por coluna:**\n```\n"
relatorio += str(checar_nulos(df_reviews))
relatorio += "\n```\n\n"

relatorio += "**Duplicatas (review_id):**\n"
relatorio += f"{checar_duplicados(df_reviews, 'review_id')}\n\n"

relatorio += "**Reviews órfãs (reviews → orders):**\n"
relatorio += f"{checar_orfaos(df_reviews, df_orders, 'order_id')}\n\n"

relatorio += "**Observação:** review_score sempre dentro do intervalo esperado (1 a 5). Os 814 casos de review_id duplicado não representam erro — correspondem a uma mesma pesquisa de satisfação respondida cobrindo múltiplos pedidos do mesmo cliente (nota, comentário e datas idênticos entre os pares). Nulos em review_comment_title e review_comment_message são esperados, já que o preenchimento de comentário é opcional.\n\n"

# Salvando o arquivo
with open("../relatorios/relatorio_qualidade.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(relatorio)

print("Relatório gerado com sucesso!")