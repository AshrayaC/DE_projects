import tweepy
from kafka import KafkaProducer
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set up your Twitter API credentials
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

# Set up Kafka Producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set the access token and the access token secret
auth.set_access_token(access_token, access_token_secret)
# create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)

topic = 'AI'

# Define your StreamListener to listen for tweets and send to Kafka
class TweetListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        logging.info(f"Tweet received: {status.text}")
        tweet_data = {
            'text': status.text,
            'created_at': str(status.created_at),
            'user': status.user.screen_name
        }
        # Send the tweet to Kafka
        producer.send(topic, tweet_data)

    def on_error(self, status_code):
        if status_code == 420:
            logging.error("Rate limit exceeded")
            return False  # Disconnect the stream
        else:
            logging.error(f"Error occurred: {status_code}")
            return True  # Keep the stream alive on other errors

myStreamListener = TweetListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
myStream.filter(track=['llm'])