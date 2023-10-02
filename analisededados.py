# PASSO 1 - PERCORRER TODOS OS ARQUIVOS DA PASTA BASE DE DADOS (PASTA VENDAS)
import os
import pandas as pd
import plotly.express as px 

lista_arquivos = os.listdir("C:/workspace JS/analise-de-dados_vendas/Vendas")
tabela_total = pd.DataFrame()

# PASSO 2 - IMPORTAR AS BASES DE DADOS DE VENDAS
for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv (f"C:/workspace JS/analise-de-dados_vendas/Vendas/{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index = True)

# PASSO 3 - TRATAR / COMPILAR BASE DE DADOS
print(tabela_total)

# PASSO 4 - PRODUTO MAIS VENDIDO (QUANTIDADE)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos [["Quantidade Vendida"]].sort_values (by ="Quantidade Vendida", ascending = False)
print(tabela_produtos)

# PASSO 5 - PRODUTO DE MAIOR FATURAMENTO (FATURAMENTO)
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento [["Faturamento"]].sort_values (by ="Faturamento", ascending = False)
print(tabela_faturamento)

# PASSO 6 - LOJA/CIDADE QUE MAIS VENDEU (FATURAMENTO)
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values (by ="Faturamento", ascending = False)
print(tabela_lojas)

# PASSO 7 - GRÁFICO/DASHBOARD
grafico = px.bar(tabela_lojas, x = tabela_lojas.index, y = "Faturamento")
grafico.show()


