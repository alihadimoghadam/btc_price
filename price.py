import requests
from bs4 import BeautifulSoup
import time

def search_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element that contains the BTC price
        btc_price_element = soup.find(class_="price_btc")

        # Extract the BTC price
        btc_price = btc_price_element.text.strip()

        # Print the BTC price
        print(f"BTC Price: {btc_price}")
    else:
        print("Failed to retrieve website content.")

# Example usage
url = 'https://coin360.com/'
interval = 3600  # Interval in seconds (1 hour = 3600 seconds)

while True:
    search_website(url)
    time.sleep(interval)
