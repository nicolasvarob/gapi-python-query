import pandas as pd

def analyse(df):

    unique_values_to_rename = df['ga:pagePath'].unique().tolist()    
    for item in unique_values_to_rename:
        split = item.split('/')
        df['ga:pagePath'] = df['ga:pagePath'].replace(item,split[-1])
    
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df['month'] = df['ga:date'].dt.month
    df_cl = df.drop(columns=['ga:browser'])
    df_gp = df_cl.groupby(['ga:pagePath','month'])['ga:uniquePageviews'].sum().reset_index()
    df_gp['sample req'] = 2000 / df_gp['ga:uniquePageviews']
    print(df_gp[df_gp['month'] == 10])
    result = df_gp.groupby(['ga:pagePath'])['ga:uniquePageviews'].mean().round(2).reset_index()
