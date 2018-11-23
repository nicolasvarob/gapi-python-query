import pandas as pd
import numpy as np

import seaborn as sns
from scipy import stats

import matplotlib.pyplot as plt

def analyse(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df['day'] = df['ga:date'].dt.day
    df.reset_index()

    df['Week_Number'] = df['ga:date'].dt.week

    df = df[df['day'] < 21]

    df_gp = df.groupby(['ga:date'])['ga:uniquePageviews'].sum().reset_index()

    ## general analysis

    df_range_before = df_gp[(df_gp['ga:date'] >= '2018-06-01') & (df_gp['ga:date'] <= '2018-10-31')].reset_index()
    df_range_selected = df_gp[(df_gp['ga:date'] >= '2018-11-01') & (df_gp['ga:date'] <= '2018-11-20')].reset_index()
    df_range_before['time'] = 'before'
    df_range_selected['time'] = 'selected'


    df_range_before_std = df_range_before['ga:uniquePageviews'].std()
    df_range_selected_std = df_range_selected['ga:uniquePageviews'].std()



    ## single browser analysis
    single_browser = df.loc[df['ga:browser'] == 'Chrome']
    single_browser_before = single_browser[(single_browser['ga:date'] >= '2018-06-01') & (single_browser['ga:date'] <= '2018-10-31')].reset_index()
    single_browser_selected = single_browser[(single_browser['ga:date'] >= '2018-11-01') & (single_browser['ga:date'] <= '2018-11-20')].reset_index()

    single_browser_before['tiempo'] = 'semanas anteriores'
    single_browser_selected['tiempo'] = 'actual'

    result = pd.concat([single_browser_before,single_browser_selected]).reset_index()

    single_browser_before_std = single_browser_before['ga:uniquePageviews'].var()
    single_browser_selected_std = single_browser_selected['ga:uniquePageviews'].var()

    print(single_browser_before['ga:uniquePageviews'].mean())
    print(single_browser_selected['ga:uniquePageviews'].mean())

    ax = sns.boxplot(x=result['tiempo'],y=result['ga:uniquePageviews'],data=result)
    ax.set(ylabel='Visitas únicas')
    plt.show()

def monthly_analysis(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df['month'] = df['ga:date'].dt.week
    df['day'] = df['ga:date'].dt.day

    df_cl = df[(df['day'] < 21)].groupby(['month'])['ga:uniquePageviews'].sum().reset_index()

def daily_analysis(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    df['month'] = df['ga:date'].dt.month
    df['day'] = df['ga:date'].dt.week

    plt.show()



    df_cl = df[df['month']].groupby(['ga:date','month','day'])['ga:uniquePageviews'].sum().reset_index()
    df_m = df_cl.groupby(['month'])['ga:uniquePageviews'].sum().reset_index()
    df_m = df_m.rename(columns={'ga:uniquePageviews': 'monthly_upv'})

    df_mpv = pd.merge(df_cl,df_m,how='inner',on='month')
    df_mpv['pcts'] = df_mpv['ga:uniquePageviews']/df_mpv['monthly_upv']

    df_day = df_mpv.groupby(['day'])['pcts'].mean().reset_index()

    print(df_day[(df_day['day'] >= 28) | (df_day['day'] <= 5 )]['pcts'].sum())