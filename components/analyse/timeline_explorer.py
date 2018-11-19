import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from datetime import datetime as dt

def visualize(df):
    ## To date
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df.reset_index()
    unique_values_to_rename = df['ga:pagePath'].unique().tolist()    
    
    for item in unique_values_to_rename:
        split = item.split('/')
        df['ga:pagePath'] = df['ga:pagePath'].replace(item,split[-1])

    unique_pages = df['ga:pagePath'].unique().tolist()    
    df_pages = df.groupby( ['ga:date','ga:pagePath'])['ga:uniquePageviews'].sum().reset_index()
    df_src = df.groupby( ['ga:date','ga:pagePath','ga:sourceMedium'])['ga:uniquePageviews'].sum().reset_index()
    # Initialize Dash
    app = dash.Dash('Hello World')

    options = []
    for item in unique_pages:
        options.append({'label':item,'value':item})

    app.layout = html.Div([
        dcc.Dropdown(
            id='my-dropdown',
            options= options,
            value='mercosur'
        ),
        dcc.Graph(id='my-graph')
    ], style={'width': '100%'})

    @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):

        df_select = df_pages.loc[df_pages['ga:pagePath'] == selected_dropdown_value]

        return {
            'data': [{
                'x': df_select['ga:date'],
                'y': df_select['ga:uniquePageviews'],
            }],
            'layout': {'margin': {'l': 40, 'r': 40, 't': 20, 'b': 30}}
        }

    app.run_server(debug=True)

    