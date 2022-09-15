import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

colors = {
    'background': '#111111',
    # 'text': '#7FDBFF'
}


app.layout = html.Div(children=[
    html.H1(children='Group Chat Analyser'),

    html.Div(children='''
        A web application framework for your WhtasApp Group data.
    '''),


])













if __name__ == '__main__':
    app.run_server(debug=True)

