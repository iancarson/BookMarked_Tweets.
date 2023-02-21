import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tweepy

# Initialize Firebase SDK with credentials from service account key
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com'
})

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Get user's bookmarked tweets
bookmarked_tweets = api.get_bookmarks()

# Store each bookmarked tweet in Firebase
for tweet in bookmarked_tweets:
    tweet_ref = db.reference('bookmarks').push()
    tweet_ref.set({
        'text': tweet.text,
        'author': tweet.author.screen_name,
        'timestamp': tweet.created_at.timestamp(),
        # Add any other properties you want to store
    })
