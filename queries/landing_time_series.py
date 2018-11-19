from secret.private import VIEW_ID

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2018-09-01', 'endDate': '2018-11-12'}],
          'metrics': [{'expression': 'ga:users'},{'expression': 'ga:uniquePageviews'},{'expression':'ga:exitRate'}],
          'dimensions': [{'name': 'ga:pagePath'},{'name': 'ga:date'},{'name':'ga:sourceMedium'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [
                  {
                    "dimensionName": "ga:pagePath",
                    "expressions": ["^/portal/productos-persona(/seguros-vehiculos/(mercosur|seguroxkm|seguro-auto-flexible|seguro-obligatorio-soap)|/seguros-de-vida-y-accidentes/(enfermedades-protegidas|seguro-mi-mascota|asistencia-en-viaje))$"]
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