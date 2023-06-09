import requests
import time
from datetime import datetime

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

def main():
    while True:
        price = get_bitcoin_price()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Time:", current_time)
        print("Bitcoin Price (USD):", price)
        print()
        time.sleep(10)

if __name__ == "__main__":
    main()
