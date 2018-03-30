### SCRIPT FOR RETRIEVING TWEETS
import tweepy
import csv
#input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file
csvFile = open('filename.csv', 'a')
fieldnames = ['datetime', 'text', 'user','retweets','likes','verified']
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(fieldnames)

#which tweetobjects? https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
index=0
#the last ten days
for tweet in tweepy.Cursor(api.search,q="globalgoals",count=100,
                           lang="en", since="YYYY-MM-DD").items():
    print(tweet.created_at, tweet.text,tweet.user.name, tweet.retweet_count, tweet.favorite_count,tweet.user.verified, tweet.user.location)
    print(index)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.name.encode('utf-8'), tweet.retweet_count,tweet.favorite_count,tweet.user.verified, tweet.user.location.encode('utf-8')])
    index+=1
