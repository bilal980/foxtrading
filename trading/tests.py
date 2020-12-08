import requests
import json

new = requests.get('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-7?apiKey=wyH5CtMCMqfAvDO45asBYfYnOWwMlQCC')
data=new.json()

