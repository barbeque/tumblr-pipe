import tumblrposter
import twittersniffer
import helpers
import time
import os

# this service uses twitter sniffer, gets the results
# and pushes them to tumblrposter.

config = helpers.load_config()

def post_tumblr_from_twitter(twitter_status):
	# what we need:
	# 	- picture(s)
	#	- user name
	#	- post content
	#	- tags
	tags = config['tags'] # loaded from yaml woohoo
	content = twitter_status.text
	user_name = twitter_status.user.name
	pictures = twittersniffer.get_media_urls(twitter_status)

	print len(pictures), 'pictures'

	tumblrposter.post_to_tumblr(pictures, content, user_name, tags)

def save_cookie(last_seen_id):
	with open('cookie.txt', 'w') as c:
		c.write("%s" % last_seen_id)

def read_cookie():
	if not os.path.exists('cookie.txt'):
		return None
	else:
		try:
			with open('cookie.txt', 'r') as c:
				return int(c.readline())
		except Error:
			return None

search_term = config['search_term']

# here we go
last_id = read_cookie()

if last_id != None:
	print 'Resuming from tweets after id = {0}.'.format(last_id)

# fetch tweets
new_tweets = twittersniffer.get_tweets_since(search_term, last_id)
if len(new_tweets) > 0:
	last_tweet_seen = max(new_tweets, key = lambda p: p.id)
	last_id = last_tweet_seen.id

	# post tweets, reversed since descending date...
	for new_tweet in reversed(new_tweets):
		print 'Posting a new tweet by', new_tweet.user.name
		post_tumblr_from_twitter(new_tweet)

	print 'Posted', len(new_tweets), 'new tweets. Last id seen is', last_id
else:
	print 'No new tweets to post. Last id seen is', last_id

save_cookie(last_id)

sleep_time = twittersniffer.get_sleep_time()
if sleep_time > 0:
	print 'Need to wait for at least', sleep_time, 'seconds before running again'

# TODO: Don't double post?
