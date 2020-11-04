import stream
from creating_feed import CreatingFeed
client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
tags=['google','apple','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']
feedlist=CreatingFeed(tags[0])
feedlist.justprint()
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
# activities = feed.get(limit=10)["results"]
# print(activities)
#gather the id of all activites and delete iteratively till limit of list