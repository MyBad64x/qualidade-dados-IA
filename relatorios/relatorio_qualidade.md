# Relatório de Qualidade de Dados — E-commerce Olist

## Tabela: Customers

**Nulos por coluna:**
```
customer_id                 0
customer_unique_id          0
customer_zip_code_prefix    0
customer_city               0
customer_state              0
dtype: int64
```

**Duplicatas (customer_id):**
0

## Tabela: Orders

**Nulos por coluna:**
```
order_id                            0
customer_id                         0
order_status                        0
order_purchase_timestamp            0
order_approved_at                 160
order_delivered_carrier_date     1783
order_delivered_customer_date    2965
order_estimated_delivery_date       0
dtype: int64
```

**Duplicatas (order_id):**
0

**Inconsistência: pedidos entregues com data faltando:**
23

## Tabela: Order Items

**Nulos por coluna:**
```
order_id               0
order_item_id          0
product_id             0
seller_id              0
shipping_limit_date    0
price                  0
freight_value          0
dtype: int64
```

**Duplicatas (order_id + order_item_id):**
0

**Valores negativos (price, freight_value):**
```
price            0
freight_value    0
dtype: int64
```

## Tabela: Products

**Nulos por coluna:**
```
product_id                      0
product_category_name         610
product_name_lenght           610
product_description_lenght    610
product_photos_qty            610
product_weight_g                2
product_length_cm               2
product_height_cm               2
product_width_cm                2
dtype: int64
```

**Duplicatas (product_id):**
0

**Valores zerados (peso e dimensões):**
```
product_weight_g     4
product_length_cm    0
product_height_cm    0
product_width_cm     0
dtype: int64
```

**Observação:** 610 produtos possuem cadastro de marketing incompleto (categoria, nome, descrição e fotos ausentes simultaneamente). Um produto específico (`product_id: 5eb564652db742ff8f28759cd8d2652a`) está praticamente vazio, sem nenhuma informação de cadastro ou dimensões preenchida.

## Tabela: Payments

**Nulos por coluna:**
```
order_id                0
payment_sequential      0
payment_type            0
payment_installments    0
payment_value           0
dtype: int64
```

**Parcelas zeradas (payment_installments):**
2

**Valores de pagamento zerados (payment_value):**
9

**Observação:** 2 pagamentos em cartão de crédito (`credit_card`) apresentam 0 parcelas registradas, o que é logicamente inválido — todo pagamento efetuado precisa ter no mínimo 1 parcela. Além disso, dos 9 pagamentos com valor R$ 0,00, 6 são do tipo `voucher` (possivelmente legítimos, representando vouchers sem saldo remanescente usados como pagamento complementar) e 3 são do tipo `not_defined` (suspeitos, já que esse tipo de pagamento não está claramente documentado/classificado).

## Relacionamento entre Tabelas

**Itens de pedido sem pedido correspondente (order_items → orders):**
0

**Pedidos sem cliente correspondente (orders → customers):**
0

## Tabela: Sellers

**Nulos por coluna:**
```
seller_id                 0
seller_zip_code_prefix    0
seller_city               0
seller_state              0
dtype: int64
```

**Duplicatas (seller_id):**
0

**Vendedores órfãos (order_items → sellers):**
0

**Observação:** tabela sem inconsistências encontradas — nulos, duplicatas e integridade referencial todos limpos.

## Tabela: Reviews

**Nulos por coluna:**
```
review_id                      0
order_id                       0
review_score                   0
review_comment_title       87656
review_comment_message     58247
review_creation_date           0
review_answer_timestamp        0
dtype: int64
```

**Duplicatas (review_id):**
814

**Reviews órfãs (reviews → orders):**
0

**Observação:** review_score sempre dentro do intervalo esperado (1 a 5). Os 814 casos de review_id duplicado não representam erro — correspondem a uma mesma pesquisa de satisfação respondida cobrindo múltiplos pedidos do mesmo cliente (nota, comentário e datas idênticos entre os pares). Nulos em review_comment_title e review_comment_message são esperados, já que o preenchimento de comentário é opcional.

