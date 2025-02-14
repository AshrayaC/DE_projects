import tweepy

# OAuth1 credentials
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuth1UserHandler(
    consumer_key, 
    consumer_secret, 
    access_token, 
    access_token_secret
)
api = tweepy.API(auth)

# Test API v1.1 call
try:
    user = api.verify_credentials()  # Use verify_credentials() instead of me()
    print(user)
except tweepy.TweepyException as e:
    print(f"Error: {e}")
    
