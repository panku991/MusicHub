# MusicHub


# MP3 Player in Python for Windows

This is a simple MP3 player built using Python, pygame and tkinter for the user interface. It runs on Windows and allows the user to play, pause, stop, skip to the next or previous song, and also choose songs from a list. The player is able to read songs from a folder in the user's music directory.



# Requirements

Python 3.x
Pygame module
Tkinter module


# Installation and Running

Install Python 3.x
Install Pygame module by running the command pip install pygame in the command prompt
Run the script mp3_player.py using Python


#Usage

Launch the MP3 player by running the script mp3_player.py
The player window will show up with a list of songs in the user's music folder
Use the buttons to play, pause, stop, skip to the next or previous song
Use the scrollbar to scroll through the list of songs
Click on a song to select it and then click the "play" button to play it
To exit the player, close the window



# Notes


Only MP3 files can be played by this player
Songs are loaded from the folder %userprofile%\Music, which is the default music folder in Windows. To add more songs, simply move them to this folder or change the str variable to the path of a different folder in the code.
The player can also be controlled using the following keyboard shortcuts:
p to play or pause a song
s to stop a song
Left arrow to skip to the previous song
Right arrow to skip to the next song
space to play or pause a song
These keyboard shortcuts are currently commented out in the code but can be enabled by uncommenting the respective lines.



# Conclusion
This is a simple MP3 player built in Python that allows users to play and manage their music collection on their Windows machines. The player is easy to use and can be customized to suit the user's needs. It is also a good starting point for beginners who want to learn about building graphical user interfaces and music players using Python.





