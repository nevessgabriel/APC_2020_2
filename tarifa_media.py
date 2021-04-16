# Bibliotecas
import xlrd 
import dash_core_components as dcc
import plotly.graph_objects as go
import dash
import pandas as pd
import re
import dash_html_components as html
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots


# ------- Lendo dados do arquivo
df = xlrd.open_workbook('202.xls')            # Acessa o arquivo 
tabela = df.sheet_by_name('Tabela 2.14')      # Lê a tabela 

# ------- Extraindo dados do arquivo
dados = []                                    # Declarando uma matriz 
coluna = []
for i in range(8):                            # Total de anos que serão codados (0 a 8)                      
    j = i + 1                                 # Variável que receberá os valores da coluna
    coluna = tabela.col_values(j)             # col_values recebe os valores das tabelas e vai colocar na coluna
    dados.append(coluna[10:15])               # Adiciona os valores da coluna e transforma em um dado 

# ------- Extraindo dados do arquivo
dados = []                                    # Declarando uma matriz 
coluna = []
for i in range(8):                            # Total de anos que serão codados (0 a 8)                      
    j = i + 1                                 # Variável que receberá os valores da coluna
    coluna = tabela.col_values(j)             # col_values recebe os valores das tabelas e vai colocar na coluna
    dados.append(coluna[10:15])               # Adiciona os valores da coluna e transforma em um dado 
#print(dados)
# ----------------------- Laço for dos anos
x = int(input())                                                  
h = 0                                               # Variável vazia para coluna
m = 0                                               # Variável vazia para linha 
tabela = [[1 for i in range(2)] for i in range(5)]  # Matriz 5 x 2 
for q in range(5):                                  # q armazena as regiões que o range vai rodar 5x                              
    for l in range(1):                             # Formando uma Matriz 5x2 
        tabela[h][0] = dados[0][q]                   
        tabela[h][1] = dados[x][q]                 
        h += 1
        m += 1

#print(tabela)
anos = []      
for dado in tabela:                              # Procurar o dado em uma tabela
    anos.append(dado[1])                         # Adiciona os valores dos dados aos anos 
valor = []
for dado in tabela:
    valor.append(dado[0])
#print(anos)
#print(valor)

# -----------Gráfico
z = 2011 + x                                    # 2011 + (0-8) dos anos desejados 
barra = go.Bar(x= anos,                         # eixo x, em anos
               y= valor,                        # eixo y, região
               orientation='h',                 # gráfico na horizontal
               name='Tarifa Média [R$/MWh]',    # Nome dos gráficos
               marker={'color': '#38AECC'})     # Cor dos gráficos   
 
config = go.Layout(title='Tarifa Média por Região [R$/MWh]- {}'.format(z), # Título do gráfico 
                   yaxis={'title': 'região'},                              # Título do eixo y 
                   xaxis={'title': ''})                                    # Título do eixo x
trace = [barra]                                                     # Variável que armazena o tipo de gráfico
fig = go.Figure(data=trace, layout=config)                                  # Transforma em fig as informações
 
py.iplot(fig)                                                          # Visualiza o gráfico
