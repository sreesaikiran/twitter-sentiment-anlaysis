
import os
import json

from tweepy import OAuthHandler, Stream, StreamListener
from dotenv import load_dotenv

from utils import remove_urls

load_dotenv('credentials.env')
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        parsed_data = json.loads(data)
        print(f'{remove_urls(parsed_data["text"])}')
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['ocean', 'gardening', 'BMCSoftware', 'school', 'CT', '#metoo', 'governor'],
                  locations=[-73.504389, 41.222582, -71.804192, 42.026518], languages=['en'])
