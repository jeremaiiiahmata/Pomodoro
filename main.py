import os
import sys
import math
from itertools import count
from tkinter import *
from tkinter import font

#-------------------- CONSTANTS --------------------
PRIMARY = "#FF4F4F"
SECONDARY = "#FEF4D9"
BOX_BACKGROUND = "#3E3B34"
TEXT_COLOR = "#1E1D19"
WHITE = "#F3FFFA"
TIMER_FONT = "Inter"
FONT = "Pixelify Sans"

WORK_SECONDS = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60

reps = 0
sets = 0

#-------------------- TIMER RESET --------------------

def resetTimer():
    window.after_cancel(counter)
    title.config(text="Pomodoro Timer")
    canvas.itemconfig(timer, text="00:00")
    print("reset")

#-------------------- TIMER START --------------------

def startTimer():
    global reps

    reps += 1

    if reps % 8 == 0:
        # LONG BREAK
        title.config(text="Long Break")
        countDown(LONG_BREAK)
    elif reps % 2 == 0:
        #SHORT BREAK
        title.config(text="Short break")
        countDown(SHORT_BREAK)
    else :
        title.config(text="Working Mode")
        countDown(WORK_SECONDS)


def countDown(count):

    minutes = math.floor(count/60)
    seconds = count % 60

    if count < 0:
        startTimer()
    else :
        if minutes == 0 and seconds < 10:
            canvas.itemconfig(timer, text=f"00:0{seconds}")
        elif seconds < 10:
            canvas.itemconfig(timer, text=f"{minutes}:0{seconds}")
        elif minutes == 0:
            canvas.itemconfig(timer, text=f"00:{seconds}")
        else:
            canvas.itemconfig(timer, text=f"{minutes}:{seconds}")

        global counter
        counter = window.after(1000, countDown, count-1)

#-------------------- UI SETUP  --------------------
window = Tk()
window.title("Pomodoro Timer")

canvas = Canvas(width=1280, height=720, bg=PRIMARY, highlightthickness=0)
boxBackground = PhotoImage(file="images/box-bg.png")
timerBackground = PhotoImage(file="images/timer-bg.png")
canvas.create_image(640, 360, image=boxBackground)
canvas.create_image(640, 280, image=timerBackground)
timer = canvas.create_text(640, 280, text="00:00", font=(TIMER_FONT, 140, "bold"))
canvas.pack()

#---- Title Label
title = Label()
title.config(width=431, height=77, text="Pomodoro Timer", font=(FONT, 32, "bold"), bg=PRIMARY, fg=SECONDARY)
title.place(x=424,y=15,width=431, height=77)

#---- Copyright Label
copyrightLabel = Label()
copyrightLabel.config(text="Pomodoro Timer by Jeremaiah Mata", font=(FONT, 16, "bold"), bg=PRIMARY, fg=SECONDARY)
copyrightLabel.place(x=424,y=650, width=431, height=29)

#---- Start button
buttonStart = Button()
buttonStart.config(width=25, height=5, text="Start", command=startTimer, font=(FONT, 50, "bold"), borderwidth=0, bg=SECONDARY, fg=TEXT_COLOR)
buttonStart.place(x=317, y=480, width=268, height=108)

#---- Reset Button
buttonReset = Button()
buttonReset.config(width=25, height=5, text="Reset", command=resetTimer, font=(FONT, 50, "bold"), borderwidth=0, bg=SECONDARY, fg=TEXT_COLOR)
buttonReset.place(x=690, y=480, width=268, height=108)


window.mainloop()