import twitter
import helpers

cfg = helpers.load_config()
secrets = helpers.load_secrets('secrets.yml')
helpers.assert_secrets(secrets, 'twitter')

api = twitter.Api(
	consumer_key = secrets['twitter_consumer_key'],
	consumer_secret = secrets['twitter_consumer_secret'],
	access_token_key = secrets['twitter_token_key'],
	access_token_secret = secrets['twitter_token_secret'] )

credentials = api.VerifyCredentials()

if __name__ == '__main__':
	# run some demo tests
	print 'Authenticated to twitter as', credentials.name
