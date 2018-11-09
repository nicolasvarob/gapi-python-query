from matplotlib import pyplot

import pandas as pd
import plotly
import plotly.graph_objs as go


def visualize(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df.reset_index()

    unique_pages = df['ga:pagePath'].unique().tolist()
    df_group = df.groupby( ["ga:date",'ga:pagePath'])['ga:uniquePageviews'].sum().reset_index()

    dimensions = []
    for item in unique_pages:
        df_trace = df_group[df_group['ga:pagePath'].str.contains(item)]
        t = go.Scatter(
            x=df_trace['ga:date'], 
            y=df_trace['ga:uniquePageviews'],
            name=item
        )
        dimensions.append(t)


    data = dimensions
    plotly.offline.plot(data, filename='analytics-time-series.html')
    
