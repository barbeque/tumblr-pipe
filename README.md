# Tumblr Pipe
This is a little program that you can run that takes tweets containing photos from a Twitter search and uploads them into your Tumblr.

It's pretty similar to the IFTTT "create a photo on tumblr" plugin, but automatically excludes retweets and replies to cut down on fuzz in your tumblr blog.

## Requirements
 * [pytumblr](https://github.com/tumblr/pytumblr)
 * [python-twitter](https://github.com/bear/python-twitter)

Install with `pip install -r requirements.txt`.

## How to Use
After installing all requirements, create a file called `secrets.yml` in the same directory as `pipe.py`. It must contain the following keys:
 * `tumblr_consumer_key`
 * `tumblr_consumer_secret`
 * `tumblr_token_key`
 * `tumblr_token_secret`
 * `twitter_consumer_key`
 * `twitter_consumer_secret`
 * `twitter_token_key`
 * `twitter_token_secret`

These keys can be gained by creating an application in both the tumblr and twitter APIs and then copying the respective OAuth details to allow the application to work.

Once `secrets.yml` is set up, change `config.yml` to suit your blog.

|Key              | What's it for?                   |
|---              | ---                              |
|`blog`		  | The username of your blog        |
|`tags`           | A list of tags to be applied to every tumblr post |
|`search_term`    | The search term to search for on Twitter. |

Last, launch the application with python:
```
python pipe.py
```

## Known Issues
### Multiple images aren't supported
The twitter api for `/search/tweets` is [currently broken](https://twittercommunity.com/t/search-tweets-endpoint-and-extended-entities/31655). The functionality to support it should exist once it starts working again, but is obviously untested..

Update: Some testing has happened, but it is still largely unproven.

### Saves state in a dumb way
It needs to be changed from saving in a text file to saving to a database or something so it can be converted to a Heroku scheduled task or similar.

If any failures occur, it will constantly attempt to repost the last images since the cookie, possibly filling an entire tumblr with the same posts until the problem is fixed.
