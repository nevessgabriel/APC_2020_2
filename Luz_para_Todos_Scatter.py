import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

df = pd.read_csv('Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv')
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
size = [20, 40, 60, 80, 100]
content = df.read().split("\n")
years = list(map(int, content[8].split(",")[2:-4]))
data0 = []
data1 = []
data2 = []
data3 = []
data4 = []
for l in content:
    ls = l.split(",")
    if ls[1] == "Norte":
        dt = ls[2:-5]
        data0 = list(map(float, ls[2:-5]))
        
    if ls[1] == "Nordeste":
        dt = ls[2:-5]
        data1 = list(map(float, ls[2:-5]))
    
    if ls[1] == "Centro-Oeste":
        dt = ls[2:-5]
        data2 = list(map(float, ls[2:-5]))
        
    if ls[1] == "Sudeste":
        dt = ls[2:-5]
        data3 = list(map(float, ls[2:-5]))
        
    if ls[1] == "Sul":
        dt = ls[2:-5]
        data4= list(map(float, ls[2:-5]))
        
data = [data0, data1, data2, data3, data4]

    
