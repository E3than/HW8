import requests


def print100():
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=100&page=1"
        "&sparkline=false")
    data_dict = response.json()
    print(" ")
    print("The price for the top 100 coins are: ")
    print(" ")
    for x in range(100):
        print(data_dict[x]['id'], data_dict[x]['current_price'])
