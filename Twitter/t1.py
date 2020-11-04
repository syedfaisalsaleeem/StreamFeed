# import tweepy

# auth = tweepy.OAuthHandler("0U21owMEyc6Y3QskvqyTtb89i", "PJNZBd0jbP61hPROazS02TzvtZxJjMeUBsycF0jUMVixLtF6lZ")
# auth.set_access_token("1321121639925362688-VRGp4FjSiN7RKthPETXeHrDVC1ocOC", "ikI8InyZg7WRdoz5EGiPhd1Hp7dpDWmtPTkDDfOl9H8ds")

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
import twitter
api = twitter.Api(consumer_key="0U21owMEyc6Y3QskvqyTtb89i",
                  consumer_secret="PJNZBd0jbP61hPROazS02TzvtZxJjMeUBsycF0jUMVixLtF6lZ",
                  access_token_key="1321121639925362688-VRGp4FjSiN7RKthPETXeHrDVC1ocOC",
                  access_token_secret="ikI8InyZg7WRdoz5EGiPhd1Hp7dpDWmtPTkDDfOl9H8ds")
print(api.tweet_mode)
# print(api.VerifyCredentials())
#print(api.GetStatus(1321819438019186689))
results = api.GetSearch(
    raw_query="q=cricket")
# print(results[0])
# print(results[0].id)
# print(results[0].AsDict())
# y=results[0].AsDict()
# print(y["text"])
try:
	for x,t in enumerate(results):
		try:
			# print(results[x]["media"])
			y=results[x].AsDict()
			print(y['media'][0]['media_url'])
			# for t1,t2 in enumerate(y):
			# 	print(y)
		except:
			print("none")
except:
	print("")


