import requests
# install it via pip:
# pip install requests
# pip install requests[security]
# info under : http://docs.python-requests.org/en/latest/
from token import *

r = requests.post("https://api.telegram.org/bot"+token+"/getUpdates")
# print r.status_code

print r.json()

r = requests.post("https://api.telegram.org/bot"+token+"/getMe")

print r.json()
