import pytumblr
import yaml
import sys
import helpers
import tempfile

secrets = helpers.load_secrets('secrets.yml')
helpers.assert_secrets(secrets)

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
	encoded_poster = poster.encode('utf-8').strip()
	encoded_text = text.encode('utf-8').strip() + '\n' + 'tweet by ' + encoded_poster
	if len(pictures) > 0:
		if len(pictures) > 1:
			print 'Multiple photos encountered on this tweet'
			# Multiple photo mode... need to download the images
			# and then upload from disk
			temp_dir = tempfile.mkdtemp()

			try:
				image_paths = helpers.download_images_to_directory(pictures, temp_dir)
				# Upload
				result = client.create_photo(
					blog_name,
					state = 'published',
					tags = tags,
					caption = encoded_text,
					data = image_paths)
				print result

			finally:
				# Delete temp dir
				shutil.rmtree(temp_dir, ignore_errors = True)

		else:
			# Single photo mode - just give tumblr the URL,
			# it can figure it out
			result = client.create_photo(
				blog_name,
				caption = encoded_text,
				state = 'published',
				tags = tags,
				source = pictures[0])
			print result
