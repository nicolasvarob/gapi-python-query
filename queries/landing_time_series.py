from secret.private import VIEW_ID

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2018-08-07', 'endDate': '2018-11-07'}],
          'metrics': [{'expression': 'ga:users'},{'expression': 'ga:uniquePageviews'},{'expression':'ga:exitRate'}],
          'dimensions': [{'name': 'ga:pagePath'},{'name': 'ga:date'}],
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
                    "expressions": ["test.*|desa.*|.*google.*"]
                  }
                ]
              }
            ]
        }]
      }