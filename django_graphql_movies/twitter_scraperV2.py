import tweepy
import json
# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "TSHKhUaNBtYyCAz6fVIFWqt7t"
consumer_secret = "NVpGIVRaSA60uiEWwmWBNw8wozwD3b4f6ICgSP3ohMFOQ0xFeJ"
access_key = "541652003-V0lzzHhzDd55ZL26KWWvZ2Aodu4lhU0MffEbfeiz"
access_secret = "A0l0chyzncoXPnOehK6ujxUl2S2Hib2CfkHueSbSJ4Ho3"

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

    # d = {}
    # profiles = []
    return_text = ""
    for i in tmp:
        return_text = return_text + i
    #     tweets = {}
    #     tweets["content"] = i
    #     tweets["contenttype"] = "text/plain"
    #     tweets["language"] = "en"
    #     profiles.append(tweets)
    #
    # d["contentItems"] = profiles
    # with open('twitter.json', 'w') as secret_info:
    #     json.dump(d, secret_info, indent=4, sort_keys=True)
    # # json.dumps(d)

    # text_file = open("profile_txt.txt", "a")
    # text_file.write(return_text)
    return return_text
