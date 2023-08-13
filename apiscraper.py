import requests
from scraper import get_usdt_to_btc_price


def get_usdt_to_btc_price():
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': 'BTCUSDT'}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'price' in data:
        return float(data['price'])
    else:
        return None

def main():
    usdt_to_btc_price = get_usdt_to_btc_price()
    
    if usdt_to_btc_price is not None:
        print(f"USDT to BTC price: {usdt_to_btc_price}")

        depositAmount = int(input("Enter the amount in USD: "))
        btcAmount = depositAmount / usdt_to_btc_price
        print(f"BTC Amount: {btcAmount}")
    else:
        print("Failed to retrieve price.")

if __name__ == "__main__":
    main()