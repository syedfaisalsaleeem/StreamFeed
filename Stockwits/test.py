import requests
import pprint
import json
#curl -X GET https://api.stocktwits.com/api/2/oauth/authorize -d 'client_id=<client id>&response_type=code&redirect_uri=http://www.example.com&scope=read,watch_lists,publish_messages,publish_watch_lists,follow_users,follow_stocks'
# token=requests.get("https://api.stocktwits.com/api/2/oauth/authorize?&client_id=ebe35f36fac1c498&response_type=code&redirect_uri=https://servat.life/&scope=read,watch_lists,publish_messages,publish_watch_lists,follow_users,follow_stocks")
# print(token)
# pprint.pprint(vars(token))
headers = {
    'Content-Type': 'application/json'
}
token=requests.get("https://api.stocktwits.com/api/2/streams/trending.json?access_token=f77887ee6a4a7d3265be6054ce3b6686768a9467",headers)
# y=json.loads(token._content)
# print(y['messages'][0])
# pprint.pprint(vars(token._content))
# curl -X GET https://api.stocktwits.com/api/2/search.json?access_token=<access_token> 'q=stocktwits'
# headers = {
#     'Content-Type': 'application/json'
# }
# token=requests.get("https://api.stocktwits.com/api/2/search.json?access_token=f77887ee6a4a7d3265be6054ce3b6686768a9467&q=python",headers)
# pprint.pprint(vars(token))
y=json.loads(token._content)
print(y['messages'][0])