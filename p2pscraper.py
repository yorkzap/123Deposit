from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper import calculate_inr_value, calculate_btc_amount

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
    
    return inr_value, float(sell_rate.replace(",", ""))

def main():
    buy_url = 'https://p2p.binance.com/en/trade/all-payments/BTC?fiat=CAD'
    driver = webdriver.Chrome()  # Change this to the appropriate WebDriver
    driver.get(buy_url)

    buy_rate_element = driver.find_element(By.CLASS_NAME, "css-onyc9z")
    buy_rate = buy_rate_element.get_attribute("textContent")

    inr_value, sell_rate_for_btcinr = calculate_inr_value(buy_rate)
    rate = inr_value / 1000
    print("P2P CAD BTC buy rate:", buy_rate)
    print("P2P CAD Sell rate: ", rate ,"INR")
    driver.quit()

    # Get user input for the amount in CAD
    depositAmount = int(input("Enter the amount in CAD: "))

    # Calculate the rate (INR value for user input amount)
    rate = inr_value / depositAmount

    # Calculate the remit amount
    remitAmount = depositAmount * rate
    print("Remit Amount:", remitAmount)

    # Calculate the equivalent BTC amount received with the deposit
    btc_received = remitAmount / sell_rate_for_btcinr
    print("Equivalent BTC Received:", btc_received)

    

if __name__ == "__main__":
    main()