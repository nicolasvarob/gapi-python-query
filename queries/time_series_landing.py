from secret.private import VIEW_ID
from settings import config

print(config)

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': config['date_start'], 'endDate': config['date_end']}],
          'metrics': [{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:nthWeek'},{'name':'ga:browser'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [
                    {
                    "dimensionName": "ga:pagePath",
                    "expressions": [".*/portal/productos-persona(/seguros-vehiculos/(mercosur|seguroxkm|seguro-auto-flexible|seguro-obligatorio-soap)|/seguros-de-vida-y-accidentes/(enfermedades-protegidas|seguro-mi-mascota|asistencia-en-viaje))$"]
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