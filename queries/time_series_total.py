from secret.private import VIEW_ID

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2018-10-15', 'endDate': '2018-11-18'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:nthWeek'},{'name':'ga:browser'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [
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