#libraries which i used
from tkinter import *
from time import sleep

#Definening Class
class Buttons:
    def __init__(self,word,bgcolor,activecolor):
        self.word = word
        self.bgcolor = bgcolor
        self.activecolor = activecolor

#Declaration of app window parametrs
window=Tk()
window.geometry("300x300")

frame=Frame(window)
frame.pack()
Button_Work=Buttons("Work","#ffffff","#f43f5e")
Button_Short=Buttons("Short","#ffffff","#0d9488")
Button_Long=Buttons("Long","#ffffff","#2563eb")

#timer for time and breaks
default_time=25*60
short_break=5*60
long_break=15*60

boolean=True
#function of timer
def timer(seconds):
    global boolean
    while seconds>0 and boolean:
        if seconds%60<10:
            time=f"{(seconds)//60}:0{seconds%60}"
        else:
            time=f"{(seconds)//60}:{seconds%60}"
        Label.config(text=time)
        Label.update()
        sleep(1)
        seconds = seconds - 1


def pause():
    global boolean
    boolean = False
    timer()

#Buttons and Labels btw
Work=Button(frame,text=Button_Work.word,command=lambda:timer(default_time),background=Button_Work.bgcolor,activebackground=Button_Work.activecolor)
Work.pack(side=LEFT)

Short=Button(frame,text=Button_Short.word,command=lambda:timer(short_break),background=Button_Short.bgcolor,activebackground=Button_Short.activecolor)
Short.pack(side=LEFT)

Long=Button(frame,text=Button_Long.word,command=lambda:timer(long_break),background=Button_Long.bgcolor,activebackground=Button_Long.activecolor)
Long.pack(side=LEFT)

Label=Label(window,text=f"{(default_time)//60}:{(default_time)%60}0",fg="black",bg="white")
Label.place(x=120,y=150)
Label.config(padx=10,pady=10)

button_stop=Button(window,text="▶︎‖",background=Button_Work.bgcolor,command=lambda:pause())
button_stop.place(x=55,y=190)

window.mainloop()
