import requests

params = {
    'collection': 'crypto-bull-society'
}

r = requests.get("https://api.opensea.io/api/v1/bundles")

print (r.json())
