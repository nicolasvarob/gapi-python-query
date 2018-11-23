from secret.private import VIEW_ID
from settings import config

print(config)

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': config['date_start'], 'endDate': config['date_end']}],
          'metrics': [{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:date'},{'name':'ga:browser'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [
                    {
                    "dimensionName": "ga:pagePath",
                    "expressions": ["^/portal/atencion-cliente/pagar-tus-cuotas$"]
                  },
                  {
                    "dimensionName": "ga:sourceMedium",
                    "not":"true",
                    "expressions": [".*newsletter.*emma"]
                  },
                  {
                    "dimensionName": "ga:hostname",
                    "not":"true",
                    "expressions": ["test.*|desa.*|.*google.*|localhost.*"]
                  }
                ]
              }
            ],
          "pageSize":"10000"
        }]
      }