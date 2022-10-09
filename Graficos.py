from dash import dcc, html
from dash.dependencies import Input, Output
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as px
import numpy as np
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash

df = pd.read_csv('Banco de dados APC/coin_Bitcoin.csv')
df1 = pd.read_csv('Banco de dados APC/O_brabo.csv')

#transforma o Bitcoin.csv em lista
lista_bitcoin = df.values.tolist()

#transforma o Dolar.csv em lista
lista_dolar = df1.values.tolist()

#alocando os anos/open em uma nova lista (data_frame_dolar)

ano_dolar = []
price_dolar = []

for linha in lista_dolar:
  ano_dolar.append(linha[0])
  price_dolar.append(linha[1])
# change = 5 ; close = 1

# tratamento dos dados dolar ano


def hunter(ano_str):
  for x in range(0, len(ano_dolar) - 1):
    procura = ano_dolar[x].find(ano_str)
    if (procura >= 0):
      ano_dolar.pop(x)
    else:
      break


anos_fora_do_escopo = ["2001", "2002", "2003",
                       "2004", "2005", "2006",
                       "2007", "2008", "2009",
                       "2010", "2011", "2012"]
for y in range(100):
  for x in anos_fora_do_escopo:
      hunter(x)

#tratamento dos dados dolar price

numero_secreto = 142857


def hunter_price(numero):
 for x in range(0, 3084):
    if (price_dolar[0] != numero):
      price_dolar.pop(0)
    else:
      break


hunter_price(numero_secreto)

#alocando os anos/open em uma nova lista (data_frame_anos)
ano_bitcoin = []
price_bitcoin = []

for linha in lista_bitcoin:
  ano_bitcoin.append(linha[3])
  price_bitcoin.append(linha[7])
# open = 6 ; close = 7



# GRÁFICO PRICE EM RELAÇÃO AO ANO (2013 A 2020)----DOLÁR


plot1 = px.line(x=ano_dolar, y=price_dolar, title= 'Dólar', labels={
    y: "Price(USD$)",
    x: "Anos corridos"
}, color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white',)



plot2 = px.line(y=price_bitcoin, x=ano_bitcoin, title='Bitcoin',
                color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white')
plot2.update_yaxes(showticklabels=False)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

#app = Dash(__name__)


app.layout = html.Div(children=[
    html.H4(children='Comparação entre Bitcoin e dolár'),
    dcc.Dropdown(['Gráfico Dólar', 'Gráfico Bitcoin',"Comparação"],
                 value='Gráfico Dólar', id='Moedas'),

    dcc.Graph(
        id='graph',
        figure=plot1
    ),

])


@app.callback(
    Output("graph", "figure"),
    Input("Moedas", "value")
)
def atualizar_output(value):
    if value == "Gráfico Dólar":
      return plot1
    elif value == "Gráfico Bitcoin":
      return plot2

   
if __name__ == '__main__':
    app.run_server(debug=True)



