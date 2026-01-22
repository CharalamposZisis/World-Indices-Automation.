import requests

API_KEY = "f452GbQOp8NwPwaJ2hXcSJfBPy32QbrjkwCiriLB"
BASE_URL = "https://api.stockdata.org/v1/data/quote"

stocks = ["AAPL", "MSFT", "GOOGL", "TSLA"] # Because of the limitation of the StockData page we can get only 3 stocks data for free.

def fetch_data(symbols):
    symbols_str = ",".join(symbols)

    params = {
        "symbols": symbols_str,
        "api_token": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data.get("data", [])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return []

stock_data = fetch_data(stocks)

# for stock in stock_data:
#     print(f"Symbol: {stock['ticker']}")
#     print(f"Price: {stock['price']}")
#     print(f"Volume: {stock['volume']}")
#     print(f"Day High: {stock['day_high']}")
#     print(f"Day Low: {stock['day_low']}")
#     print("-" * 40)