import requests
import config

def fetch_bitcoin_price():
    """
    Fetches the current price of Bitcoin (BTC) in USD from the CoinMarketCap API.

    Returns:
        float: The current price of Bitcoin in USD.
    """
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': 'BTC',  # Symbol for Bitcoin
        'convert': 'USD'  # Convert to USD
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.cmc_key  # API key from the config file
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        btc_price = data['data']['BTC']['quote']['USD']['price']
        return btc_price
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None
