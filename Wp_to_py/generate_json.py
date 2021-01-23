
# import urllib, json
import requests

for u in range(62,78):
    # print (u)
    s = requests.get("https://foloker.com/wp-json/wp/v2/categories/%s"%u)
    data = s.json()
    print("id :",data['id'])
    print("description :",data['description'])