import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import pprint
import json

consumer_key = 'AuqelaIg0YLkWC4vToUV8bUMh'
consumer_secret = 'SECNwsCczYbJlIAnxUyfd0ytDDCq2o4Fsr1ZGTMLdCskCxYwPn'
access_token = '147892104-88JainiSiKVksISvRRBvwucpASZsfHKycnwEKWXj'
access_secret = 'nGcAuRx6YAg405JSb6sV1SjkydONgg8H97IGAygvFvt1G'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
