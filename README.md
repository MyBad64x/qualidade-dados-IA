# Pipeline de Qualidade de Dados — E-commerce Olist

## Descrição

Projeto de análise e validação de qualidade de dados aplicado ao dataset público **Brazilian E-Commerce (Olist)**. O objetivo é identificar, documentar e explicar inconsistências reais em um conjunto de dados relacional, combinando validações automatizadas em Python com interpretação técnica gerada por IA generativa (Google Gemini API).

O projeto foi desenvolvido como parte da preparação para o processo seletivo do programa Lighthouse (Indicium), com foco em fundamentos de engenharia de dados, qualidade de dados e integração com IA.

## Dataset

Os dados utilizados são do **Brazilian E-Commerce Public Dataset by Olist**, disponível no Kaggle, contendo aproximadamente 100 mil pedidos realizados entre 2016 e 2018, distribuídos em 9 tabelas relacionadas:

- `olist_customers_dataset` — clientes
- `olist_orders_dataset` — pedidos
- `olist_order_items_dataset` — itens de cada pedido
- `olist_products_dataset` — produtos
- `olist_order_payments_dataset` — pagamentos
- `olist_sellers_dataset` — vendedores
- `olist_order_reviews_dataset` — avaliações
- `olist_geolocation_dataset` — geolocalização por CEP
- `product_category_name_translation` — tradução de categorias (PT → EN)

Os arquivos CSV não estão incluídos neste repositório. Para reproduzir o projeto, baixe o dataset no Kaggle e posicione os arquivos em `dados/brutos/`.


## Estrutura do Projeto

qualidade_dados/
├── dados/
│ ├── brutos/ # CSVs originais do Olist (não versionado)
│ └── processados/ # Dados após tratamento (não versionado)
├── scripts/
│ ├── explorar_dados.py # Exploração inicial e testes ad-hoc
│ ├── funcoes_valid.py # Funções de validação de qualidade
│ ├── gerar_relatorio.py # Geração do relatório consolidado em Markdown
│ └── ia_explicacao.py # Geração de explicações técnicas via IA
├── relatorios/
│ ├── relatorio_qualidade.md # Relatório com resultados das validações
│ └── explicacao_ia.md # Explicações técnicas geradas por IA
├── requirements.txt
├── .gitignore
└── README.md


## Funções de Validação

O módulo `funcoes_valid.py` implementa sete funções de validação reutilizáveis, aplicáveis a qualquer combinação de tabela e coluna:

| Função | Finalidade |
|---|---|
| `checar_nulos(df)` | Conta valores nulos por coluna |
| `checar_duplicados(df, colunas)` | Conta registros duplicados em uma coluna ou combinação de colunas |
| `checar_valores_negativos(df, colunas)` | Conta valores negativos em colunas numéricas |
| `checar_valores_zerados(df, colunas)` | Conta valores iguais a zero em colunas numéricas |
| `checar_fora_do_range(df, coluna, minimo, maximo)` | Conta valores fora de um intervalo esperado |
| `checar_orfaos(df_estrangeiro, df_principal, coluna_chave)` | Verifica integridade referencial entre duas tabelas |
| `checar_sequencia_status_datas(df)` | Valida se pedidos com status "delivered" possuem todas as datas do fluxo de entrega preenchidas |

## Principais Achados

- Nulos em colunas de data de `orders` são, em sua maioria, esperados (refletem etapas do pedido ainda não ocorridas), mas 23 pedidos com status `delivered` apresentam datas do fluxo ausentes — inconsistência real.
- `customer_unique_id` apresenta 3.345 duplicatas esperadas, representando clientes com múltiplas compras.
- 610 produtos possuem cadastro de marketing incompleto; 1 produto está praticamente vazio; 4 produtos físicos apresentam peso 0g.
- 2 pagamentos em cartão de crédito com 0 parcelas registradas (inconsistência); 9 pagamentos com valor R$ 0,00, parte legítima (vouchers) e parte suspeita (tipo `not_defined`).
- Mais de 260 mil linhas duplicadas em `geolocation`, além de 42 registros com coordenadas fora dos limites geográficos do Brasil.
- 814 `review_id` duplicados, identificados como comportamento esperado do sistema (uma mesma avaliação cobrindo múltiplos pedidos), não como erro.
- Integridade referencial validada entre `order_items`↔`orders`, `orders`↔`customers`, `order_items`↔`sellers` e `reviews`↔`orders`, sem registros órfãos.

O detalhamento completo está disponível em `relatorios/relatorio_qualidade.md`.

## Integração com IA Generativa

O script `ia_explicacao.py` utiliza a API do Google Gemini para gerar, a partir dos achados de cada tabela, explicações técnicas em linguagem natural sobre o significado prático de cada inconsistência, seu possível impacto no negócio e a distinção entre problemas reais e comportamentos esperados dos dados. O resultado é salvo em `relatorios/explicacao_ia.md`.

## Tecnologias Utilizadas

- Python
- Pandas
- Google Gemini API (google-genai)
- python-dotenv
- Git / GitHub

## Como Executar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd qualidade_dados
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows
source venv/bin/activate       # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Baixe o dataset do Kaggle e posicione os arquivos CSV em `dados/brutos/`.

5. Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini:

GEMINI_API_KEY=sua_chave_aqui

6. Execute os scripts na ordem:
```bash
cd scripts
python explorar_dados.py
python gerar_relatorio.py
python ia_explicacao.py
```

## Autor: Alberto Zgraia Neto (MyBad64x)

Projeto desenvolvido como parte de estudos em engenharia de dados e IA aplicada, com foco em preparação para processos seletivos na área de Dados/IA.