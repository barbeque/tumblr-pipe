import pytumblr
import yaml

def load_secrets(secretsfile):
	with open(secretsfile) as stream:
		return yaml.load(stream)

secrets = load_secrets('secrets.yml')

client = pytumblr.TumblrRestClient(
		secrets['consumer_key'],
		secrets['consumer_secret'],
		secrets['token_key'],
		secrets['token_secret']
	 )

print client.info()
