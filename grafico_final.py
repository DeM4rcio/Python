import pandas as pd
from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px 

app = Dash(__name__)

#Ler .csv
df = pd.read_csv('Banco de dados APC/coin_Bitcoin.csv')
df_array = df.values

#Gráfico de linha por dia
marketcap = []
dias = []

for linha in df_array:
    dias.append(linha[3])
    marketcap.append(linha[9])

fig1 = px.line(
    x=dias,
    y=marketcap,
)    

#Gráfico de linha por ano

#Filtro do eixo X
contador = 0
anos = []
dias_2013 = []
while contador < 2991:
  dias[contador] = dias[contador].split('-')  
  anos.append(dias[contador][0])
  contador = contador+1

anos = sorted(set(anos))

#Filtro do eixo y

marketdic =	{
  '2013': [], # Ano/Key : valor(es) = (lista vazia)
  '2014': [],
  '2015': [],
  '2016': [],
  '2017': [],
  '2018': [],
  '2019': [],
  '2020': [],
  '2021': [],
}

cont = 0
while cont < 2991:
  for linha in df_array:
    for key in marketdic:
      if key == dias[cont][0]:
        marketdic[key].append(linha[9])
    cont = cont+1

def media(x):
  y = sum(marketdic[(x)])/len(marketdic[(x)])
  return y

marketcap_media = []
for key in marketdic:
  marketcap_media.append(media(key))

fig2 = px.line(
    x=anos,
    y=marketcap_media,
    title = 'Média anual do Marketcap do Bitcoin'
)

marketdic2 =	{
  '2013': [], # Ano/Key : valor(es) = (lista vazia)
  '2014': [],
  '2015': [],
  '2016': [],
  '2017': [],
  '2018': [],
  '2019': [],
  '2020': [],
  '2021': [],
}

c = 0
while c < 2991:
  for linha in df_array:
    for key in marketdic2:
      if key == dias[c][0]:
        marketdic2[key].append(linha[3])
    c = c+1


app.layout = html.Div(children=[
    html.H1(children='Criptomoedas',), 
    html.H3(children='Gráfico do marketcap do Bitcoin por ano'), 
    html.Div(children='''
        Obs: Esse gráfico mostra a variação do marketcap anual.
    '''), 

    dcc.Dropdown(anos, value='2013' , id='anos'),

    dcc.Graph(
        id= 'Gráfico_Bitcoin',
        figure= fig1 
    )
])

@app.callback(
    Output('Gráfico_Bitcoin', 'figure'),
    Input('anos', 'value')
)
def atualizar_output(value):
    if value != None:
        for key in marketdic:
            if value == key:
                fig1 = px.line(
                    x = marketdic2[key],
                    y = marketdic[key]
                )
        return fig1
    else:
        return fig2

# Colocando servidor pra rodar
if __name__ == '__main__':
     app.run_server(debug=True)
