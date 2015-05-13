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

