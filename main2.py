import requests
import json
r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2CEthereum%2CTether&vs_currencies=usd')

#print(r.text)

a = json.loads(r.text)

print(round(a['tether']['usd']))