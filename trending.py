import requests
def printtrend():
    response = requests.get("https://api.coingecko.com/api/v3/search/trending")
    data_dict = response.json()
    for x in range(7):
        print(data_dict['coins'][x]['item']['id'], "(" + data_dict['coins'][x]['item']['symbol'] + ")")
