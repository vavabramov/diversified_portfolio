import pandas as pd
import requests
import functools
from datetime import datetime

def check_status(response)->bool:
    return response.status_code == 200

def get_listings(url:str, headers:dict, sortedby:str='market_cap', limit:int=100)->pd.DataFrame:

    result=None

    url = url.replace('__sortedby__', sortedby).replace('__limit__', str(limit))
    response = requests.get(url, headers=headers)

    if check_status(response):
        _json = response.json()

        if 'data' in  _json.keys():
            result = pd.DataFrame.from_records(response.json()['data'])
        else:
            result = pd.DataFrame.from_records(response.json())

    return result

def get_historic_prices(url:str, ticker:str, start_date:str, end_date:str)->pd.DataFrame:

    result=None

    repls = ('__ticker__', ticker), ('__start_date__', start_date), ('__end_date__', end_date)
    url = functools.reduce(lambda a, kv: a.replace(*kv), repls, url)
    response = requests.get(url)

    if check_status(response):
        _json = response.json()
        result = pd.DataFrame(_json, columns = ['date', 'low', 'high', 'open', 'close', 'volume'])
        result['date'] = pd.to_datetime(result['date'], unit='s')
        result['symbol'] = ticker

    return result

