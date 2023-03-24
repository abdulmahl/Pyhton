from pygame import mixer
from tkinter import Tk, Label, Button, filedialog

current_volume = float(.5)

# Functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="documents", title="Please select song")
    # print(filename)
    current_song = filename
    song = filename.split("/")
    song = song[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_label.config(fg="green", text="Now playing : " + str(song))
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_label.config(fg="red", text="Error playing track")    

def play():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_label.config(fg="red", text="Track not selected") 

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_label.config(fg="red", text="Track not selected") 

def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume : Muted")
            return
        current_volume = current_volume - float(.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume " + str(current_volume))
    except Exception as e:
        print(e)  
        song_label.config(fg="red", text="Track is not selected")  

def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green", text="Volume : Max")
            return
        current_volume = current_volume + float(.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume " + str(current_volume))
    except Exception as e:
        print(e)  
        song_label.config(fg="red", text="Track is not selected")

# Main Screen.
master = Tk()
master.title("Music Player")

# Labels.
Label(master, text="Classic Music Player",font=("Roboto", 15), fg="magenta").grid(sticky="N", row=0, padx=120)
Label(master, text="Select Track",font=("Roboto", 12), fg="dark grey").grid(sticky="N", row=1)
Label(master, text="Volume",font=("Roboto", 12), fg="dark grey").grid(sticky="N", row=4)
song_label = Label(master, font=("Roboto", 12))
song_label.grid(sticky="N", row=3)
volume_label = Label(master, font=("Roboto", 12))
volume_label.grid(sticky="N", row=5)

# Buttons
Button(master, text="Select Song", font=("Roboto", 12),command=play_song,fg="magenta",).grid(row=2, sticky="N")
Button(master, text="Pause", font=("Roboto", 12), foreground="magenta", command=pause).grid(row=3, sticky="E")
Button(master, text="Play", font=("Roboto", 12), foreground="magenta", command=play).grid(row=3, sticky="W")
Button(master, text="-", font=("Roboto", 12), foreground="magenta", width=3, command=reduce_volume).grid(row=5, sticky="E")
Button(master, text="+", font=("Roboto", 12), foreground="magenta", width=3, command=increase_volume).grid(row=5, sticky="W")

master.mainloop()
