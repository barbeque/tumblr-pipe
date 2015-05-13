import tumblrposter
import twittersniffer
import helpers
import time

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

	print pictures

	tumblrposter.post_to_tumblr(pictures, content, user_name, tags)

	
search_term = config['search_term']

# here we go
last_id = None
# run the pump...
while True:
	# fetch tweets
	new_tweets = twittersniffer.get_tweets_since(search_term, last_id)
	if len(new_tweets) > 0:
		last_tweet_seen = max(new_tweets, key = lambda p: p.id)
		last_id = last_tweet_seen.id

		# post tweets
		for new_tweet in new_tweets:
			print 'Posting a new tweet by', new_tweet.user.name
			post_tumblr_from_twitter(new_tweet)
	
	print 'Posted', len(new_tweets), 'new tweets. Last id seen is', last_id

	sleep_time = twittersniffer.get_sleep_time()
	if sleep_time > 0:
		print 'Need to sleep for at least', sleep_time, 'seconds'
	time.sleep(sleep_time + 5) # add an extra 5 seconds just to be nice

	# TODO: Detect ctrl-c and shut down more cleanly?
