import requests
import twitter
import json
import praw
from datetime import date
class StockFeed:
	def __init__(self):
		self.main_dict={}

	def searchfinhub(self):
		try:
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
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
			return self.main_dict
		except:
			return {}
			print("error")
	def searchfinhubstocknews(self,symbol):
		try:
			today = date.today()
			# print(type(today))
			d2 = today.strftime("%Y")
			d1 = today.strftime("-%m-%d")
			lastyear=str(int(d2)-1)+d1
			sup_dict={}
			# print(lastyear,today)
			r = requests.get('https://finnhub.io/api/v1/company-news?symbol='+symbol+'&from='+lastyear+'&to='+str(today)+'&token=bufvijf48v6qf6lbs26g')
			y=r.json()
			for t in y:
				self.main_dict[str(t["id"])]={"id":t["id"],
				"category":t["category"],"datetime":t["datetime"],"image":t["image"],
				"summary":t["summary"],
				"url":t["url"],
				"headline":t["headline"]}
			# print(self.main_dict)
			return self.main_dict
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
		except:
			return {}
			print("error")
	def searchtwitter(self,tags1):
		try:
			main_dict=[]
			sup_dict={}
			api = twitter.Api(consumer_key="0U21owMEyc6Y3QskvqyTtb89i",
	                  consumer_secret="PJNZBd0jbP61hPROazS02TzvtZxJjMeUBsycF0jUMVixLtF6lZ",
	                  access_token_key="1321121639925362688-VRGp4FjSiN7RKthPETXeHrDVC1ocOC",
	                  access_token_secret="ikI8InyZg7WRdoz5EGiPhd1Hp7dpDWmtPTkDDfOl9H8ds")
			# print(api.tweet_mode)
			results = api.GetSearch(
			    raw_query="q="+tags1)
			# y=results[0].AsDict()
			# print(y)
			try:
				
				for x,t in enumerate(results):
					y=results[x].AsDict()
					try:
						if('media'in y) and (len(y["urls"])!=0):
							# print(y['media'][0]['media_url'])
							# print("media")
							if(y["lang"]=="en"):
								# print("worked1",main_dict)
								self.main_dict[str(y["id"])]={"id":y["id"],
								"category":tags1,"datetime":y["created_at"],
								"image":y['media'][0]['media_url'],
								"summary":y["text"],
								"url":y["urls"][0]["expanded_url"],
								"headline":y["source"]}
								continue
								
						elif('media'in y):
							# print(y['media'][0]['media_url'])
							if(y["lang"]=="en"):
								# print("worked2",main_dict)
								self.main_dict[str(y["id"])]={"id":y["id"],
								"category":tags1,"datetime":y["created_at"],
								"image":y['media'][0]['media_url'],
								"summary":y["text"],
								"url":"null",
								"headline":y["source"]}
								continue
						elif(len(y["urls"])!=0):
							# print(y["lang"],y["urls"])
							if(y["lang"]=="en"):
								# print("worked3",main_dict)
								self.main_dict[str(y["id"])]={"id":y["id"],
								"category":tags1,"datetime":y["created_at"],"image":"null",
								"summary":y["text"],
								"url":y["urls"][0]["expanded_url"],
								"headline":y["source"]}
								continue
						else:
							continue
							# print("none1")
					except:
						return {}
						# print("none")


			except:
				return {}
				# print("")
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
			return self.main_dict
		except:
			return {}
			print("error")

			# print(t["category"],"1")
	def searchstockwits(self,sector):
		try:
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
		except:
			print("error")
	def searchtiingo(self,typeof,sector):
		try:
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
			elif(typeof=="stocks"):
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
		except:
			print("error")
	def searchreddit(self,sector):
		print("none")
		client_id="RQCMwDEkpL9c_A"
		client_secret="5tS4n1UNUIw6ZnQmXuMXxQ89Vbtkjw"
		user_agent="Application for Stock"
		reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,password="neverleavefootball10A",username="Ok-Studio7215",user_agent=user_agent)
		# print(reddit.user.me())
		# # print(reddit)
		# # reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")
		# # hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
		# # print(hot_posts)
		# # for post in hot_posts:
		# # 	# print("!")
		# #     print(post.link_type)
		# # for moderator in reddit.subreddit("MachineLearning").moderator():
		# #     print(moderator)
		# # ml_subreddit = reddit.subreddit('MachineLearning')

		# # print(ml_subreddit.description)

		# # import pandas as pd
		# # posts = []
		# # ml_subreddit = reddit.subreddit('MachineLearning')
		# # for post in ml_subreddit.hot(limit=10):
		# #     posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
		# # posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
		# # print(posts)
		hot_posts = reddit.subreddit(sector).hot(limit=100)
		temp_dict={}
		temp_attributes={}
		for post in hot_posts:
			if("self" in post.thumbnail or "spoiler" in post.thumbnail or "default" in post.thumbnail):
				image="null"
			else:
				image=post.thumbnail
			self.main_dict[str(post.id)]={"id":post.id,
			"category":sector,
			"datetime":post.created,
			"image":image,
			"summary":post.selftext,
			"url":post.url,
			"headline":post.title}
		stock_feed_list=[]
		stock_feed_list.append(self.main_dict)	
		print(stock_feed_list)	


##there maybe many different feeds with same id because user follows it we have to get unique only when i will be making an object and putting
## it in user feed i have to make the feed unique with id
# tags={'stocks':['AMZN','AAPL'],'sector':['trending','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}
# feedlist=StockFeed(tags['sector'])
# # feedlist.searchfinhubstocknews(tags['stocks'][0])
# # feedlist.searchfinhub()
# # feedlist.searchstockwits(tags['sector'][0])
# # feedlist.searchtiingo('stocks',tags['stocks'][0])
# feedlist.searchreddit(tags['stocks'][0])