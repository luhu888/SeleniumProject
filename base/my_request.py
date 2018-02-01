# -*- coding: utf-8 -*-
# __author__=luhu
import requests

url = "http://pointapi.dreamgotech.com/department/"

payload = {'name': '部门自定义', 'order': 3, 'departments': 1, 'users': [1, 2, 3]}
headers = {
    'authorization': "Token 7582b1089cb8fd605d03fe70bcd0ee7c2f7c6fb4",

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)



