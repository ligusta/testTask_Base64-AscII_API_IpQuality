import requests
import json

ip = '98.6.97.26'

url = ('https://ipqualityscore.com/api/json/ip')
params = {
    'key': 'BEOThHbIDo34q9lycrGuA7oJMvPTesya',
    'ip': ip,
    'strictness': 2,
    'allow_public_access_points': 'true',
    'mobil': 'false',
    'fast': 'false',
    'lighter_penalties': 'false'

}

response = requests.get(url, params)
data = response.json()
fraud = data['fraud_score']

print(fraud)
