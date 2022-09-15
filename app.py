import dash
from dash import Dash, html, dcc 
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


app = Dash(__name__)


app.layout = html.Div(className = "content", children=[
    
    html.Div(
        className="app-header",
        children=[
            html.H1('Group Chat Analyser', id='tit'),
            # html.H6('A web application framework for your WhatsApp Group data.')
            html.Div('A web application framework for your WhatsApp Group data.', id='descr')
        ]
),
    html.Div(
        id='sidebar'
        ),
    html.Div(
        id='rightbar'
    ),
    html.Div(
        id='footer'
    )
])











if __name__ == '__main__':
    app.run_server(debug=True)

