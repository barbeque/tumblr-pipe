import twitter
import helpers

cfg = helpers.load_config()
secrets = helpers.load_secrets('secrets.yml')
helpers.assert_secrets(secrets)

api = twitter.Api(
	consumer_key = secrets['twitter_consumer_key'],
	consumer_secret = secrets['twitter_consumer_secret'],
	access_token_key = secrets['twitter_token_key'],
	access_token_secret = secrets['twitter_token_secret'] )

credentials = api.VerifyCredentials()

def get_tweets(search_term):
	return get_tweets_since(search_term)

def get_tweets_since(search_term, last_seen_id = None):
	results = api.GetSearch(
			term = search_term,
			since_id = last_seen_id,
			result_type = 'recent',
			include_entities = True )
	return [x for x in results if not is_a_reply(x) and not is_a_retweet(x)]

def dump_status(status):
	print status.text
	print status.user.name
	if is_a_reply(status):
		print '\tIs a reply.'
	if is_a_retweet(status):
		print '\tIs a retweet.'
	if has_media_url(status):
		print '\tHas media URL.'
		dump_media_urls(status)
	print

def is_a_reply(status):
	return status.in_reply_to_user_id != None
def is_a_retweet(status):
	return status.retweeted_status != None
def has_media_url(status):
	return status.media != None
def get_media_urls(status):
	if has_media_url(status):
		return [media['media_url'] for media in status.media]
	else:
		return []
def dump_media_urls(status):
	if has_media_url(status):
		for media in get_media_urls(status):
			print media
def get_sleep_time():
	return api.GetAverageSleepTime('/search/tweets')

if __name__ == '__main__':
	# run some demo tests
	print 'Authenticated to twitter as', credentials.name
	clean_tweets = get_tweets('#garageofidiots')
	for tweet in clean_tweets:
		dump_status(tweet)
