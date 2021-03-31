import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
years = list(map(int, content[8].split(",")[2:-4]))
data = []
for l in content:
    ls = l.split(",")
    if ls[1] == "Sudeste":
        dt = ls[2:-5]
        data = list(map(float, ls[2:-5]))
        
linha = go.Scatter(x = years,
                   y = data, 
                   mode = 'lines',
                   name = 'Geracao [GWh]',
                   line = {'color': '#38aecc'})

# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
years = list(map(int, content[8].split(",")[2:-4]))
data = []
for l in content:
    ls = l.split(",")
    if ls[1] == "Sudeste":
        dt = ls[2:-5]
        data = list(map(float, ls[2:-5]))

barra = go.Bar(x = years,
                   y = data, 
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})


config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)
