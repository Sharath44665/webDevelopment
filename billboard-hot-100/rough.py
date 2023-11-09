import spotipy,pandas
# import json
from spotipy.oauth2 import SpotifyClientCredentials


csvData = pandas.read_csv("myToken.csv")
clientId = csvData.iloc[0]["clientID"]
clientSecret = csvData.iloc[0]["client secret"]

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

# Set up the Spotipy client
client_credentials_manager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the search query # Hello adele
artist = "Sisqo"
track_name = "Incomplete "
search_query = f"artist:{artist} track:{track_name}"

# Search for the track
results = sp.search(q=search_query, type="track")

# with open("deleteOne.json", mode="w") as mySongFile:
#     json.dump(obj=results,indent=4, fp=mySongFile)
# print(results.json)
# Print the track details
if len(results["tracks"]["items"]) > 0:
    track = results["tracks"]["items"][0]
    print(f"Track name: {track['name']}")
    print(f"Artist name: {track['artists'][0]['name']}")
    print(f"Album name: {track['album']['name']}")
    print(f"Release date: {track['album']['release_date']}")
else:
    print("No tracks found.")





'''
# First demo code to get album for birdy
# url = https://open.spotify.com/artist/2WX2uTcsvV5OnS0inACecP/discography/album

results = spotify.artist_albums(birdy_uri, album_type='album')
# with open(file="delete.json", mode="w") as myFile:
#     json.dump(obj=results,fp=myFile,indent=4)
# print(results)
albums = results['items']

print(results["next"])
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
for album in albums:
    print(album['name'])
'''