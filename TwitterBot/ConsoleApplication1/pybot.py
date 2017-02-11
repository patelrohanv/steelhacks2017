#!/usr/bin/python3
import json
import tweepy

consumer_key = 'ZoSd0CJN61VpfgjWVAeIpjjib'
consumer_secret = '11hd2TiCXz7Fv8zZre7cwD1prXsOmBbB8roVr8Mw1PfZetgwIJ'
access_token = '830431809779466240-YTWx5zkdbnynSAqH1mkajmLl1WfLXJI'
access_secret = 'y8UNy0c2WVk1yCiaM6plSDvjorZyUAXOGINehmpoT6ifS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

rate_limit = api.rate_limit_status()
user = api.get_user('AntiHHarassment')

s = "ocean"
for tweet in tweepy.Cursor(api.search,q=s).items(10):
    print('Tweet by: @' + tweet.user.screen_name)