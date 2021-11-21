import requests

def coinvalue(mycoin):
    response = requests.get("https://api.coingecko.com/api/v3/coins/" + mycoin)
    data_dict = response.json()
    print(data_dict['market_data']['current_price']['cad'])