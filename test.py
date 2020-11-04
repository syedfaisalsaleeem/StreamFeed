import stream
from stock_feed1 import StockFeed
client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
# tags=['google','apple','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']
# feedlist=CreatingFeed(tags[0])
# feedlist.searchfinhub()
tags={'stocks':{'Amazon':'AMZN','Apple':'AAPL'},
'sector':['trending','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}

# group of function contains only stocks
feedlist=StockFeed()
result1=feedlist.searchfinhubstocknews(tags['stocks']['Amazon'])
#print(result1)
result2=feedlist.searchtwitter(tags['stocks']['Amazon'])
# print(result2)
result3=feedlist.searchtwitter(tags['stocks']['Amazon'])
print(result3)







###in trending the must will be searchfinhub() function and searchstockwits() function

# x=feedlist.searchfinhub()
# print(x)
# feed = client.feed('constantuser', 'google')

# feed.add_activity({
#   "actor": 'google',
#   "verb": "post",
#   # "object": "I love this picture",
#   "object": {
#       "og": {
#           "title": "Crozzon di Brenta photo by Lorenzo Spoleti",
#           "description": "Download this photo in Italy by Lorenzo Spoleti",
#           "url": "https://unsplash.com/photos/yxKHOTkAins",
#           "images": [
#             {
#               "image": "https://goo.gl/7dePYs"
#             }
#           ]
#       }
#   }
# })
# # activites=client.collection.get("food", "cheese-burger")
# activities = feed.get()

# for no,li in enumerate(activities):
#   print(activities['results'][no]['id'])
# #gather the id of all activites and delete iteratively till limit of list