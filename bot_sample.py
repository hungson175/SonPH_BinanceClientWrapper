import numpy as np
from binance.um_futures import UMFutures

from binance_futures_client import BinanceFuturesClient


class TradingBot:
    def __init__(self, client):
        self.client = client

    def fetch_prices(self, symbol, interval, limit):
        """Fetch historical prices for a given symbol and interval."""
        bars = self.client.klines(symbol=symbol, interval=interval, limit=limit)
        prices = [float(bar[4]) for bar in bars]  # Closing price index is 4
        return prices

    def calculate_ma(self, prices, period):
        """Calculate moving average."""
        return np.mean(prices[-period:])

    def execute_strategy(self, symbol, interval='4h', period=50, quantity=0.01):
        """Execute the trading strategy based on moving average."""
        prices = self.fetch_prices(symbol, interval, 300)
        current_price = prices[-1]
        ma50 = self.calculate_ma(prices, period)

        print(f"Current Price: {current_price}, MA50: {ma50}")

        if current_price > ma50:
            print("Current price is above MA50, placing buy order.")
            params = {
                'symbol': symbol,
                'side': 'BUY',
                'order_type': 'MARKET',
                'quantity': quantity,
                'position_side': 'LONG'
            }
            self.client.place_order(**params)
        elif current_price < ma50:
            print("Current price is below MA50, placing sell order.")
            params = {
                'symbol': symbol,
                'side': 'SELL',
                'order_type': 'MARKET',
                'quantity': quantity,
                'position_side': 'SHORT'
            }
            self.client.place_order(**params)
        else:
            print("Current price is below MA50, no action taken.")


# Example usage:
client = BinanceFuturesClient(
    BinanceFuturesClient.FUTURE_API_KEY,
    BinanceFuturesClient.FUTURE_API_SECRET,
    testing=True)
bot = TradingBot(client)
# Run the strategy for BTCUSDT
bot.execute_strategy('BTCUSDT')
