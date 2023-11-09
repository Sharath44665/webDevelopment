import spotipy,pandas
from spotipy.oauth2 import SpotifyOAuth
#
# class SpotifyToken:
#     def __init__(self):
csvData = pandas.read_csv("myToken.csv")
clientID = csvData.iloc[0]["clientID"]
clientSecret = csvData.iloc[0]["client secret"]
redirectUri = csvData.iloc[0]["Redirect uri"]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri=redirectUri,
                                               scope="SCOPE"))
