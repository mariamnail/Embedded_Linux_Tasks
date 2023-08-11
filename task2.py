import requests
rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(rate.json()['bpi']['USD']['rate'])  