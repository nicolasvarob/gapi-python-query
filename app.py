import numpy as np

from components.initialize_analytics import initialize_analyticsreporting
from components.to_df import response_to_df

from secret.private import CLIENT_SECRET_PATH
from queries.landing_time_series import request_body
from components.analyse.anomaly_detection import visualize

# Get report from Analytics
def get_report(analytics):
  # Use the Analytics Service Object to query the Analytics Reporting API V4.
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
  ## Visualise Dataframe (Not standarized)
  visualize(df)

if __name__ == '__main__':
  main()

