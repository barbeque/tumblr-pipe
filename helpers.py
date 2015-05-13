import yaml

def load_secrets(secretsfile):
	with open(secretsfile) as stream:
		return yaml.load(stream)

def load_config():
	with open('config.yml') as stream:
		return yaml.load(stream)

def tryget_config(config, key, fallback_value = None):
	if key not in config:
		return fallback_value
	return config[key]

def assert_secrets(secrets, prefix):
	for mandatory_key in ['consumer_key', 'consumer_secret', 'token_key', 'token_secret']:
		prefixed_key = prefix + '_' + mandatory_key
		if prefixed_key not in secrets:
			print 'Missing mandatory secrets.yml key called', prefixed_key
			sys.exit()


