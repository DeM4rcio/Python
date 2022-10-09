import pandas as pd
from pandas.core.frame import DataFrame
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

df_moedas = pd.read_csv('Banco de dados APC/coin_Bitcoin.csv')

media_preco = df_moedas.values.tolist()

Real, Libra, Euro, Kwanza, Yen = 5.16, 1.14, 1.00, 429.98, 143.36

valores = [Real, Libra, Euro, Kwanza, Yen]
valores_2 = ['Real', 'Libra', 'Euro', 'Kwanza', 'Yen']

#Criando lista vazia

valores_media = []

#Pegando as colunas, tirando a média e convertendo pra real

for coluna in media_preco:
  valores_media.append([((coluna[4]+coluna[5])/2)*Real,coluna[2],coluna[3]])

moedas = DataFrame(valores_media, columns=['Media Preco Dia','Moeda', 'Data'])

fig = px.line(moedas, x='Data', y='Media Preco Dia', color='Moeda')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Dropdown(['Real', 'Libra', 'Euro', 'Kwanza', 'Yen'], value='Real', id='botao'),

    dcc.Graph(
        id='grafico',
        figure=fig
    )
])


@app.callback(
    Output('grafico', 'figure'),
    Input('botao', 'value')
)
def update_output(value):
    if value == 'Real':
        media_preco = df_moedas.values.tolist()

        Real, Libra, Euro, Kwanza, Yen = 5.16, 1.14, 1.00, 429.98, 143.36

        valores = [Real, Libra, Euro, Kwanza, Yen]
        valores_2 = ['Real', 'Libra', 'Euro', 'Kwanza', 'Yen']

        #Criando lista vazia

        valores_media = []

        #Pegando as colunas, tirando a média e convertendo pra real

        for coluna in media_preco:
            valores_media.append([((coluna[4]+coluna[5])/2)*Real,coluna[2],coluna[3]])

        moedas = DataFrame(valores_media, columns=['Media Preco Dia','Moeda', 'Data'])

        fig = px.line(moedas, x='Data', y='Media Preco Dia', color='Moeda')
    else:
        media_preco = df_moedas.values.tolist()

        Real, Libra, Euro, Kwanza, Yen = 5.16, 1.14, 1.00, 429.98, 143.36

        valores = [Real, Libra, Euro, Kwanza, Yen]
        valores_2 = ['Real', 'Libra', 'Euro', 'Kwanza', 'Yen']

        #Criando lista vazia

        valores_media = []

        #Pegando as colunas, tirando a média e convertendo pra real

        for coluna in media_preco:
            valores_media.append([((coluna[4]+coluna[5])/2)*valores[valores_2.index(value)],coluna[2],coluna[3]])

        moedas = DataFrame(valores_media, columns=['Media Preco Dia','Moeda', 'Data'])

        fig = px.line(moedas, x='Data', y='Media Preco Dia', color='Moeda')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)