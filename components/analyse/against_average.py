def analyse(df):
    df_clean = df[df['ga:nthWeek'] != '0005']
    df_group = df_clean.groupby(['ga:nthWeek'])['ga:uniquePageviews'].sum().reset_index()
    n_week_before = df_group.loc[df_group['ga:nthWeek'] != '0004']
    n_week_point = df_group.loc[df_group['ga:nthWeek'] == '0004']



    mean = n_week_before['ga:uniquePageviews'].mean()
    point_mean = n_week_point['ga:uniquePageviews'].mean()

    print((point_mean - mean)/mean)
