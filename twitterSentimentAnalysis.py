import tweepy
from textblob import TextBlob
import numpy as np
import operator
import csv
consumer_key='jBOdi5A5tfm1XoWWyjAgQGzEk'
consumer_secret='loLBDRZHbepV4luOlWUFEcco8c8d2ejRfZLweBC5I4N72e0vlO'

access_token='813424749481070592-jmN6QDRcwwywwDxER4997PpHOUVYi7v'
access_token_secret='vLpqPqFf8119CkhQJ6Q1ZqK1gCaTgjwve5BJVjE90AjOd'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Aleppo')
for i in public_tweets:
	print(i.text)
	analysis = TextBlob(i.text)
	print(analysis.sentiment)


array=[]

def get_label(analysis):
	if analysis.sentiment[0]>0.25:
		return 'Positive'
	else:
		return 'Negative'

with open('tweets.csv','wb') as txtfile:
	abc = csv.writer(txtfile)
	for i in public_tweets:
		analysis = TextBlob(i.text)
		array.append(analysis.sentiment[0])
		# txtfile.write('%s,%s\n'%(i.text,get_label(analysis)))
ans = np.mean(array)

#cant write successfully in csv file

print("The sentiment analysis for Trump is {}"
	  .format(ans))
