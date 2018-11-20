from settings import config
import re

import re
pattern = re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2}|today|yesterday|[0-9]+(daysAgo))$")

## Verify inputs to check if ok
def inputParse(conf):
    date_start = False
    date_end = False
    error = False

    if 'date_start' in config:
        date_start = conf['date_start']
        if not pattern.match(date_start):
            error = True  

    if 'date_end' in config:
        date_end = conf['date_end']
        if not pattern.match(date_end):
            error = True     

    if date_end and date_start:
        print('todo ok')
        return
    if not date_end and not date_start:
        print('auto set dates')
        return
    else:
        print('date errors')
        error = True
inputParse(config)
