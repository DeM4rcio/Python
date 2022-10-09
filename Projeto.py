from dash import dcc, html
from dash.dependencies import Input, Output
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as px
import numpy as np
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash
import matplotlib.pyplot as plt

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

# aumentano a escala para melhor visualização
constante_de_multiplicacao = 207
for x in range(len(price_dolar)):
  price_dolar[x] = price_dolar[x] * constante_de_multiplicacao


plt.plot(ano_dolar, price_dolar, linestyle='--',
         marker='o', color='blue', markersize=4)
plt.plot(ano_bitcoin, price_bitcoin, linestyle='--',
         marker='o', color='red', markersize=4)

plt.xlabel('Ano', fontsize=15)
plt.ylabel('Price ( USD$)', fontsize=15)

plt.title('Perfil de temperatura do forno')

plt.legend(['Variação do dólar','Variação do Bitcoin'], fontsize=14)

axes = plt.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)

plt.figure(figsize=(10.5, 9))

plt.show()
