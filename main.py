# Загрузим необходимые пакеты
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

#  Объяснение данных строк пока опускается, будет объяснено далее
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv("test1.csv")
fig = px.pie(df, names="region", values="price", hole=0.9)
# fig.layout.height = 2000
# fig.layout.width = 1000
fig1 = px.pie(df, names="region", values="price", hole=0.9)
# fig1.layout.height = 2000
# fig1.layout.width = 1000

app.layout = html.Div([
    html.H1(
        children='Ваш налоговый проводник!',
        style={
            'textAlign': 'center'
        }
    ),
    html.Div(
        children='''Здесь вам поднимут ваше чувство налогоплательщика!!!''',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.Graph(
        id='1',
        figure=fig,
        style={
            'textAlign': 'center'
        }
    ),
    html.Label('Укажите период'),
    dcc.Input(type='text', placeholder='Месяц', style={"width": 150, "margin-right": 10}),
    dcc.Input(type='text', placeholder='Год', style={"width": 150}),
        html.Label('Выберите свой регион'),
    dcc.Dropdown(
        options=[
            {'label': 'Московская область', 'value': 'NYC'},
            {'label': 'Краснодарский край', 'value': 'MTL'},
            {'label': 'Республика Татарстан', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        style={"width": 310},
    ),
    html.Label('Сумма уплаченного налога:'),
    dcc.RadioItems(
        options=[
            {'label': 'Рассчитать сумму уплаченного налога', 'value': 'NYC'},
            {'label': 'Укажете самостоятельно сумму налога', 'value': 'MTL'},
        ],
        value='MTL'
    ),
    dcc.Input(type='text', placeholder='Укажите свой доход', style={"width": 310}),
    dcc.Graph(
        id='2',
        figure=fig1
    )
 ]#, style={'columnCount': 2}
)

if __name__ == '__main__':
    app.run_server(debug=True)
