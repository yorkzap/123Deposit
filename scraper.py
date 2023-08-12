from selenium import webdriver
from selenium.webdriver.common.by import By

def calculate_inr_value(buy_rate):
    # Calculate BTC for $1000
    btc_amount = 1000 / float(buy_rate.replace(",", ""))
    
    # Convert BTC to INR using the sell rate
    sell_url = 'https://p2p.binance.com/en/trade/sell/BTC?fiat=INR&payment=all-payments'
    driver = webdriver.Chrome()  # Change this to the appropriate WebDriver
    driver.get(sell_url)
    
    sell_rate_element = driver.find_element(By.CLASS_NAME, "css-onyc9z")
    sell_rate = sell_rate_element.get_attribute("textContent")
    inr_value = btc_amount * float(sell_rate.replace(",", ""))
    
    driver.quit()
    
    return inr_value

buy_url = 'https://p2p.binance.com/en/trade/all-payments/BTC?fiat=CAD'
driver = webdriver.Chrome()  # Change this to the appropriate WebDriver
driver.get(buy_url)

buy_rate_element = driver.find_element(By.CLASS_NAME, "css-onyc9z")
buy_rate = buy_rate_element.get_attribute("textContent")

inr_value = calculate_inr_value(buy_rate)
rate = inr_value/1000
print("By sending $1000, you will receive ", inr_value, "INR", "Rate: ", rate)

driver.quit()
