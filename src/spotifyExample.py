import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


#Get the username from terminal
username = sys.argv[1]
D=dict={}
categories=[]
#https://open.spotify.com/user/moulid15?si=z5EUhNleRa-ChQNDoY-ABQ
# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']
# def dl(s):


def cat():
    s=spotifyObject.categories(country=None,locale=None,limit=50,offset=0)
    # for i in s:
    #     print(i)
    #     break
    for i in s['categories']['items']:
        categories.append(i['id'])


#recommendations
def rec1(artist,i):
    albums=[]
    results = spotifyObject.recommendations([artist['id']])
    for track in results['tracks']:
        data=track['name']+'-'+ track['artists'][0]['name']
        if i in D.keys():
            D[i].append(data)
        else:
            D[i]=[data]

while True:
    print()
    print(">>> Welcome to Spotipy "+displayName+"!")
    print(">>> You have "+str(followers)+" followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    #Search for the artist_albums
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        #Get search results

        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        try:
            other=searchResults['artists']['items'][0]['genres']
            json1=json.dumps(searchResults['artists']['items'][0]['genres'],sort_keys=True, indent=4)
            # print(json1)
            rec1(searchResults['artists']['items'][0],other[-2])

            cat()
            print("categories :\n\n",json.dumps(categories,sort_keys=True, indent=4))
            print()
            print("dict:\n\n",json.dumps(D,sort_keys=True, indent=4))
        except IndexError:
            print("retry")





    if choice == "1":
        break
