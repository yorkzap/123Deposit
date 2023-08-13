import requests

def calculate_inr_value(buy_rate):
    # Calculate BTC for $1000
    btc_amount = 1000 / float(buy_rate.replace(",", ""))
    
    # Convert BTC to INR using the sell rate
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    sell_url = 'https://p2p.binance.com/en/trade/sell/BTC?fiat=INR&payment=all-payments'
    driver = webdriver.Chrome()  # Change this to the appropriate WebDriver
    driver.get(sell_url)
    
    sell_rate_element = driver.find_element(By.CLASS_NAME, "css-onyc9z")
    sell_rate = sell_rate_element.get_attribute("textContent")
    inr_value = btc_amount * float(sell_rate.replace(",", ""))
    
    driver.quit()
    
    return inr_value, float(sell_rate.replace(",", ""))

def calculate_btc_amount(depositAmount, sell_rate_for_btcinr):
    # Calculate equivalent BTC amount received with the deposit
    btc_received = depositAmount / sell_rate_for_btcinr
    return btc_received

def get_usdt_to_btc_price():
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': 'BTCUSDT'}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'price' in data:
        return float(data['price'])
    else:
        return None
