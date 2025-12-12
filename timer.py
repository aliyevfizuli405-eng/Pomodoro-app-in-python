#stilldevolopmentprocess


from tkinter import *

from time import sleep


class Buttons:
    def __init__(self,word,bgcolor,activecolor):
        self.word = word
        self.bgcolor = bgcolor
        self.activecolor = activecolor

window=Tk()

window.geometry("300x300")

frame=Frame(window)
frame.pack()
Button_Work=Buttons("Work","#ffffff","#f43f5e")
Button_Short=Buttons("Short","#ffffff","#0d9488")
Button_Long=Buttons("Long","#ffffff","#2563eb")


default_time=25*60
short_break=5*60
long_break=15*60



def timer(seconds):
    while seconds>0:
        if seconds%60<10:
            time=f"{(seconds)//60}:0{seconds%60}"
        else:
            time=f"{(seconds)//60}:{seconds%60}"

        Label.config(text=time)
        Label.update()
        sleep(1)
        seconds=seconds-1

def short_break_timer(saniye):
    while saniye>0:
        if saniye%60<10:
            time=f"{(saniye)//60}:0{saniye%60}"
        else:
            time=f"{(saniye)//60}:{saniye%60}"
        sleep(1)
        saniye=saniye-1

        Label.config(text=time)
        Label.update()

    return True

def long_break_timer(seconds):
    while seconds>0:
        if seconds%60<10:
            time=f"{(seconds)//60}:0{seconds%60}"
        else:
            time=f"{(seconds)//60}:{seconds%60}"
        sleep(1)
        seconds=seconds-1
        Label.config(text=time)
        Label.update()


def stop():
    return 1



Work=Button(frame,text=Button_Work.word,command=lambda:timer(default_time),background=Button_Work.bgcolor,activebackground=Button_Work.activecolor)
Work.pack(side=LEFT)

Short=Button(frame,text=Button_Short.word,command=lambda:short_break_timer(short_break),background=Button_Short.bgcolor,activebackground=Button_Short.activecolor)
Short.pack(side=LEFT)

Long=Button(frame,text=Button_Long.word,command=lambda:long_break_timer(long_break),background=Button_Long.bgcolor,activebackground=Button_Long.activecolor)
Long.pack(side=LEFT)

Label=Label(window,text=f"{(default_time)//60}:{(default_time)%60}0",fg="black",bg="white")
Label.place(x=120,y=150)
Label.config(padx=10,pady=10)

button_stop=Button(window,text="▶︎‖",background=Button_Work.bgcolor)
button_stop.place(x=55,y=190)
window.mainloop()
