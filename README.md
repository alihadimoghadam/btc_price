# Bitcoin Price Monitor
This Python script fetches the current price of Bitcoin (BTC) in USD using the CoinGecko API and displays it along with the timestamp. The script updates the price every 10 seconds.

# Prerequisites
Python 3.x
requests library (install using pip install requests)
Usage
Clone the repository or download the bitcoin_price_monitor.py file.
Install the required requests library if not already installed: pip install requests.
Run the script: python bitcoin_price_monitor.py.
The script will continuously display the current Bitcoin price and the corresponding timestamp every 10 seconds.

# API Key (Optional)
The script does not require an API key as it uses the CoinGecko API, which is free and open. However, if you encounter any issues with the API or want to use a different cryptocurrency data source, you may need to obtain an API key and modify the code accordingly.

# Note
Continuous polling of an API every 10 seconds can be resource-intensive and may violate the API provider's usage limits or terms of service. Make sure to check the API documentation for any rate limits or restrictions before using this code in a production environment.

# License
MIT License

Feel free to customize the README file according to your specific project requirements and any additional information you would like to provide to users.
