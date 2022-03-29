import spotipy
from credentials import spotipy_credentials
import spotipy.util as util

username = spotipy_credentials['USERNAME']
clientID = spotipy_credentials['SPOTIPY_CLIENT_ID']
clientSecret = spotipy_credentials['SPOTIPY_CLIENT_SECRET']
redirectURI = 'http://google.com'

scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-private'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI,scope=scope)

token = util.prompt_for_user_token(username = username, client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI, scope=scope)

# Create Spotify Object
spotify = spotipy.Spotify(auth=token)
user = spotify.current_user()

#Get web browser to play tracks
devices = spotify.devices()
deviceID = devices['devices'][0]['id']

#print(json.dumps(user,sort_keys=True, indent=4))
playlisturi = "spotify:playlist:7DM159dKkjm0Mgu2gFARp0"

spotify.start_playback(deviceID, playlisturi, None)
print("Welcome to your Spotify Jukebox" + user['display_name'])
tracks = []

while True:
    print("Welcome to your Spotify Jukebox" + user['display_name'])
    print("Enter 'exit' to exit")
    print("Enter a URI")
    songURI = input("Enter a URI: ")
    if songURI == "exit":
        break
    elif songURI in tracks:
        pass
    else:
        spotify.user_playlist_add_tracks(username, "7DM159dKkjm0Mgu2gFARp0", [songURI])
        tracks.append(songURI)