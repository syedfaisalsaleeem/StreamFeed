import requests
import twitter

class CreatingFeed:
	def __init__(self, feed):
		self.feed = feed
		self.main_dict=[]

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
			sup_dict["category"]=t["category"]
			sup_dict["datetime"]=t["datetime"]
			sup_dict["headline"]=t["headline"]
			sup_dict["id"]=t["id"]
			sup_dict["image"]=t["image"]
			sup_dict["summary"]=t["summary"]
			sup_dict["url"]=t["url"]
			self.main_dict.append(sup_dict)
		print(main_dict)
	def searchtwitter(self):
		api = twitter.Api(consumer_key="0U21owMEyc6Y3QskvqyTtb89i",
                  consumer_secret="PJNZBd0jbP61hPROazS02TzvtZxJjMeUBsycF0jUMVixLtF6lZ",
                  access_token_key="1321121639925362688-VRGp4FjSiN7RKthPETXeHrDVC1ocOC",
                  access_token_secret="ikI8InyZg7WRdoz5EGiPhd1Hp7dpDWmtPTkDDfOl9H8ds")
		print(api.tweet_mode)
		# print(api.VerifyCredentials())
		#print(api.GetStatus(1321819438019186689))
		results = api.GetSearch(
		    raw_query="q=AMZN")
		# print(results[0]["lang"])
		# print(results[0].id)
		# print(results[0].AsDict())
		y=results[0].AsDict()
		print(y["lang"])
		if(y["lang"]=="en"):
			print(y)
		try:
			sup_dict={}
			for x,t in enumerate(results):
				try:
					# print(results[x]["media"])
					y=results[x].AsDict()

					print(y['media'][0]['media_url'])
					if(y["lang"=="en"]):
						sup_dict["category"]=t["category"]
						sup_dict["datetime"]=t["datetime"]
						sup_dict["headline"]=t["headline"]
						sup_dict["id"]=t["id"]
						sup_dict["image"]=t["image"]
						sup_dict["summary"]=t["summary"]
						sup_dict["url"]=t["url"]
						self.main_dict.append(sup_dict)
					print(self.main_dict)					
					# for t1,t2 in enumerate(y):
					# 	print(y)
				except:
					print("none")
		except:
			print("")

			# print(t["category"],"1")
	
tags={'stocks':['AMZN','AAPL'],'sector':['industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}
feedlist=CreatingFeed(tags)
feedlist.searchtwitter()