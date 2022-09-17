import dash
from dash import Dash, html, dcc , dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

import base64
import datetime
import io


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
            html.H1('Group Chat Analyser', id='tit')
            # html.H6('A web application framework for your WhatsApp Group data.')
        ]
),
    html.Div(
        id='sidebar',
        children=[
            html.Img(src='/assets/wicon.png', id='wicon'),
        html.I(className="bi bi-whatsapp"),   
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')]
            ),
            multiple=True, 
        ), 
        html.Div('A web application framework for your WhatsApp Group data.', id='descr'),
        html.Div(id='output-data-upload')
        ]), 
  
    html.Div(
        id='rightbar',
        children=[
             dcc.Tabs(id='tabs', value='tab-1', children=[
                dcc.Tab(label='Analytics', value='tab-1', className='tab-1'),
                dcc.Tab(label='Data Preview', value='preview', className='tab-1')
             ]),
    html.Div(id='tabs-example-content-1')
    ]),
    
    html.Div(
        id='footer'
    ),
    
    # html.Div(id='output-data-upload'),
    
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            dbc.Alert(
                'There was an error processing this file.',
                color='danger'
            )
      ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])




# @app.callback(# Output('output-data-upload', 'children'),
#             Output('tabs-example-content-1', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))


@app.callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs', 'value'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
)

def update_output(tab, list_of_contents, list_of_names, list_of_dates):
    if tab == 'preview':
        if list_of_contents is not None:
            children = [
                parse_contents(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]
            return children
        else:
            dbc.Alert(
                'Upload A File',
                color='danger'
            )

# def render_content(tab):
#     if tab == 'preview':
#         return html.Div([
#             html.H3('Tab content 1'),
#             dcc.Graph(
#                 figure=dict(
#                     data=[dict(
#                         x=[1, 2, 3],
#                         y=[3, 1, 2],
#                         type='bar'
#                     )]
#                 )
#             )
#         ])
#     elif tab == 'tab-2':
#         return html.Div([
#             html.H3('Tab content 2'),
#             dcc.Graph(
#                 figure=dict(
#                     data=[dict(
#                         x=[1, 2, 3],
#                         y=[5, 10, 6],
#                         type='bar'
#                     )]
#                 )
#             )
#         ])






if __name__ == '__main__':
    app.run_server(debug=True)

