### SCRIPT FOR RETRIEVING TWEETS
import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = '2dFAcYLDXNpT5plrRywnZcwMb'
consumer_secret = 'AF4LARd1wl0LtWbaLEejqru0Mmn5XRhWv8MbgY8jMwEEzAogo2'
access_token = '961540992175411201-pijkV9UHMALTfvmZ49jnRapNIUwlhjD'
access_token_secret = 'eTLef6FWg631D8blZDIAAXqh98Ov2GJP4M5B351QLrZo2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file
csvFile = open('filename.csv', 'a')
fieldnames = ['datetime', 'text', 'user','retweets','likes','verified']
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(fieldnames)

#script now also includes the user! but not a seperate column for hashtags
index=0
#the last ten days in since 
for tweet in tweepy.Cursor(api.search,q="globalgoals",count=100,
                           lang="en", since="2018-03-01").items():
    print(tweet.created_at, tweet.text,tweet.user.name, tweet.retweet_count, tweet.favorite_count,tweet.user.verified, tweet.user.location)
    print(index)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.name.encode('utf-8'), tweet.retweet_count,tweet.favorite_count,tweet.user.verified, tweet.user.location.encode('utf-8')])
    index+=1