# BookMarked_Tweets.
This Application uses Firebase tools and Twitter API to find a user Bookmarked tweets and store it on Firebase just in case the tweets get deleted or the original user or the current user looses their account.
### Storing Bookmarked Tweets in Firebase using Python
Create a Firebase project and set up a Realtime Database. Follow the instructions in the Firebase documentation to create a new project and set up a Realtime Database. Make sure to note the URL of your Realtime Database, as you will need it later.

- **Install the Firebase SDK for Python.** Install the Firebase SDK for Python using pip:



 `pip install firebase-admin: `
 
- **Initialize the Firebase SDK with your Firebase project credentials.** 
Download a service account key from the Firebase console and save it to a file on your local machine. Then, initialize the Firebase SDK with the following code:

```
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com'
})
```

Replace path/to/serviceAccountKey.json with the path to the service account key file you downloaded in step 2, and replace your-project with the name of your Firebase project.

- **Authenticate with the Twitter API.** Use the Tweepy library to authenticate with the Twitter API using the user's API keys and access tokens.

Retrieve the user's bookmarked tweets. Use the get_bookmarks() method of the tweepy.API object to retrieve a list of the user's bookmarked tweets.

Store each bookmarked tweet in Firebase. For each bookmarked tweet, create a new node in the Realtime Database and set its properties to the relevant tweet data. Here's an example of how to do this:

python
Copy code
import tweepy
from firebase_admin import db

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
This code creates a new node under the bookmarks node in the Realtime Database for each bookmarked tweet, with properties for the tweet text, author screen name, and timestamp. You can add any other properties you want to store for each tweet.
