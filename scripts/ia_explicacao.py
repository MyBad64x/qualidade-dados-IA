import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

achados = {
    "Customers": "Nenhuma inconsistência encontrada. Nulos: 0. Duplicatas em customer_id: 0. customer_unique_id possui 3345 duplicatas, o que é esperado (representa clientes recorrentes).",
    "Orders": "23 pedidos com status 'delivered' possuem ao menos uma das datas do fluxo de entrega ausente (order_approved_at, order_delivered_carrier_date ou order_delivered_customer_date), o que é logicamente inconsistente para um pedido já entregue.",
    "Order Items": "Nenhuma inconsistência encontrada. order_id + order_item_id formam chave composta única. Sem valores negativos em price ou freight_value. Sem itens órfãos em relação a orders.",
    "Products": "610 produtos possuem cadastro de marketing incompleto (categoria, nome, descrição e fotos ausentes simultaneamente). 1 produto está praticamente vazio, sem nenhuma informação preenchida. 4 produtos da categoria 'cama_mesa_banho' possuem peso 0g, o que é fisicamente implausível.",
    "Payments": "2 pagamentos em cartão de crédito possuem 0 parcelas registradas, o que é logicamente inválido. 9 pagamentos possuem valor R$ 0,00: 6 são do tipo voucher (possivelmente legítimo), 3 são do tipo not_defined (suspeito).",
    "Sellers": "Nenhuma inconsistência encontrada. Sem nulos, sem duplicatas, sem vendedores órfãos.",
    "Reviews": "814 review_id duplicados, porém não representam erro: correspondem a uma mesma pesquisa de satisfação respondida cobrindo múltiplos pedidos do mesmo cliente. review_score sempre dentro do intervalo esperado (1 a 5).",
    "Geolocation": "Mais de 260 mil linhas totalmente duplicadas. 42 linhas possuem coordenadas geográficas fora dos limites plausíveis do Brasil, indicando possível erro de geocodificação.",
    "Category Translation": "13 categorias usadas na tabela de produtos não possuem tradução correspondente nesta tabela."
}

def gerar_explicacao(nome_tabela, resumo_achados):
    prompt = f"""
Você é um analista de qualidade de dados. Abaixo está um resumo técnico dos problemas encontrados na tabela "{nome_tabela}" de um dataset de e-commerce.

Resumo dos achados:
{resumo_achados}

Escreva uma explicação técnica clara, em português, sobre:
1. O que esses achados significam na prática
2. Qual o possível impacto no negócio, se houver
3. Se algum desses pontos não representa um problema real, explique por quê

Seja objetivo, use no máximo 150 palavras.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

relatorio_ia = "# Explicações Geradas por IA — Qualidade de Dados\n\n"

for tabela, resumo in achados.items():
    print(f"Gerando explicação para: {tabela}...")
    explicacao = gerar_explicacao(tabela, resumo)
    relatorio_ia += f"## {tabela}\n\n{explicacao}\n\n"

with open("../relatorios/explicacao_ia.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(relatorio_ia)

print("Relatório de explicações gerado com sucesso!")