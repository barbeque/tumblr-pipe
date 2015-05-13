import pytumblr
import yaml
import sys

def load_secrets(secretsfile):
	with open(secretsfile) as stream:
		return yaml.load(stream)

def assert_secrets(secrets):
	for mandatory_key in ['consumer_key', 'consumer_secret', 'token_key', 'token_secret']:
		if mandatory_key not in secrets:
			print 'Missing mandatory secrets.yml key called', mandatory_key
			sys.exit()

def load_config():
	with open('config.yml') as stream:
		return yaml.load(stream)

def tryget_config(config, key, fallback_value = None):
	if key not in config:
		return fallback_value
	return config[key]

secrets = load_secrets('secrets.yml')
assert_secrets(secrets)

config = load_config()

# auth via oauth
client = pytumblr.TumblrRestClient(
		secrets['consumer_key'],
		secrets['consumer_secret'],
		secrets['token_key'],
		secrets['token_secret']
	 )

info = client.info()
blogs = info['user']['blogs']

blog_sought = tryget_config(config, 'blog', blogs[0]['name'])
print "Targeting blog:", blog_sought
