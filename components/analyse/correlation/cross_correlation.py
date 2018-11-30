import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from components.analyse.correlation.external_data_prep import external_data



# Cross Correlation between two time series

def analyse(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df_cl = df.groupby(['ga:date'])['ga:uniquePageviews'].sum().reset_index()
    df_cl['unique pageviews norm'] = (df['ga:uniquePageviews']-df['ga:uniquePageviews'].min())/(df['ga:uniquePageviews'].max()-df['ga:uniquePageviews'].min())
    
    df_sales = external_data.groupby(['Fecha de Venta'])['Total Ventas'].sum().reset_index()

    df_sales['sales norm'] =  (df_sales['Total Ventas']-df_sales['Total Ventas'].min())/(df_sales['Total Ventas'].max()-df_sales['Total Ventas'].min())
    

    df_web_cl = df_cl.drop(['ga:uniquePageviews'],axis=1).rename(columns={'ga:date': 'date'})
    df_web_cl['rolling pv'] = df_web_cl['unique pageviews norm'].rolling(14).mean()
    df_sales_cl = df_sales.drop(['Total Ventas'],axis=1).rename(columns={'Fecha de Venta': 'date'})
    df_sales_cl['rolling sales'] = df_sales_cl['sales norm'].rolling(14).mean()
    df_sales_cl = df_sales_cl[df_sales_cl['date'] >= '2018-05-25']

    df_consolidate = pd.merge(df_web_cl,df_sales_cl,how='inner',on='date')
    df_consolidate.plot(x='date',y=['unique pageviews norm','sales norm'])
    print(df_consolidate.corr())
    plt.show()



