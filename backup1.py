import requests

response = requests.get("https://ipqualityscore.com/api/json/ip/BEOThHbIDo34q9lycrGuA7oJMvPTesya/194.166.52.20?strictness=2&allow_public_access_points=true&mobil=false&fast=false&lighter_penalties=false")
data = response.json()
fraud = data['fraud_score']

print(fraud)