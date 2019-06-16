import tweepy
import  json
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "1pIGLRGrCSRIrziXdjSR3ZoE7"
consumer_secret = "K5QY6CtHpM8kxvNY3RC6pzFp5QznAx1OrvqtMRNy2tzK7hxFuj"
access_key = "541652003-hEcAmXSyCHJkFB4SSWi9nGAm9rECmBBTSvjET9e9"
access_secret = "6j2FVljFLAmENr2tfuDfkTHZIZBE2mFgyc9TnrvdhAWin"

tmp = []

# Function to extract tweets


def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 500
    tweets = api.user_timeline(screen_name=username, count=number_of_tweets)

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

        # Printing the tweets
    # print(tmp)


    d = {}
    profiles = []
    for i in tmp:
        tweets = {}
        tweets["content"] = i
        tweets["contenttype"] = "text/plain"
        tweets["language"] = "en"
        profiles.append(tweets)

    d["contentItems"] = profiles
    with open('twitter.json', 'w') as secret_info:
        json.dump(d, secret_info, indent=4, sort_keys=True)
    # json.dumps(d)


# Driver code 
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted. 
    get_tweets(input("Please input your twitter username: "))
