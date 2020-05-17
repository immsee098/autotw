import tweepy
import time
print('this is my twitter bot')

CONSUMER_KEY = 'PFqIljJVYzfa1EdGVAR9gfFCi'
CONSUMER_SECRET = 'sv53lv7tZOMySgZcAmq2to0k1mu9NN7L6N0qC36UljJopFjxFq'
ACCESS_KEY = '1122744673796124672-7KwMTvjQxL83GI8A2RQrVitd2oN3ll'
ACCESS_SECRET = 'O1aPJEp35DuvsULnF0vbNlThfwl75EzvmRUinpFqZ6TQq'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
