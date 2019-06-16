import sys
import spotipy
import spotipy.util as util

import random



# - Steps:
#     - 1. Authenticating Spotipy (✅)
#     - 2. Creating a list of your favorite artists (get max 50) ✅)
#         - API: Get a User’s Top Artists and Tracks
#         - Scope: user-top-read
#     - 3. For each of the artists, get all tracks for each artist. ✅
#         - API: Get an Artist’s Top Tracks
#     - 4. From top tracks, select tracks that are within a certain valence range ✅
#         - API: Get Audio Features for Several Tracks
#     - 5. From these tracks, create a playlist for user ✅
#         - API: Create a Playlist
#         - API: Add Tracks to a Playlist
#         - Scope: playlist-modify-public

client_id = "9a6e7be5e69a43f4bfbf7834ca8dd6c1"
client_secret = "fd867b2e103d4f90bb456b57107f75e9"
redirect_uri = "https://www.youtube.com/"


scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
    mood = float(sys.argv[2])
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:

	#Step 1. Authenticating Spotipy

	def authenticate_spotify():
		print('...connecting to Spotify')
		sp = spotipy.Spotify(auth=token)
		return sp

    #Step 2. Creating a list of your favorite artists

	def aggregate_top_artists(sp):
		print('...getting your top artists')
		top_artists_name = []
		top_artists_uri = []

		ranges = ['short_term', 'medium_term', 'long_term']
		for r in ranges:
			top_artists_all_data = sp.current_user_top_artists(limit=50, time_range= r)
			top_artists_data = top_artists_all_data['items']
			for artist_data in top_artists_data:
				if artist_data["name"] not in top_artists_name:
					top_artists_name.append(artist_data['name'])
					top_artists_uri.append(artist_data['uri'])

		followed_artists_all_data = sp.current_user_followed_artists(limit=50)
		followed_artists_data = (followed_artists_all_data['artists'])
		for artist_data in followed_artists_data["items"]:
			if artist_data["name"] not in top_artists_name:
				top_artists_name.append(artist_data['name'])
				top_artists_uri.append(artist_data['uri'])
		return top_artists_uri


    #Step 3. For each of the artists, get a set of tracks for each artist

	def aggregate_top_tracks(sp, top_artists_uri):
		print("...getting top tracks")
		top_tracks_uri = []
		for artist in top_artists_uri:
			top_tracks_all_data = sp.artist_top_tracks(artist)
			top_tracks_data = top_tracks_all_data['tracks']
			for track_data in top_tracks_data:
				top_tracks_uri.append(track_data['uri'])
		return top_tracks_uri

	# Step 4. From top tracks, select tracks that are within a certain mood range

	def select_tracks(sp, top_tracks_uri):

		print("...selecting tracks")
		selected_tracks_uri = []

		def group(seq, size):
			return (seq[pos:pos + size] for pos in range(0, len(seq), size))

		random.shuffle(top_tracks_uri)
		for tracks in list(group(top_tracks_uri, 50)):
			tracks_all_data = sp.audio_features(tracks)
			for track_data in tracks_all_data:
				print(track_data['energy'])
sp = authenticate_spotify()
a = aggregate_top_artists(sp)
t = aggregate_top_tracks(sp,a)
select_tracks(sp,t)
