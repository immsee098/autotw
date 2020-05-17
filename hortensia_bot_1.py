import tweepy
import time
import random
from datetime import datetime
print('this is my twitter bot')

CONSUMER_KEY = 'CA3uBG3tmuKr60izMFGxWkBwF'
CONSUMER_SECRET = 'pIH2u7prjicPE6fngVBKNefCpsYwCpiWlcMeduFrTaCL2yld7f'
ACCESS_KEY = '1128324973494296576-x0tpDOVKCsCb9NqOPmjUS4vz5ri0IA'
ACCESS_SECRET = 'kYNVHEaWX1djSkBJsl51Yircr2YexduIJuje457tP1cii'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
