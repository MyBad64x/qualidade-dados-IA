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

