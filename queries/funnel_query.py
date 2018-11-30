from secret.private import VIEW_ID

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2018-09-01', 'endDate': '2018-11-12'}],
          'metrics': [{'expression': 'ga:users'},{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:pagePath'},{'name': 'ga:date'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [
                  {
                    "dimensionName": "ga:pagePath",
                    "expressions": [".*seguros-vehiculos/seguro-auto-flexible|(?i)/autoflexible/ventadirecta(/cotizacion.*|/oferta.*|.*(DatosBasicos|DatosBien|PlanPago|Emision|Contratado).*)"]
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