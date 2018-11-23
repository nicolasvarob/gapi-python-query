import numpy as np

from secret.private import CLIENT_SECRET_PATH
from config.initialize_analytics import initialize_analyticsreporting
from components.to_df import response_to_df

'from components.analyse.timeline_explorer import visualize'
from queries.time_series_landing import request_body
from components.analyse.timeseries_analysis import analyse as analysis

# INPUT
## Query report from Analytics
def get_report(analytics):
  ## Use the Analytics Service Object to query the Analytics Reporting API V4.
  return analytics.reports().batchGet(
      body=request_body
  ).execute()

def main():

  ## Initialize
  analytics = initialize_analyticsreporting()
  ## Get response
  response = get_report(analytics)
  ## Convert response to dataframe
  df = response_to_df(response)
  ## OUTPUTVisualise Dataframe ()
  analysis(df)

if __name__ == '__main__':
  main()

