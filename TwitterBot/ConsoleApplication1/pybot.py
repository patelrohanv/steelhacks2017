#!/usr/bin/python3
import json
import tweepy
import urllib

consumer_key = 'ZoSd0CJN61VpfgjWVAeIpjjib'
consumer_secret = '11hd2TiCXz7Fv8zZre7cwD1prXsOmBbB8roVr8Mw1PfZetgwIJ'
access_token = '830431809779466240-YTWx5zkdbnynSAqH1mkajmLl1WfLXJI'
access_secret = 'y8UNy0c2WVk1yCiaM6plSDvjorZyUAXOGINehmpoT6ifS'
tweetBody = ' Hello! Remember to be respectful to others on the internet. Don’t use words that may directly offend someone. Together we can end online harassment. #HackHarassment.'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

rate_limit = api.rate_limit_status()
user = api.get_user('AntiHHarassment')
badwords_textFile = open('../badwords.txt')
games = open('../games.txt')
#txt = urllib.request.urlopen("http://www.bannedwordlist.com/lists/swearWords.txt").read()
txtOne = games.read().splitlines()
txtTwo = badwords_textFile.read().splitlines()
games = txtOne
badwords = txtTwo
ignoreWordsArray = ['youtube', 'twitch', 'instagram', 'facebook', 'twitter', 'snapchat', 'reddit', 'tumblr', 'myspace']
tweetId = "0"
tweetUser = "0"
#print(txtOne)
#print(txtTwo)
#print(len(games))
wordcount = [None] * len(games)
#print(len(wordcount))
i = -1
flag = False
for game in games:
    i = i+1
    count = 0
    #print(i)
    wordcount[i] = count
    for word in badwords:
        for tweet in tweepy.Cursor(api.search,q=[game,word]).items(10):
            for ignoreword in ignoreWordsArray:
                if ignoreword in tweet.text:
                    flag = True 
                    #if the flag is true, this tweet should be ignored.
            if flag == False:
                tweetId = tweet.id
                tweetUser = tweet.user
                finalTweetStatus = str(tweetUser) + str(tweetBody)
                api.update_status(finalTweetStatus , tweetId)
                count = count+1
                wordcount[i] = count
                #print('Tweet by: @' + tweet.user.screen_name)
                #print(tweet.text)
for i in range(0,len(games)):
    print(str(games[i]) + ": " + str(wordcount[i]))