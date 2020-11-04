import stream

client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')

feed = client.feed('timeline', 'user-one')

# feed.add_activity({
#   "actor": client.users.create_reference('user-one'),
#   "verb": "post",
#   "object": "I love this picture",
#   "attachments": {
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
activities = feed.get(limit=10)["results"]
print(activities[0])