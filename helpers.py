import yaml
import sys
import urllib

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

def assert_secrets(secrets):
	if secrets == None:
		print 'Secrets could not be loaded from file (secrets.yml).'
		sys.exit()

	for mandatory_key in get_secret_keys():
		if mandatory_key not in secrets:
			print 'Missing mandatory secrets.yml key called', mandatory_key
			sys.exit()

def get_secret_keys():
	services = ['tumblr', 'twitter']
	keys = ['consumer_key', 'consumer_secret', 'token_key', 'token_secret']
	return ["{s}_{k}".format(s = service, k = key) for service in services for key in keys]

def download_images_to_directory(images, directory):
	paths = []
	for image in images:
		image_filename = image.split('/')[-1] # last part of the url
		download_path = os.path.join(directory, image_filename)
		urllib.urlretrieve(image, download_path)
		paths.append(download_path)
		print 'Downloaded', image, 'to', download_path
	return paths
