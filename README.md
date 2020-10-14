# gaming-setup
Start your music and game with a click of a button

The program looks through all the currently running programs. If it does not see the chosen game and/or spotify, it will open them. After a short delay, the playlist listed in the program will start with a random song and proceed from there.

<br/>
Before runnig make sure you have the following libraries installed:
<br/>spotipy
<br/>psutil


Some variables need to be filled in before using:	
<br/> game: The .exe name of the game. Is often just the games name, but can be found by looking at the properties of the application. Also can be found by looking at the application in task manager
<br/><br/>  Game and music location: The path for the program to find the games. Not if the path includes a \U or \R (like \User or \Roaming) the string needs to be a r string (r'path-here'). Works if spotify is downloaded from the website vs the windows store
<br/><br/>  playlist_uri: Can be found right clicking on a playlist > share > Copy spotify URI
<br/><br/>  dev_id: At time of righting, do not know how to find the id of device besides using spotipy's devices() function

Changes coming soon:
<br/>The mentioned variables will be filled in through the command terminal through an update coming soon
<br/>The required pip install will be available through a requirements.txt
