import stream
from stock_feed1 import StockFeed
client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
# tags=['google','apple','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']
# feedlist=CreatingFeed(tags[0])
# feedlist.searchfinhub()
tags={'stocks':{'Amazon':'AMZN','Apple':'AAPL'},
'sector':['industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}

# group of function contains only stocks
# feedlist=StockFeed()
#result1=feedlist.searchfinhubstocknews(tags['stocks']['Amazon'])
# # print(result1)
#result2=feedlist.searchtwitter(tags['stocks']['Amazon'])
# print(result2)
#result3=feedlist.searchtiingo('stocks',tags['stocks']['Amazon'])
# # print(result3)
# result4=feedlist.searchreddit(tags['stocks']['Amazon'])
# print(result4)


#group of function contains only sector
# feedlist=StockFeed()
# # result1=feedlist.searchtwitter(tags['sector'][1])
# # # print(result1)
# # result2=feedlist.searchtiingo('sector',tags['sector'][1])
# # # print(result2)
# result3=feedlist.searchreddit(tags['sector'][1])
# print(result3)



##group of latest trends and this user will be folowed by everyone




###in trending the must will be searchfinhub() function and searchstockwits() function
feedlist=StockFeed()
# feedlist.searchfinhub()
# print(result1)
# feedlist.searchtwitter("trending")
# print(result2)
# feedlist.searchtiingo('trending',"trending")
# print(result3)
# feedlist.searchreddit("trending")
# print(result4)
result5=feedlist.searchstockwits("trending")
# print(result5)
# print(next(iter(result5)))
# print(list(result5.keys()))
# print(next(iter(result5)))
# x=feedlist.searchfinhub()
# print(x)
feed = client.feed('constantuser', 'trending')

# feed.add_activity({
#   "actor": 'trending',
#   "verb": "post",
#   # "object": "I love this picture",
#   "object": result5
# })
# # activites=client.collection.get("food", "cheese-burger")


##removing the feed from the user
activities = feed.get()
print(activities['results'])

# for x in activities['results']:
# 	print(x['id'])
# 	feed.remove_activity(x['id'])
	# client.users.delete(x['id'])

##Add trendingdict to the trending user
# for key, value in result5.items():
# 	# print(key, '->', value)
# 	feed.add_activity({
# 	  "actor": 'trending',
# 	  "verb": "post",
# 	  # "object": "I love this picture",
# 	  "object": value
# 	})



# for no,li in enumerate(activities):
#   print(activities['results'][no]['id'])
#   temp_id=activities['results'][no]['id']
#   client.users.delete(temp_id)
#gather the id of all activites and delete iteratively till limit of list


def adding_the_feed_trending():
	feedlist=StockFeed()
	feedlist.searchfinhub()
	feedlist.searchtwitter("trending")
	feedlist.searchtiingo('trending',"trending")
	feedlist.searchreddit("trending")
	result5=feedlist.searchstockwits("trending")
	print(result5)
	# client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
	# feed = client.feed('constantuser', 'trending')
	# for key, value in result5.items():
	# 	feed.add_activity({
	# 	  "actor": 'trending',
	# 	  "verb": "post",
	# 	  "object": value
	# 	})

def delete_the_feed_trending():
	client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
	feed = client.feed('constantuser', 'trending')
	activities = feed.get()
	# print(activities['results'])
	for x in activities['results']:
		feed.remove_activity(x['id'])

def adding_the_feed_stocks(key,value):
	feedlist=StockFeed()
	feedlist.searchfinhubstocknews(value)
	feedlist.searchtwitter(value)
	feedlist.searchtiingo('stocks',value)
	result4=feedlist.searchreddit(value)
	print(result4)

def adding_stocks_list():
	adding_the_feed_trending()
	stocks={'Amazon':'AMZN','Apple':'AAPL'}
	for key, value in stocks.items():
		adding_the_feed_stocks(key,value)


adding_stocks_list()