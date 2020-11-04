import requests
import twitter
import json
class Error(Exception):
    """Base class for other exceptions"""
    pass
class UrlError(Error):
    """Raised when the url is empty"""
    pass
class ImageError(Error):
    """Raised when the url is empty"""
    pass
class StockFeed:
	def __init__(self, feed):
		self.feed = feed
		self.main_dict={}

	def searchfinhub(self):
		print(self.feed)
		# list_company=[]
		# if(self.feed in list_company):
		#we can get company news but it's going to be different
		sup_dict={}
		# main_dict=[]
		r=requests.get('https://finnhub.io/api/v1/news?category=general&token=bufvijf48v6qf6lbs26g')
		# print(r.json())
		y=r.json()
		# print(y[0])
		for t in y:
			# print(t['datetime'])
			# sup_dict.clear()
			# sup_dict["category"]=t["category"]
			# sup_dict["datetime"]=t["datetime"]
			# sup_dict["headline"]=t["headline"]
			# sup_dict["id"]=t["id"]
			# sup_dict["image"]=t["image"]
			# sup_dict["summary"]=t["summary"]
			# sup_dict["url"]=t["url"]
			# print(sup_dict["id"])
			self.main_dict[str(t["id"])]={"id":t["id"],
			"category":t["category"],"datetime":t["datetime"],"image":t["image"],
			"summary":t["summary"],
			"url":t["url"],
			"headline":t["headline"]}
			# print(self.main_dict)
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
		# print(api.VerifyCredentials())
		#print(api.GetStatus(1321819438019186689))
		results = api.GetSearch(
		    raw_query="q="+tags1)
		# print(len(results))
		# print(results[0]["lang"])
		# print(results[0].id)
		# print(results[0].AsDict())
		y=results[0].AsDict()
		print(y)
		# print(y["lang"])
		# if(y["lang"]=="en"):
		# 	# print(y)
		try:
			
			for x,t in enumerate(results):
			# for x in range(0,10):
				# print(y["lang"],y["urls"])
				y=results[x].AsDict()
				# print(y["lang"],y["urls"])
				try:
					# print("")
					# print(y["text"],y["created_at"],y["lang"],y["source"],y["id"])	
					# print(results[x]["media"])
					
					
					if('media'in y) and (len(y["urls"])!=0):
						print(y['media'][0]['media_url'])
						print("media")
					# 	# print(y['media'][0]['media_url'],y["urls"][0]["expanded_url"])
					# 	# raise NameError 
						if(y["lang"]=="en"):
							
							# sup_dict["category"]=tags1
							# sup_dict["datetime"]=y["created_at"]
							# sup_dict["headline"]=y["source"]
							# sup_dict["id"]=y["id"]
							# sup_dict["image"]=y['media'][0]['media_url']
							# sup_dict["summary"]=y["text"]
							
							# sup_dict["url"]=y["urls"][0]["expanded_url"]
							# main_dict.append(sup_dict)
							print("worked1",main_dict)
							self.main_dict[str(y["id"])]={"id":y["id"],
							"category":tags1,"datetime":y["created_at"],"image":y['media'][0]['media_url'],
							"summary":y["text"],
							"url":y["urls"][0]["expanded_url"],
							"headline":y["source"]}
							# print(self.main_dict)
							continue
						# stock_feed_list=[]
						# stock_feed_list.append(self.main_dict)	
						# print(stock_feed_list)
							
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
						# print(self.main_dict)
											
						# for t1,t2 in enumerate(y):
						# 	print(y)
				except:
					print("none")


		except:
			print("")
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)

			# print(t["category"],"1")
	
tags={'stocks':['AMZN','AAPL'],'sector':['industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}
feedlist=StockFeed(tags['sector'])
feedlist.searchtwitter(tags['sector'][2])
# feedlist.searchfinhub()