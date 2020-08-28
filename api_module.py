#!/usr/bin/python3
import configparser
import requests
from requests import RequestException, ConnectionError, Timeout

config = configparser.ConfigParser()
config.read('config.ini')
index_api_url = f'{config["default"]["index_api_url"]}/api'


def tdt_id_by_lot_size(lot_size_):
    get_tdt_id_url = f"{index_api_url}/op/tdt_id?lot={lot_size_}&token=TBTC"
    try:
        req = requests.get(get_tdt_id_url)
        if req.status_code == 200 and req.text[0:2] == "0x" and len(req.text) == 42:
            print(req.text)
            return req.text

        else:
            print(req.text)
            return "Can't find a suitable TDT_ID for current lot size"

    except (RequestException, ConnectionError, Timeout, Exception) as connectErr:
        print(f'Error in tdt_id_by_lot_size():\n{connectErr}')
        return "error"



