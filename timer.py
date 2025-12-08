from time import sleep

default_time=25*60



def timer(seconds):
    while seconds>0:
        minutes=seconds//60
        saniye=seconds%60
        if saniye<10:
           print(f'{minutes}:0{saniye}')
        else :
           print(f'{minutes}:{saniye}')
        seconds-=1
        sleep(1)



timer(default_time)
