import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

#importa banco de dados aleatório
df = pd.read_csv('kc_house_data.csv')

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
