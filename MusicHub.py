#import all helpful modules
from tkinter import *
import os
import pygame
from pygame import mixer




#creating music player window
root=Tk()
root.title("Music Player")
root.geometry("700x700")
root.resizable(False,False)

#additional info
str=os.path.join(os.path.expandvars("%userprofile%"),"Music")
FOLDER_PATH=r'%s'%str
os.chdir(str)


mixer.init()
songstatus=StringVar()
songstatus.set("Choosing")

#creating functions


#for playing song
def playsong():
    currentsong=song_box.get(ACTIVE)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
    
    

#for stoping the song    
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

#playing the nextsong
def nextsong():
    active = song_box.get(ACTIVE)
    song_box.selection_clear(ACTIVE)
    listbox_contents = song_box.get(0, END)
    current_pos = listbox_contents.index(active)
    if current_pos + 1 < len(listbox_contents):
        new_pos = current_pos + 1
        song_box.activate(new_pos)
        song_box.selection_set(ACTIVE)
    else:
        new_pos =0
        song_box.activate(new_pos)
        song_box.selection_set(ACTIVE)
    playsong()
    song_box.see(new_pos)

#playing the previous song
def presong():
    active = song_box.get(ACTIVE)
    song_box.selection_clear(ACTIVE)
    listbox_contents = song_box.get(0, END)
    current_pos = listbox_contents.index(active)
    if current_pos - 1 < len(listbox_contents):
        new_pos = current_pos - 1
        song_box.activate(new_pos)
        song_box.selection_set(ACTIVE)
    playsong()
    song_box.see(new_pos)


#for pausing or unpausing the current song
a=0
pause=False
def trysong():
    global pause,a
    a=a+1
    if pause == False:
        pygame.mixer.music.pause()
        pause = True
        
    else:
        pygame.mixer.music.unpause()
        pause = False
        


#music player name
name="Music.hub"



#creating the head of music player
canvas=Canvas(root,width=710,height=100,bg="lightgreen")
canvas.create_text(350,50, text=name,fill="black", font=('Helvetica 20 bold italic'))
canvas.place(x=-5,y=0)
    
    



#creating mainframe
mainFrame=LabelFrame(root,width=710,height=610,bg="lightgray",borderwidth=3).place(x=-5,y=100)

#creating scrollbar
scrollbar = Scrollbar(mainFrame, orient="vertical",width=20)
scrollbar.pack(side="right",fill="y",pady=(120,125))
    
#creating a list box for storing songs
song_box=Listbox(mainFrame,width=115,bg="lightblue",yscrollcommand=scrollbar.set,highlightcolor="white",selectbackground="black")

#adding songs form file exploler
fileNames=os.listdir(FOLDER_PATH)
for fileName in fileNames:
    split=os.path.splitext(fileName)
    file_ex=split[-1]
    if file_ex==".mp3":
        song_box.insert(END,fileName)
            
            


#placing the song_box
song_box.pack(side="left",fill="y",padx=(40,0),pady=(120,125))



    
#configure scrollbar
scrollbar.configure(command=song_box.yview)


#creating buttons

trybtn=Button(mainFrame,text="※",font="Arial 11 italic",width=5,command=trysong).place(x=320,y=620)
playbtn=Button(mainFrame,text="play",font="Arial 11 italic",width=5,command=playsong).place(x=320,y=580)
stopbtn=Button(mainFrame,text="stop",font="Arial 11 italic",width=5,command=stopsong).place(x=320,y=660)
prebtn=Button(mainFrame,text="pre",font="Arial 11 italic",width=5,command=presong).place(x=250,y=620)
nexttbtn=Button(mainFrame,text="next",font="Arial 11 italic",width=5,command=nextsong).place(x=390,y=620)
l1=Label(mainFrame,text="✿◕‿◕✿",font="Arial 28 italic",bg="lightgray").place(x=50,y=620)
l2=Label(mainFrame,text="✿◕‿◕✿",font="Arial 28 italic",bg="lightgray").place(x=500,y=620)



#mianloop
root.mainloop()
