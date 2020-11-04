import requests
import twitter
import json

class StockFeed:
	def __init__(self, feed):
		self.feed = feed
		self.main_dict={}

	def searchfinhub(self):
		print(self.feed)
		sup_dict={}
		r=requests.get('https://finnhub.io/api/v1/news?category=general&token=bufvijf48v6qf6lbs26g')
		y=r.json()
		for t in y:
			self.main_dict[str(t["id"])]={"id":t["id"],
			"category":t["category"],"datetime":t["datetime"],"image":t["image"],
			"summary":t["summary"],
			"url":t["url"],
			"headline":t["headline"]}
			# print(self.main_dict)
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)
	def searchfinhubstocknews(self,symbol):
		print(self.feed)
		sup_dict={}
		r = requests.get('https://finnhub.io/api/v1/company-news?symbol='+symbol+'&from=2020-04-30&to=2020-05-01&token=bufvijf48v6qf6lbs26g')
		y=r.json()
		for t in y:
			self.main_dict[str(t["id"])]={"id":t["id"],
			"category":t["category"],"datetime":t["datetime"],"image":t["image"],
			"summary":t["summary"],
			"url":t["url"],
			"headline":t["headline"]}
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)
	def searchtwitter(self,tags1):
		print(tags1,"tags1")
		main_dict=[]
		sup_dict={}
		api = twitter.Api(consumer_key="0U21owMEyc6Y3QskvqyTtb89i",
                  consumer_secret="PJNZBd0jbP61hPROazS02TzvtZxJjMeUBsycF0jUMVixLtF6lZ",
                  access_token_key="1321121639925362688-VRGp4FjSiN7RKthPETXeHrDVC1ocOC",
                  access_token_secret="ikI8InyZg7WRdoz5EGiPhd1Hp7dpDWmtPTkDDfOl9H8ds")
		print(api.tweet_mode)
		results = api.GetSearch(
		    raw_query="q="+tags1)
		y=results[0].AsDict()
		print(y)
		try:
			
			for x,t in enumerate(results):
				y=results[x].AsDict()
				try:
					if('media'in y) and (len(y["urls"])!=0):
						print(y['media'][0]['media_url'])
						print("media")
						if(y["lang"]=="en"):
							print("worked1",main_dict)
							self.main_dict[str(y["id"])]={"id":y["id"],
							"category":tags1,"datetime":y["created_at"],"image":y['media'][0]['media_url'],
							"summary":y["text"],
							"url":y["urls"][0]["expanded_url"],
							"headline":y["source"]}
							continue
							
					elif('media'in y):
						print(y['media'][0]['media_url'])
						if(y["lang"]=="en"):
							print("worked2",main_dict)
							self.main_dict[str(y["id"])]={"id":y["id"],
							"category":tags1,"datetime":y["created_at"],"image":y['media'][0]['media_url'],
							"summary":y["text"],
							"url":"null",
							"headline":y["source"]}
							continue
					elif(len(y["urls"])!=0):
						print(y["lang"],y["urls"])
						if(y["lang"]=="en"):
							print("worked3",main_dict)
							self.main_dict[str(y["id"])]={"id":y["id"],
							"category":tags1,"datetime":y["created_at"],"image":"null",
							"summary":y["text"],
							"url":y["urls"][0]["expanded_url"],
							"headline":y["source"]}
							continue
					else:
						print("none1")
				except:
					print("none")


		except:
			print("")
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)

			# print(t["category"],"1")
	def searchstockwits(self,sector):
		print(self.feed)
		headers = {
		'Content-Type': 'application/json'
		}
		token=requests.get("https://api.stocktwits.com/api/2/streams/trending.json?access_token=f77887ee6a4a7d3265be6054ce3b6686768a9467",headers)
		y=json.loads(token._content)
		# print(y['messages'])
		# sup_dict={}
		# r=requests.get('https://finnhub.io/api/v1/news?category=general&token=bufvijf48v6qf6lbs26g')
		# y=r.json()
		for t in y['messages']:
			# print(t)
			self.main_dict[str(t["id"])]={"id":t["id"],
			"category":sector,
			"datetime":t["created_at"],
			"image":"null",
			"summary":t["body"],
			"url":t['source']["url"],
			"headline":t['source']["title"]}
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)
	def searchtiingo(self,typeof,sector):
		# For the latest news
		if(typeof=="trending"):
			print(self.feed)
			headers = {
			'Content-Type': 'application/json'
			}
			token=requests.get("https://api.tiingo.com/tiingo/news?&token=75b0b300db1aff2a0addbb762e800f1f0ba78fab", headers=headers)
			y=token.json()
			for t in y:
				# print(t)
				self.main_dict[str(t["id"])]={"id":t["id"],
				"category":sector,
				"datetime":t["publishedDate"],
				"image":"null",
				"summary":t["description"],
				"url":t["url"],
				"headline":t["title"]}
			stock_feed_list=[]
			stock_feed_list.append(self.main_dict)	
			print(stock_feed_list)
		elif(typeof=="sector"):
			print(self.feed)
			headers = {
			'Content-Type': 'application/json'
			}
			token=requests.get("https://api.tiingo.com/tiingo/news?tags="+sector+"&token=75b0b300db1aff2a0addbb762e800f1f0ba78fab", headers=headers)
			y=token.json()
			for t in y:
				# print(t)
				self.main_dict[str(t["id"])]={"id":t["id"],
				"category":sector,
				"datetime":t["publishedDate"],
				"image":"null",
				"summary":t["description"],
				"url":t["url"],
				"headline":t["title"]}
			stock_feed_list=[]
			stock_feed_list.append(self.main_dict)	
			print(stock_feed_list)		
		elif(typeof=="tags"):
			print(self.feed)
			headers = {
			'Content-Type': 'application/json'
			}
			token=requests.get("https://api.tiingo.com/tiingo/news?tickers="+sector+"&token=75b0b300db1aff2a0addbb762e800f1f0ba78fab", headers=headers)
			y=token.json()
			for t in y:
				# print(t)
				self.main_dict[str(t["id"])]={"id":t["id"],
				"category":sector,
				"datetime":t["publishedDate"],
				"image":"null",
				"summary":t["description"],
				"url":t["url"],
				"headline":t["title"]}
			stock_feed_list=[]
			stock_feed_list.append(self.main_dict)	
			print(stock_feed_list)	
		# https://api.tiingo.com/tiingo/news

		# # For the latest news for specific tickers
		# https://api.tiingo.com/tiingo/news?tickers=aapl,googl

		# # For the latest news for specific tags/countries/topics/tc
		# https://api.tiingo.com/tiingo/news?tags=election,argentina
	


##there maybe many different feeds with same id because user follows it we have to get unique only when i will be making an object and putting
## it in user feed i have to make the feed unique with id
tags={'stocks':['AMZN','AAPL'],'sector':['trending','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}
feedlist=StockFeed(tags['sector'])
# feedlist.searchfinhubstocknews(tags['stocks'][0])
# feedlist.searchfinhub()
# feedlist.searchstockwits(tags['sector'][0])
feedlist.searchtiingo('tags',tags['stocks'][0])