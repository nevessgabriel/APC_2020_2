import json
import plotly.express as px
import plotly.graph_objs as go


#renomeia as siglas para relacionar as do arquivo json com as do arquivo csv
def name_to_sigla(name):
    if name == "Norte":
        return "N"
    if name == "Nordeste":
        return "NE"
    if name == "Centro-Oeste":
        return "CO"
    if name == "Sudeste":
        return "SE"
    if name == "Sul":
        return "S"

# abre o arquivo GEOJSON dividindo o mapa por região
f = open("brazil_reg.json")
#lê o arquivo json
br = json.loads(f.read())

# abre o arquivo de dados
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")
# .split("\n") divide essa string do conteudo em linhas
lines = f.read().split("\n") 
#lista vazia que armazena as siglas
siglas = []
#lista vazia que armazena os dados de população
populations = []
#os anos podem ser alterados nessa linha
year = '2018'
#lê as linhas começando da linha 10 e excluindo as duas últimas linhas
for l in lines[10:-2]:
    #.split(",") separa elementos por vírgula da lista
    ls = l.split(",")
    #insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista
    siglas.append(name_to_sigla(ls[1]))
    # transforma de float para inteiro todo elemento que esteja na penultima posição da lista
    population_str = ls[int(year[-1])]
    if population_str == '  -   ':
        population_str == 0
    else:
        population_str == float(population_str)
    population = float(population_str)
    #insere na lista population cada elemento de population
    populations.append(population)

#cria dicionario que relacionacona cada regiao por cigla e cada valor de populacao     
d = {"regiao": siglas, "populacao": populations}

#grafico de heatmap, com geojson dividido por região do br
#o valor avaliado é o de populaçao
fig = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                           color_continuous_scale="Blues", #cor definida
                            featureidkey="properties.SIGLA", #chave de interesse 
                           range_color=(0, 200), #a internsidade das cores
                           scope="south america", #mapa da america do sul
                           labels={'populacao':'População (mil)'}#label do gráfico
                          )
fig.update_layout(
    title_text = 'Distribuição Regional do Programa Luz Para Todos no Ano de 2018', #título do gráfico
)

fig.show()#plota gráfico
