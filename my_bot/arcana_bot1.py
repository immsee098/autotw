# -*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import tweepy
import time
import random
from datetime import datetime
import math
print('this is my twitter bot')


CONSUMER_KEY = 'idDh6EyajUEy0QATgMswSqvhf'
CONSUMER_SECRET = 'kL9tlcnzR2rlqmofs5Ly6JinaES6j4ZzF2B6wMrLZQZlaRRE5P'
ACCESS_KEY = '1128324973494296576-rv8usVkGVPNIH5kJJ43NDWz03H8EhY'
ACCESS_SECRET = 'er5oTqnRQFhzlxrZGVajgbUMrcVNbb7KrpnOQJjRDEvzN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

mentions = api.mentions_timeline()

FILE_NAME = 'last_seen_arcanabot1.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    abc = ['a', 'b', 'c', 'd', 'e', 'f']
    oddeven = ['의 결과는… 홀!', '의 결과는… 짝!']
    freeTweets = ['(은)는 엄청나게 실패했다! 어디서 부서지는 소리 나지 않았어?', '(은)는 실패했다. 안타깝게도…', '(은)는 기분 좋게 성공했다!', '(은)는 완벽하게 성공했다! 대단한 걸']
    rosipa = ['의 선택은…… 가위!', '의 선택은…… 바위!', '의 선택은…… 보!']
    hh = datetime.now().hour
    mm = datetime.now().minute
    ss = datetime.now().second
    now = ('%s:%s:%s' % ( hh, mm, ss) )

    print('retrieving and replying to tweets...')
    # DEV NOTE: Testing the lastest mention
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'd100' in mention.full_text.lower():
            print('found d100')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,101)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd90' in mention.full_text.lower():
            print('found d90')
            print('responding back...')
            damage = str(random.randrange(1,91))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd89' in mention.full_text.lower():
            print('found d89')
            print('responding back...')
            damage = str(random.randrange(1,90))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd88' in mention.full_text.lower():
            print('found d88')
            print('responding back...')
            damage = str(random.randrange(1,89))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd87' in mention.full_text.lower():
            print('found d87')
            print('responding back...')
            damage = str(random.randrange(1,88))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd86' in mention.full_text.lower():
            print('found d86')
            print('responding back...')
            damage = str(random.randrange(1,87))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd85' in mention.full_text.lower():
            print('found d85')
            print('responding back...')
            damage = str(random.randrange(1,86))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd84' in mention.full_text.lower():
            print('found d84')
            print('responding back...')
            damage = str(random.randrange(1,85))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd83' in mention.full_text.lower():
            print('found d83')
            print('responding back...')
            damage = str(random.randrange(1,84))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd82' in mention.full_text.lower():
            print('found d82')
            print('responding back...')
            damage = str(random.randrange(1,83))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd81' in mention.full_text.lower():
            print('found d81')
            print('responding back...')
            damage = str(random.randrange(1,82))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd80' in mention.full_text.lower():
            print('found d80')
            print('responding back...')
            damage = str(random.randrange(1,81))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd79' in mention.full_text.lower():
            print('found d79')
            print('responding back...')
            damage = str(random.randrange(1,80))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd78' in mention.full_text.lower():
            print('found d84')
            print('responding back...')
            damage = str(random.randrange(1,79))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd77' in mention.full_text.lower():
            print('found d77')
            print('responding back...')
            damage = str(random.randrange(1,78))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd76' in mention.full_text.lower():
            print('found d76')
            print('responding back...')
            damage = str(random.randrange(1,77))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd75' in mention.full_text.lower():
            print('found d75')
            print('responding back...')
            damage = str(random.randrange(1,76))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd74' in mention.full_text.lower():
            print('found d74')
            print('responding back...')
            damage = str(random.randrange(1,75))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd73' in mention.full_text.lower():
            print('found d73')
            print('responding back...')
            damage = str(random.randrange(1,74))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd72' in mention.full_text.lower():
            print('found d72')
            print('responding back...')
            damage = str(random.randrange(1,73))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd71' in mention.full_text.lower():
            print('found d71')
            print('responding back...')
            damage = str(random.randrange(1,72))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd70' in mention.full_text.lower():
            print('found d70')
            print('responding back...')
            damage = str(random.randrange(1,71))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd69' in mention.full_text.lower():
            print('found d69')
            print('responding back...')
            damage = str(random.randrange(1,70))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd68' in mention.full_text.lower():
            print('found d68')
            print('responding back...')
            damage = str(random.randrange(1,69))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd67' in mention.full_text.lower():
            print('found d67')
            print('responding back...')
            damage = str(random.randrange(1,68))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd66' in mention.full_text.lower():
            print('found d66')
            print('responding back...')
            damage = str(random.randrange(1,67))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd65' in mention.full_text.lower():
            print('found d65')
            print('responding back...')
            damage = str(random.randrange(1,66))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd64' in mention.full_text.lower():
            print('found d64')
            print('responding back...')
            damage = str(random.randrange(1,65))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd63' in mention.full_text.lower():
            print('found d63')
            print('responding back...')
            damage = str(random.randrange(1,64))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd62' in mention.full_text.lower():
            print('found d62')
            print('responding back...')
            damage = str(random.randrange(1,63))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd61' in mention.full_text.lower():
            print('found d61')
            print('responding back...')
            damage = str(random.randrange(1,62))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd60' in mention.full_text.lower():
            print('found d60')
            print('responding back...')
            damage = str(random.randrange(1,61))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd59' in mention.full_text.lower():
            print('found d59')
            print('responding back...')
            damage = str(random.randrange(1,60))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd58' in mention.full_text.lower():
            print('found d54')
            print('responding back...')
            damage = str(random.randrange(1,59))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd57' in mention.full_text.lower():
            print('found d57')
            print('responding back...')
            damage = str(random.randrange(1,58))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd56' in mention.full_text.lower():
            print('found d56')
            print('responding back...')
            damage = str(random.randrange(1,57))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd55' in mention.full_text.lower():
            print('found d55')
            print('responding back...')
            damage = str(random.randrange(1,56))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd54' in mention.full_text.lower():
            print('found d54')
            print('responding back...')
            damage = str(random.randrange(1,55))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd53' in mention.full_text.lower():
            print('found d53')
            print('responding back...')
            damage = str(random.randrange(1,54))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd52' in mention.full_text.lower():
            print('found d52')
            print('responding back...')
            damage = str(random.randrange(1,53))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd51' in mention.full_text.lower():
            print('found d51')
            print('responding back...')
            damage = str(random.randrange(1,52))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd50' in mention.full_text.lower():
            print('found d50')
            print('responding back...')
            damage = str(random.randrange(1,51))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd49' in mention.full_text.lower():
            print('found d49')
            print('responding back...')
            damage = str(random.randrange(1,50))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd48' in mention.full_text.lower():
            print('found d48')
            print('responding back...')
            damage = str(random.randrange(1,49))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd47' in mention.full_text.lower():
            print('found d47')
            print('responding back...')
            damage = str(random.randrange(1,48))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd46' in mention.full_text.lower():
            print('found d46')
            print('responding back...')
            damage = str(random.randrange(1,47))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd45' in mention.full_text.lower():
            print('found d45')
            print('responding back...')
            damage = str(random.randrange(1,46))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd44' in mention.full_text.lower():
            print('found d44')
            print('responding back...')
            damage = str(random.randrange(1,45))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd43' in mention.full_text.lower():
            print('found d43')
            print('responding back...')
            damage = str(random.randrange(1,44))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd42' in mention.full_text.lower():
            print('found d42')
            print('responding back...')
            damage = str(random.randrange(1,43))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd41' in mention.full_text.lower():
            print('found d41')
            print('responding back...')
            damage = str(random.randrange(1,42))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd40' in mention.full_text.lower():
            print('found d40')
            print('responding back...')
            damage = str(random.randrange(1,41))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd39' in mention.full_text.lower():
            print('found d39')
            print('responding back...')
            damage = str(random.randrange(1,40))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd38' in mention.full_text.lower():
            print('found d38')
            print('responding back...')
            damage = str(random.randrange(1,39))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd37' in mention.full_text.lower():
            print('found d37')
            print('responding back...')
            damage = str(random.randrange(1,38))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd36' in mention.full_text.lower():
            print('found d36')
            print('responding back...')
            damage = str(random.randrange(1,37))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd35' in mention.full_text.lower():
            print('found d35')
            print('responding back...')
            damage = str(random.randrange(1,36))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd34' in mention.full_text.lower():
            print('found d34')
            print('responding back...')
            damage = str(random.randrange(1,35))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd33' in mention.full_text.lower():
            print('found d33')
            print('responding back...')
            damage = str(random.randrange(1,34))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd32' in mention.full_text.lower():
            print('found d32')
            print('responding back...')
            damage = str(random.randrange(1,33))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd31' in mention.full_text.lower():
            print('found d31')
            print('responding back...')
            damage = str(random.randrange(1,32))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd30' in mention.full_text.lower():
            print('found d30')
            print('responding back...')
            damage = str(random.randrange(1,31))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd29' in mention.full_text.lower():
            print('found d29')
            print('responding back...')
            damage = str(random.randrange(1,30))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd28' in mention.full_text.lower():
            print('found d24')
            print('responding back...')
            damage = str(random.randrange(1,29))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd27' in mention.full_text.lower():
            print('found d27')
            print('responding back...')
            damage = str(random.randrange(1,28))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd26' in mention.full_text.lower():
            print('found d26')
            print('responding back...')
            damage = str(random.randrange(1,27))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd25' in mention.full_text.lower():
            print('found d25')
            print('responding back...')
            damage = str(random.randrange(1,26))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd24' in mention.full_text.lower():
            print('found d24')
            print('responding back...')
            damage = str(random.randrange(1,25))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd23' in mention.full_text.lower():
            print('found d23')
            print('responding back...')
            damage = str(random.randrange(1,24))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd22' in mention.full_text.lower():
            print('found d22')
            print('responding back...')
            damage = str(random.randrange(1,23))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd21' in mention.full_text.lower():
            print('found d21')
            print('responding back...')
            damage = str(random.randrange(1,22))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd20' in mention.full_text.lower():
            print('found d20')
            print('responding back...')
            damage = str(random.randrange(1,21))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd19' in mention.full_text.lower():
            print('found d19')
            print('responding back...')
            damage = str(random.randrange(1,20))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd18' in mention.full_text.lower():
            print('found d14')
            print('responding back...')
            damage = str(random.randrange(1,19))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd17' in mention.full_text.lower():
            print('found d17')
            print('responding back...')
            damage = str(random.randrange(1,18))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd16' in mention.full_text.lower():
            print('found d16')
            print('responding back...')
            damage = str(random.randrange(1,17))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd15' in mention.full_text.lower():
            print('found d15')
            print('responding back...')
            damage = str(random.randrange(1,16))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd14' in mention.full_text.lower():
            print('found d14')
            print('responding back...')
            damage = str(random.randrange(1,15))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd13' in mention.full_text.lower():
            print('found d13')
            print('responding back...')
            damage = str(random.randrange(1,14))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd12' in mention.full_text.lower():
            print('found d12')
            print('responding back...')
            damage = str(random.randrange(1,13))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd11' in mention.full_text.lower():
            print('found d11')
            print('responding back...')
            damage = str(random.randrange(1,12))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd10' in mention.full_text.lower():
            print('found d10')
            print('responding back...')
            damage = str(random.randrange(1,11))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd9' in mention.full_text.lower():
            print('found d9')
            print('responding back...')
            damage = str(random.randrange(1,10))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd8' in mention.full_text.lower():
            print('found d8')
            print('responding back...')
            damage = str(random.randrange(1,9))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd7' in mention.full_text.lower():
            print('found d7')
            print('responding back...')
            damage = str(random.randrange(1,8))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd6' in mention.full_text.lower():
            print('found d6')
            print('responding back...')
            damage = str(random.randrange(1,7))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd5' in mention.full_text.lower():
            print('found d5')
            print('responding back...')
            damage = str(random.randrange(1,6))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd4' in mention.full_text.lower():
            print('found d4')
            print('responding back...')
            damage = str(random.randrange(1,5))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd3' in mention.full_text.lower():
            print('found d3')
            print('responding back...')
            damage = str(random.randrange(1,4))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd2' in mention.full_text.lower():
            print('found d2')
            print('responding back...')
            damage = str(random.randrange(1,3))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd1' in mention.full_text.lower():
            print('found d1')
            print('responding back...')
            damage = str(random.randrange(1,2))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd70' in mention.full_text.lower():
            print('found d70')
            print('responding back...')
            damage = str(random.randrange(1,71))
            damplus = int(int(damage)*0.1)
            if('우세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / '+str(damplus)+')'+ '\n' + str(now), mention.id)
            elif('열세') in mention.full_text.lower():
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은…\n' + ' ' +  '(' + damage + ' / -'+str(damplus)+')'+ '\n' + str(now), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + damage + '> !!' +' '+ '\n' + str(now), mention.id)


        elif 'd20' in mention.full_text.lower():
            print('found d20')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,21)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif '[전투]' in mention.full_text.lower():
            print('found [전투]')
            print('responding back...')
            firstNum = random.randrange(1, 11)
            secondNum = random.randrange(1, 11)
            addNum = int(math.ceil((firstNum + secondNum) / 2))
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자!' + '\n' + '[' + ' ' + str(firstNum) + ' ' + ']' + '  ' + '[' + ' ' + str(secondNum) + ' ' + ']' + '\n' + '평균' + ' ' + str(addNum) +'  '+ '\n' + str(random.randrange(1,101)) + '\n' + str(now), mention.id)

        elif 'd10' in mention.full_text.lower():
            print('found d10')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,11)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd6' in mention.full_text.lower():
            print('found d6')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,7)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif '홀짝' in mention.full_text.lower():
                print('found 홀짝')
                print('responding back...')
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + str(random.choice(oddeven))+' '+ '\n' + str(now), mention.id)

        elif '가위바위보' in mention.full_text.lower():
                print('found 가위바위보')
                print('responding back...')
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + str(random.choice(rosipa))+' '+ '\n' + str(now), mention.id)

        elif '자체휴강' in mention.full_text.lower():
            print('found 자체휴강')
            print('responding back...')
            HueGang = ['선생님의 눈을 피해 숲속으로 피신했다. 바람은 살랑살랑.. 햇볕도 적당하니 절로 졸음이 밀려온다. 가끔은 이렇게 쉬는 것도 좋은 것 같다.  ' + str(random.randrange(600,801)) + '페탈 획득!',
            '고목나무 위로 올라오니 오르텐시아의 풍경이 한눈에 보인다. 저기 웬 땡땡이를 친 걸로 보이는 학생이랑 즐겁게 수다를 떠는 월터 선생님도 보이는걸...  ' + str(random.randrange(600,801)) + '페탈 획득!',
            '나무 아래에서 나만의 시간을 보내고 있는 도중.. 짤그랑 소리와 함께 까마귀가 ' + str(random.randrange(600,801)) + '페탈을 떨어트리고 갔다. 위에 까마귀 둥지가 있었나 보군..',
            '휴강을 위한 내 비밀의 아지트를 만들었더니 한 학생이 급하게 뛰어온다. 「미안한데 나도 좀 숨겨줄래?」 주섬주섬 ' + str(random.randrange(600,801)) + '페탈을 쥐여주며 사정하는 모습이 안타까운데.. 어떡할까?',
            '꾀병 실력이 점점 늘어가는 것만 같다. 오늘도 리얼한 꾀병 연기로 수업 땡땡이에 성공한걸 보니.. 이 정도면 나에게 연기 재능이 있는 것 아닐까 싶은 생각마저 든다.  ' + str(random.randrange(600,801)) + '페탈 획득!',
            '오늘은 기숙사에서 나오지 않을 것이다. 굳게 마음먹고 침대 위에 누워있으니 구석진 곳에서 무언가 반짝거린다. 저거.. ' + str(random.randrange(600,801)) + '페탈 아냐?',
            '오늘도 열심히 쉬어볼까~ 가볍게 나무 위로 올라와서 눈을 감으려는 찰나 아래에서 「나무 타는 실력이 꽤 훌륭하군요. 한두 번 해본 솜씨가 아닌 것 같습니다만..」 하며 시안 선생님이 나를 올려다보고 있다. 아니.. 그게 아니라요...',
            '콜록콜록..! 선생님.. 저 아픈 것 같아요. 하며 꾀병을 부렸으나 눈치 없는 옆 친구가 감기에 좋은 약이 있다며 약을 주섬주섬 꺼내기 시작했다. 제발 눈치 좀 챙겨!',
            '수업 시간에 도망치기 위해 몰래 뒷문을 빠져나오는 순간 복도를 지나던 시안 선생님과 딱 마주쳐버렸다. 「수업이 끝나려면 아직 멀은 것 같은데 이상하네요..」 웃는 얼굴로 말하니 더 무서워..',
            '숨기 좋은 은신처 근처에서 월터 선생님과 마주쳤다. 「어라? ' + mention.user.name +' 학생도 땡땡이를 치는 건가요? 하하핫! 하핫!」 하며 선생님께서 크게 웃는 순간 나까지 들켜버렸다. 선생님..']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(HueGang) + '\n' + str(now), mention.id)

        elif '기마술' in mention.full_text.lower():
            print('found 기마술')
            print('responding back...')
            gima = ['눈에 띄는 붉은 말을 골라 탔더니 호흡도 척척! 누구보다 빠르게 달려 수업도 빠르게 끝냈다!' +  ' (' +  str(random.randrange (600, 801)) + '페탈 획득)', '나와 호흡을 이루는 말이 어디로 달려가더니' + ' ' + str(random.randrange (600, 801)) + '페탈을 물고왔다. 이거 절도 아냐?', '말을 타고 호수 주위를 달리는 수업을 하던 중… 어라? 말 발굽에 무언가 걸렸다.' + ' ' + str(random.randrange (600, 801)) + '페탈이잖아?', '수업을 시작하기 전 건초더미를 옮기고 있었는데 툭. 데구르르르… 와르르르… 건초더미 사이에서' + ' ' + str(random.randrange (600, 801)) + '페탈이 굴러떨어졌다. 횡재야 횡재!', '「몸 숨기기 전술. 오른편 오금을 안장에 걸치고 오른손으로 안장 뒤쪽을 잡고 몸을 말 왼쪽으로 떨어뜨린다. 이 때에는 왼손으로 땅의 모래를 쥐어서 흩뿌리며 적진으로 들어간다.」 신박한 전술이다. 언젠가는 쓸 일이 있지 않을까?' + ' ('+ str(random.randrange (600, 801)) + '페탈 획득)', '실전을 위해 안장 위에 올라앉는 순간 말이 날뛰기 시작한다. 중심을 잡을 틈도 없이 떨어져버렸는데.. 떨어진 충격이 큰지 꽤 아프다..', '오늘은 이 말로 정했다! 교감을 위해 당근을 건네자 맛이 없는지 한 입 먹고 퉤! 뱉어버렸다. 내 성의를…','오늘따라 고삐를 당겨도 말이 내 말을 제대로 들어주지 않는다. 왼쪽으로 가면 오른쪽으로~ 오른쪽으로 가면 왼쪽으로~ 췌키럽 췌키럽~','내가 아끼는 말을 누군가 데려갔다. 쿵짝이 안 맞는 말과 달리니 기운도 빠지고… 말도 속도를 내지 않고… 에잉…','타국에서 오신 선생님께서 전통 마상 묘기를 현란하게 선보이시다 그만 허리가 나가셨다. 오늘의 수업은 여기서… 끝?']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(gima) + '\n' + str(now), mention.id)

        elif '검술' in mention.full_text.lower():
            print('found 검술')
            print('responding back...')
            gumsul = [('하나 둘.. 몇번째지.. 계속 같은 동작으로 검을 휘두르다 보니 팔이 떨어져 나갈 것만 같다. 내일 근육통 오는거 아니겠지? 생각하던 찰나 쉬고 오라며 ' + str(random.randrange (600, 801)) + '페탈을 쥐여주신다. 저 열심히 할게요..!'), ('상대가 휘두르는 검을 빠르게 받아치니 여기저기서 환호성이 들린다. 내가 그렇게 멋있었나? 조금 쑥스러운걸.. 와중에 팬이라며 누군가가 ' + str(random.randrange (600, 801))+'페탈을 내 주머니에 넣어주고 간다. 이거 받아도 되는 거야?'), ('「롱소드를 사용할 때는 상대와 가깝게 붙은 상태에서 싸워야 합니다.」 선생님의 말씀에 따라 긴 목검을 들고 바짝 접촉해보니 상대의 움직임이 훨씬 더 쉽게 읽히는 것만 같다. ' +str(random.randrange (600, 801))+'페탈 획득)'), ('기초는 탄탄할수록 중요한 법. 여러 자세를 고쳐잡으며 검술 동작을 연습해보았다. 어쩐지 점점 동작이 전보다 부드러워지는 것 같다. 뿌듯한걸? '+ str(random.randrange (600, 801)) + '페탈 획득)'), ('챙! 절도있는 움직임으로 검술 대련을 시작했다. 오늘따라 컨디션이 좋은지 선생님에게 칭찬도 받았다! ' + str(random.randrange (600, 801)) + '페탈 획득)'), '이거 진짜 검 맞지? 칼날이 무딘 것 같아서 만져보다 그만 손가락을 조금 베여버렸다. 따가워라...', '내 실력은 그럭저럭 괜찮았지만 경합을 하는 상대의 실력이 너무 좋아 내 실력이 묻혀버렸다. 크윽…', '아야! 상대방이 진심으로 검을 휘둘러 내 어깨를 쳤다. 가짜 칼이 아니었으면 지금 쯤… …일부러는 아니겠지?', '오늘은 이미 배운 수업을 복습하고 복습하고 복습하기만 했다. 신선하지 않아!', '발레에서 검술로 진로를 바꾼 학생의 현란한 검술실력을 보게 되었다. 나비처럼 날아서 나바바를 잘라내는 모습이 아름답기 그지없다…']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(gumsul) + '\n' + str(now), mention.id)

        elif '군사지리' in mention.full_text.lower():
            print('found 군사지리')
            print('responding back...')
            gunjiri = ['적에게 거점이 있다면 먼저 그들의 식량과 자원을 조달하는 길을 알아내어 끊는 것이 최선의 전략! 많이 듣다보니 귀에 딱지가 앉았다. (' + str(random.randrange(600,801)) + '페탈 획득)',
            '세익스페라의 한 곳에 교묘하게 숨겨진 계곡을 제일 먼저 발견했다. 이 곳을 이용한다면 새로운 작전이 떠오르지 않을까? (' + str(random.randrange(600,801)) + '페탈 획득)',
            '지리 전략에는 베르바브의 사례가 많이 참고가 되었다. 그들은 약탈을 업으로 삼으며 살아가기 때문이지! 악행이 지식이 될 수 있다니 아이러니하다. (' + str(random.randrange(600,801)) + '페탈 획득)',
            '다양한 격퇴법을 토론하는 시간이 길어지자 홧김에 물길을 뚫어 적군을 다 침몰시켜 버리기로 했다. 너무 간단하게 끝낸 것 같지만 이기면 그만 아니겠어? (' + str(random.randrange(600,801)) + '페탈 획득)',
            '오르텐시아 주변의 지리를 살펴보는 현장실습 중 ' + str(random.randrange(600,801)) + '페탈이 묻혀진 장소를 발견했다. 최근 까마귀가 반짝이는걸 숨긴다더니 정말인가봐. ',
            '그림 지역에는 깊게 들어가면 출구를 알 수 없어 행방불명이 되는 미지의 숲이 존재한다고 한다. 이곳엔 메르헨이 세워지기 전 전쟁으로 죽은 영혼들도 떠돌아 다닌다나 뭐라나… 흉흉한 소문도 많다.',
            '언젠간 땅이 아닌 하늘에서 전투를 벌이는 날이 올까? 허무맹랑한 이야기겠지. 선생님이 눈치채기 전에 집중하자…',
            '따악! 집중하라는 듯 선생님이 이쪽을 강하게 노려보신다. 집중 집중!',
            '물어보는 질문에 성실히 답했으나 지리의 이점을 잘 활용하지 못했다며 혼이났다. 좀 더 공부해야겠어…']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(gunjiri) + '\n' + str(now), mention.id)

        elif '모의전술' in mention.full_text.lower():
            print('found 모의전술')
            print('responding back...')
            moe = ['야전에서는 땅을 파 만든 창호시설로 적의 공격을 방어한다고 한다. 참호 설치를 위해 열심히 땅을 파던 중.. ' + str(random.randrange(600,801)) + '페탈이 흙에 섞여 나왔다. 누가 여기에 비상금이라도 묻어놓은 건가?',
            '메르헨 기사단에서는 야습을 위해 손으로 암어를 정해둔다. 그리고 검지랑 중지를 까딱이면… 귀엽다고  ' + str(random.randrange(600,801)) + '페탈을 받을 수 있다.',
            '전술 보완을 위해 요새 주변에 마름쇠를 깔아두면 좋겠지? 조심히 다루어 아군은 살리고 상대팀을 격파했다!  (' + str(random.randrange(600,801)) + '페탈 획득)',
            '오늘 따라 머리가 잘 돌아가는 느낌이야! 여기선 심리전! 그리고 순자방법 삼십육계 줄행랑! 술술 나오는 전략으로 칭찬을 잔뜩 들었다! (' + str(random.randrange(600,801)) + '페탈 획득)',
            '때에 따라선 철수하는 것도 전술의 한 방법이 될 수 있다. 전쟁은 마지막의 한 사람이 남을때까지 끝난게 아니니까! 포기하지 않는 나의 마음에 ' + str(random.randrange(600,801)) + '페탈로 건배!',
            '멍하니 땅을 파본다. 어쩐지 계속 삽질만 하는 기분인데.. 선생님 언제 끝나나요? 고개를 들어보니 아무도 없다. 너무 땅 파는 것에 집중했나 보다..',
            '내 모든 전술을 갖고 선생님께 덤벼 보았지만 너무 가볍게 막혀버렸다. 이래서 졸업이나 할 수 있겠어?! 선생님에게 혼나버렸다…',
            '오르텐시아의 비밀 통로를 이용하는 수업! 을 하려고 했는데 아무리 찾아도 보이지 않는다… 이상하다 어제까진 있었는데 없어졌습니다?',
            '오늘은 선생님의 비술을 전달하겠다고 말해던 날! 그런데… 어라? 선생님이 수업에 나타나지 않았다. 설마 거짓말?',
            '사공이 많으면 배가 산으로 간다고 했던가? 같은 수업을 듣는 학생들의 의견이 너무 많아 오늘의 수업은 꽝이었다. 에잉!']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(moe) + '\n' + str(now), mention.id)

        elif '정치학' in mention.full_text.lower():
            print('found 정치학')
            print('responding back...')
            Jungchi = ['정치에 있어서 가장 중요한 건 사람에게 받는 신임이다. 그들에게 받는 믿음은 일을 추진하는데에 있어... 느릿하게 읽는 선생님의 목소리가 어쩐지 자장가 처럼 느껴졌지만 눈을 빠릿하게 뜨고 수업에 집중했다. 오늘은 기필코...! ' + str(random.randrange(600,801)) + '페탈 획득.',
            '"제 1왕녀는 추진적인 정치를 펼치며 귀족들의 신임을..." 예시를 들며 설명해주시는 선생님의 이야기를 들으며 필기를 열심히 했다. 어쩐지 오늘따라 집중이 잘 되는 기분인걸! ' + str(random.randrange(600,801)) + '페탈 획득.',
            '두터운 정치학 책을 펼치자 제 1왕자의 정치적인 성향과 그에 따른 평민. 귀족들이 따르는 정치적은 상황과 경제적인 움직임에 대해서 상세하게 적혀있다. 흠..음음.. 그래 이래서 이런거였군. ' + str(random.randrange(600,801)) + '페탈 획득',
            '"엣헴. 그러니까... 무엇보다도 중요한건..." 선생님이 수업을 하다 자기 자랑에 빠져버렸다. 휴... 어쩔 수 없지. 오늘은 자습이라도 해볼까. 한껏 집중하여 책을 열심히 읽었다. ' + str(random.randrange(600,801)) + '페탈 획득.',
            '"사실 정치에서 중요한 건 편가르기 아니야?"  모르는 얼굴의 선배가 슬쩍 ' + str(random.randrange(600,801)) + '페탈을 넣어주고 갔다. 아니 이게 뭔데요? 왜 벌써부터 편을 가르세요?',
            '선생님이 이야기하시는 어려운 용어들이 마치 주문을 외는 것만 같다.. 열심히 해석하는 사이 순식간에 진도가 뒤처져버렸는데.. 아무래도 다시 복습을 해야 되겠지..',
            '꾸벅..꾸벅... 감기기 시작한 눈은 아무리 눈을 크게 떠도 감당이 안될만큼 묵직하다. 선생님, 제가 자려고 했던게 아니라요! 아야! 돌돌 뭉친 책으로 이마를 맞았다. 흑흑.',
            '바스락... 바스락... 너무 배가 고파 슬쩍 챙겨온 음식을 열었다. 후후... 잘먹겠습니다. 한 입 먹으려던 순간 귀신같이 알아차렸는지 바로 눈을 마주쳤다. "나와라, ' + mention.user.name + '" 힝...',
            '현재의 정치상황. 그리고 과거의 정치 상황에 대하여 선생님이 예시를 들어 열심히 설명하고 계시지만 교재에 찍힌 왕녀님의 사진이 너무 예뻐 그만 정신이 홀려버리고 말았다. 아아...왕녀님...!',
            '정치에는 언제나 돈이 따른다. 사람들을 움직이는데에 있어서 가장 효율적이며.... ... 아니 결론은 뭔데요! 장황하게 적혀있는 내용을 보며 탁 하고 책을 덮어버렸다.']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(Jungchi) + '\n' + str(now), mention.id)

        elif '전쟁사' in mention.full_text.lower():
            print('found 전쟁사')
            print('responding back...')
            Junjang =['데보티오 이전, 가장 최근에 일어난 전투는 메르헨이 우위를 점한 전투였다. 그들은 무력적으로 약해 모두 투항을 했으며... 이런 식의 전투도 있었구나. 처음 아는 사실이다.  ' + str(random.randrange(600,801)) + '페탈 획득!',
            '이전 메르헨의 전투에서는 지형이 험한 곳에서의 전투도 있었다. 그들은 기습에 능하여 처음의 전투에는 속절없이 당했으나,... ... 뭐야 이 뒤의 내용은 어디갔어?! ' + str(random.randrange(600,801)) + '페탈 획득!',
            '어디보자.. .이번 과제로 내준 책들은... 메르헨의 전쟁역사. 그들은 어떻게 하여 강대국으로 남았는가. 주변국들의 위협에도 불구하고 우뚝 선 메르헨.  ... ... 잠깐만요 선생님 이거 책 너무 많지 않나요!? ' + str(random.randrange(600,801)) + '페탈 획득',
            '원인을 알 수 없는 지진. 데보티오가 일어났을 적, 다른 나라 또한 혼란스러운 시기가 있었고. 자신의 나라에 부족한 것들을 강탈하기 위하여 이곳저곳에서 전쟁이 일어났다. 살기 위해서 라고해도 끔찍한 이야기다.  ' + str(random.randrange(600,801)) + '페탈 획득!',
            '"지루한듯 하구나. 그래, 옛날 이야기 하나 해볼까. 데보티오 이전의 이야기란다. ... ..." 하나 둘 잠들었던 아이들이 깨어나 선생님이 얘기하는 옛날 이야기를 들었다. 생각보다 흥미로운걸 ' + str(random.randrange(600,801)) + '페탈 획득.',
            '"에... 그러니까, 여기에 나오는건 중요하니 꼭 외우도록 하고... 에, 또. 이전 데보티오가 일어나기 전에는..." 선생님의 이야기가 자꾸만 자장가로 들려온다. 잠들면...안되는..ㄷ...쿠우울.',
            '이전의 이야기는 관심도 없고, 교재에 나온 사람들의 얼굴에 낙서를 하기 시작했다. 푸핫! 푸흐핫! 이거 너무 잘그린 것 같은데? 회심의 역작이다.',
            '선생님의 이야기를 한귀로 듣고, 한귀로 흘리며 펜을 빙글빙글 돌렸다. 서른 두바퀴...서른 세바퀴... 여기서 열 바퀴만 더 돌리면 정말 신기록 세우겠는데?',
            '"야, 너 지우개좀 줘봐." 옆자리에 있는 아이의 지우개를 뺏어 하나 둘 탑을 쌓기 시작했다. 아슬아슬하게 쌓인 지우개 탑은 어느덧... ' + str(random.randrange(3,10)) + '층...!',
            '왜 이게 선택과목이 아닌거야... 잔뜩 싫은 얼굴로 책만 팔랑팔랑 넘기다 풀썩 고개를 숙여 잠들어 버리고 말았다. 이야~ 자장가로 딱인걸요 선생님.']
            api.update_status('@' + mention.user.screen_name + ' ' + random.choice(Junjang) + '\n' + str(now), mention.id)

        else:
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + random.choice(freeTweets)+' '+ '\n' + str(now), mention.id)


while True:
    reply_to_tweets()
    time.sleep(30)
