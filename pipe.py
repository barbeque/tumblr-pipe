import tumblrposter
import twittersniffer

# this service uses twitter sniffer, gets the results
# and pushes them to tumblrposter.

config = helpers.get_config()

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
