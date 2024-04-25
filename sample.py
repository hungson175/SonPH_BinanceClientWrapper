import datetime
from binance.client import Client
from binance.enums import *
import json

import utils
from binance_futures_client import BinanceFuturesClient

# API_KEY = 'IpKHNugKGPPM1Yv8AfgtMnsaZCtX9vGo6LdJ7RnHDhQHFK3dO1M9Eboolt6nPLRv'
# API_SECRET = 'DhV01PZFBlLbsDIeI7XMNq3n10HoxSaPQjm5pxUJXjWBRWHYNEP7usZn7TftZRz3'
# BASE_URL_TESTNET = "https://testnet.binance.vision/api"

FUTURE_API_KEY = "4fadcd74e67a6ae63dff5566402c28d9e408bb9a460fd687fd39b976af499fed"
FUTURE_API_SECRET = "b9fe1e235e4dfe4788e906f364430888322e34a4ebe3771751199abe72a88c33"
BASE_URL_TESTNET_FUTURE = "https://testnet.binancefuture.com"




if __name__ == '__main__':
    client = BinanceFuturesClient(FUTURE_API_KEY, FUTURE_API_SECRET, testing=True)
    # print(client.get_server_time())
    # utils.beautify_json(client.get_open_positions())
    # utils.beautify_json(client.get_available_assets())
    print(client.get_unrealized_pnl())
    account = client.get_account_info()
    utils.print_dict_schema(account)
    leverage = client.get_leverage('BTCUSDT')
    print(leverage," - ", type(leverage))



    # utils.beautify_json(client.get_account_info()['positions'])

    # params = {
    #     'symbol': 'BTCUSDT',
    #     'side': 'BUY',
    #     'order_type': 'MARKET',
    #     'quantity': 0.1,
    #     'position_side': 'LONG'
    # }
    # response = client.place_order(**params)
    # utils.beautify_json(response)

    # response = client.close_all_positions()
    # utils.beautify_json(response)
