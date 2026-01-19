import requests
api_key = '3HWC08RABPOP8UTE'
api_url = "https://www.alphavantage.co/query"
stocks = ["AAPL", "MSFT", "GOOGL", "IBM"]

def fetch_data(symbol, function="TIME_SERIES_DAILY"):
    print(f"Fetching data for {symbol} from Alpha Vantage")

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        print("API response received successfully")
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise

for stock in stocks:
    data = fetch_data(stock)
# def mock_fetch_data():
    