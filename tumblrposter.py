import pytumblr
import yaml
import sys
import helpers

secrets = helpers.load_secrets('secrets.yml')
helpers.assert_secrets(secrets, 'tumblr')

config = helpers.load_config()

# auth via oauth
client = pytumblr.TumblrRestClient(
		secrets['tumblr_consumer_key'],
		secrets['tumblr_consumer_secret'],
		secrets['tumblr_token_key'],
		secrets['tumblr_token_secret']
	 )

info = client.info()
blogs = info['user']['blogs']

blog_name = helpers.tryget_config(config, 'blog', blogs[0]['name'])
print "Targeting blog:", blog_name

# Verify the blog exists...
target_blog = next((blog for blog in blogs if blog['name'] == blog_name), None)
if target_blog is None:
	print 'Could not find a blog with the name', blog_name
	sys.exit()

print "That blog's title is:", target_blog['title']

if __name__ == '__main__':
	client.create_photo(
		blog_name,
		state="published",
		tags=["testing"],
		data=["1.jpg", "2.jpg", "3.jpg"])

def post_to_tumblr(pictures, text, poster, tags):
	client.create_photo(
		blog_name,
		state = 'published',
		tags = tags,
		data = pictures)
