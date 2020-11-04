
import praw
client_id="RQCMwDEkpL9c_A"
client_secret="5tS4n1UNUIw6ZnQmXuMXxQ89Vbtkjw"
user_agent="Application for Stock"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,password="neverleavefootball10A",username="Ok-Studio7215",user_agent=user_agent)
print(reddit.user.me())
# print(reddit)
# reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")
# hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
# print(hot_posts)
# for post in hot_posts:
# 	# print("!")
#     print(post.link_type)
# for moderator in reddit.subreddit("MachineLearning").moderator():
#     print(moderator)
# ml_subreddit = reddit.subreddit('MachineLearning')

# print(ml_subreddit.description)

# import pandas as pd
# posts = []
# ml_subreddit = reddit.subreddit('MachineLearning')
# for post in ml_subreddit.hot(limit=10):
#     posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
# posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# print(posts)
import pprint
hot_posts = reddit.subreddit('MachineLearning').hot(limit=1)
print(hot_posts)
temp_dict={}
temp_attributes={}
for post in hot_posts:
	# print("!")
	# temp_dict['id']=post.id
	temp_attributes['url']=post.url
	temp_attributes['thumbnail']=post.thumbnail
	temp_attributes['title']=post.title
	temp_attributes['selftext']=post.selftext
	temp_attributes['created']=post.created
	temp_attributes['created_utc']=post.created_utc
	temp_dict[post.id]=temp_attributes
	# temp_dict[post.id]=dict(post.thumbnail)
	print(post.selftext)
	pprint.pprint(vars(post)) ##for having which attributes are supported by class
# assume you have a Reddit instance bound to variable `reddit`
# submission = reddit.submission(id="39zje0")
# print(submission.title) # to make it non-lazy
# pprint.pprint(vars(submission))
# print(temp_dict)