#Bibliotecas
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)



# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv",encoding="utf8")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))

def filtra_dados(regiao):
    data = []
    #for lê todas as linhas da lista
    for l in content:
        #.split(",") separa por vírgula
        ls = l.split(",")
        #condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
        if ls[1] == regiao:
            #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
            dt = ls[2:-5]
            #lê cada elemento da lista filtrada
            for l in dt:
                #insere na lista data cada elemento l transformado de string para float
                data.append(float(l))
    return data



regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste']#lista das regiões

#-------------------------------------------------Dash--------------------------------------------------------------

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id = "filtro",
        options = [{'label': regiao, 'value': regiao} for regiao in regioes],
        value = "Norte",
        clearable = False
        ),
    dcc.Graph(id = "geracao")
])

@app.callback(
    Output("geracao","figure"),
    Input("filtro","value")
)

def graficos(regiao):
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv",encoding="utf8")
    # f.read lê todo o conteúdo do arquivo e retorna uma string
    # .split("\n") divide essa string do conteudo em linhas
    content = f.read().split("\n")
    
    #lista que armazena energia de cada região
    armazena_data = filtra_dados(regiao)

    #variável que armazena informações do gráfico      
    linha = go.Scatter(x = years, #anos do gráfico, eixo x
                       y = armazena_data, #energia do gráfico, eixo y
                       mode = 'lines', #modo do gráfico, tipo linhas
                       name = 'Geracao [GWh]', #nome das linhas
                       line = {'color': '#38aecc'}) #cor das linhas

    # abre o arquivo
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv",encoding="utf8")
    # f.read lê todo o conteúdo do arquivo e retorna uma string
    # .split("\n") divide essa string do conteudo em linhas
    content = f.read().split("\n")
    
    #lista que armazena energia de cada região
    armazena_data = filtra_dados(regiao)
    #variável que armazena informações do gráfico
    barra = go.Bar(x = years,#anos do gráfico, eixo x
                       y = armazena_data, #energia do gráfico, eixo y
                       name = 'Consumo [GWh]',#nome das barras
                       marker = {'color': '#183446'})#cor das barras


    config = go.Layout( title ='Consumo Vs Geração na Região '+ regiao + ' [GWh]', #título do gráfico
                                    yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                    xaxis={'title':''}) #título eixo x
    trace = [linha, barra] #variável que armazena gráficos
    fig = go.Figure(data=trace, layout=config)
   
    return fig

if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)
