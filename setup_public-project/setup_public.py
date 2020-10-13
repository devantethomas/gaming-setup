import psutil
import subprocess
import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#variables for game and music
game = '' #.exe name in game 
game_location = ''
music = 'spotify' 
music_location = r'' #raw string due to use of \u in string
game_on = False
music_on = False

#check if programs are open. If not then will open
for p in psutil.process_iter():
    if game.lower() in p.name().lower():
        game_on = True
    elif music.lower() in p.name().lower():
        music_on = True

if not game_on:
    subprocess.Popen(game_location)

if not music_on:
    subprocess.Popen(music_location)


time.sleep(3) #Change depending on how fast program loads

#spotipy code
client_id = os.environ.get('SPOTIPY_CLIENT_ID') #Environmental variables for SpotifyOAuth
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

playlist_uri = "" #playist you want to play while gaming
dev_id ='' #id of the music player

scope = 'user-read-playback-state streaming user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp.start_playback(device_id=dev_id, context_uri=playlist_uri)
        
        


