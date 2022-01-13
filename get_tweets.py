import config
from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import json

def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 2 required authentication tokens:

       1. API_KEY
       2. API_SECRET
     

    See course material for instructions on getting your own Twitter credentials.
    """
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    return auth



###########################################################
for x in ['Greenpeace', 'WHO', 'CNBC', 'UNHumanRights']:

############################################################

    if __name__ == '__main__':
        auth = authenticate()
        api = API(auth)

        cursor = Cursor(
            api.user_timeline,
            id = x,
            tweet_mode = 'extended'
        )

    ############################################################ 
        counter = 0

    ############################################################

        for status in cursor.items(100):
            text = status.full_text

            # take extended tweets into account
            # TODO: CHECK
            if 'extended_tweet' in dir(status):
                text =  status.extended_tweet.full_text
            if 'retweeted_status' in dir(status):
                r = status.retweeted_status
                if 'extended_tweet' in dir(r):
                    text =  r.extended_tweet.full_text

            tweet = {
                'text': text,
            }
           # print(tweet)

            ##################################################################

            with open(f'/{x}/{x}_{counter}.txt', 'w') as file:
                file.write(json.dumps(tweet))
            counter += 1
            print(counter)
            print(x)
            print(tweet)
        


#check: Greenpeace, WHO, CNBC, UNHumanRights

#out_file=open('/Users/nataliaresende/Dropbox/PYTHON/'+text_name,"w")