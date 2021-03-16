import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

#importa banco de dados aleatório
df = pd.read_csv('kc_house_data.csv')

# Gerando gráficos para casas que tem 1 quarto
trace1 = go.Box(y = df.loc[df['bedrooms'] == 1, 'price'],
                name = 'Casas com 1 quarto',
                marker = {'color': '#f39c12'})
# Gráfico de caixa para casas com 2 quartos
trace2 = go.Box(y = df.loc[df['bedrooms'] == 2, 'price'],
                name = 'Casas com 2 quartos',
                marker = {'color': '#e67e22'})
# Gráfico de caixa para casas com 3 quartos
trace3 = go.Box(y = df.loc[df['bedrooms'] == 3, 'price'],
                name = 'Casas com 3 quartos',
                marker = {'color': '#d35400'})
# Gráfico para casas de quatro quartos
trace4 = go.Box(y = df.loc[df['bedrooms'] == 4, 'price'],
                name = 'Casas com 4 quartos',
                marker = {'color': '#e74c3c'})
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(title = 'Dispersão de preços para casas com diferentes quartos',
                   titlefont = {'family': 'Arial',
                                'size': 22,
                                'color': '#7f7f7f'},
                   xaxis = {'title': 'Número de quartos'},
                   yaxis = {'title': 'Preço'},
                   paper_bgcolor = 'rgb(243, 243, 243)',
                   plot_bgcolor = 'rgb(243, 243, 243)')
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

# Gráfico de linha
linha = go.Scatter(x = ['2012', '2013', '2014', '2015', '2016'],
                    y = [50, 100, 150, 200, 250],
                    mode = 'lines',
                    name = 'Geracao',
                    line = {'color': '#38aecc'})
# Gráfico de barras
barra = go.Bar(x = ['2012', '2013', '2014', '2015', '2016'],
                    y = [50, 100, 150, 200, 250],
                    name = 'Consumo',
                    marker = {'color': '#183446'})
data = [linha, barra]
py.iplot(data)
