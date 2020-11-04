# import requests
# r = requests.get('https://api.tiingo.com/tiingo/news?tags=election&token=3d4f22f6231c5c94f24b9babba78e0f3ad77db12')
# print(r.json())
# import requests
# headers = {
#     'Content-Type': 'application/json'
# }
# requestResponse = requests.get("https://api.tiingo.com/tiingo/news?token=3d4f22f6231c5c94f24b9babba78e0f3ad77db12", headers=headers)
# print(requestResponse.json())
# import requests

# headers = {
#         'Content-Type': 'application/json'
#         }
# requestResponse = requests.get("https://api.tiingo.com/api/test?token=3d4f22f6231c5c94f24b9babba78e0f3ad77db12",
#                                     headers=headers)
# print(requestResponse.json())
import requests
headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/news?tags=technology&token=75b0b300db1aff2a0addbb762e800f1f0ba78fab", headers=headers)
print(requestResponse.json())