import dash
from dash import Dash, html, dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# For Bootstrap Icons...
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]
)
# Or for Font Awesome Icons...
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)



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
        id='sidebar',
        children=[
        html.I(className="bi bi-whatsapp"),   
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')]
            ),
            multiple=True
        ) ]
        
            
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

