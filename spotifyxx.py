import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


#Get the username from terminal
username = sys.argv[1]

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

def rec1(artist):
    albums=[]
    results = spotifyObject.recommendations([artist['id']])
    print(results['tracks'][0])
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nxxxxxxxxxxxxxxxxxxx\n")
    for track in results['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])

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

        other=searchResults['artists']['items'][0]['genres']

        json1=json.dumps(searchResults['artists']['items'][0]['genres'],sort_keys=True, indent=4)
        print(json1)
        rec1(searchResults['artists']['items'][0])

    if choice == "1":
        break



# import os
# import sys
# import json
# import spotipy
# import webbrowser
# import spotipy.util as util
# from json.decoder import JSONDecodeError
#
# #Get the username from terminal
# username = sys.argv[1]
#
# #https://open.spotify.com/user/moulid15?si=z5EUhNleRa-ChQNDoY-ABQ
# # Erase cache and prompt for user permission
# try:
#     token = util.prompt_for_user_token(username)
# except:
#     os.remove(f".cache-{username}")
#     token = util.prompt_for_user_token(username)
#
# # Create our spotifyObject
# spotifyObject = spotipy.Spotify(auth=token)
#
# user = spotifyObject.current_user()
#
# displayName = user['display_name']
# followers = user['followers']['total']
#
# while True:
#     print()
#     print(">>> Welcome to Spotipy "+displayName+"!")
#     print(">>> You have "+str(followers)+" followers.")
#     print()
#     print("0 - Search for an artist")
#     print("1 - exit")
#     print()
#     choice = input("Your choice: ")
#
#     #Search for the artist_albums
#     if choice == "0":
#         print()
#         searchQuery = input("Ok, what's their name?: ")  # text
#         print()
#         #Get search results
#
#         # searches for an item
#         searchResults = spotifyObject.search(searchQuery,1,0,"artist")
#         print(json.dumps(searchResults,sort_keys=True, indent=4))
#
#         #Artist details
#         artist = searchResults['artists']['items'][0]
#         print(artist)
#         print(artist['name'])
#         print(str(artist['followers']['total'])+" followers")
#         print(artist['genres'][0])
#         print()
#
#
#         # getting image and write to browser
#         webbrowser.open(artist['images'][0]['url'])
#
#         artistID = artist['id']
#
#         #Album and track details
#         trackURIs = []
#         trackArt = []
#         z = 0
#
#         #Extract album data
#         albumResults = spotifyObject.artist_albums(artistID)
#         albumResults = albumResults['items']
#
#         for item in albumResults:
#             print("ALBUM " + item['name'])
#
#             albumID = item['id']
#             albumArt = item['images'][0]['url']
#
#             # Extract track data
#             trackResults = spotifyObject.album_tracks(albumID)
#             trackResults = trackResults['items']
#
#             for item in trackResults:
#                 print(str(z) + ": "+ item['name'])
#                 trackURIs.append(item['uri'])
#                 trackArt.append(albumArt)
#                 z+=1
#             print()
#
#             # just print the stuff
#         # See album art
#         while True:
#             songSelection = input("Enter a song number to see the album art associate with it")
#             if songSelection =='x':
#                 break
#             webbrowser.open(trackArt[int(songSelection)])
#
#     if choice == "1":
#         break
# # print
# # 12133626085
