import math
from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK = []
COMPLETED_CYCLE = 0
TIMER = None
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 7

REPS = 0


# ====================RESET======================#


def reset():
    global REPS
    global TICK
    global COMPLETED_CYCLE

    REPS = 0
    TICK = []
    COMPLETED_CYCLE = 0

    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    window.after_cancel(TIMER)
    heading.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    tick.config(text=TICK, font=("", 15), fg=GREEN, bg=YELLOW)
    completed_cycle.config(text=f"Completed Cycle : {COMPLETED_CYCLE}", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)


# ===================TIMER MECHANISM=============#


def start_timer():
    global REPS
    global TICK
    global COMPLETED_CYCLE
    REPS += 1
    if REPS % 8 == 0:
        start_countdown(LONG_BREAK_MIN)
        heading.config(text="Breakkk", font=(FONT_NAME, 30, "bold"), fg=RED)
        TICK = []
        COMPLETED_CYCLE += 1
        completed_cycle.config(text=f"Completed Cycle : {COMPLETED_CYCLE}", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
        # print("Long break : ", LONG_BREAK_MIN)
    elif REPS % 2 == 0:
        start_countdown(SHORT_BREAK_MIN)
        heading.config(text="Break", font=(FONT_NAME, 30, "bold"), fg=PINK)
        # print("Short Break : ", SHORT_BREAK_MIN)
    else:
        start_countdown(WORK_MIN)
        heading.config(text="Work", font=(FONT_NAME, 30, "bold"), fg=GREEN)
        TICK.append("✔")
        tick.config(text=TICK, font=("", 15), fg=GREEN, bg=YELLOW)
        # print("Working mins : ", WORK_MIN)


# =============COUNTDOWN FUNCTION=================#


def start_countdown(time_to_display):
    minutes = math.floor(time_to_display / 60)
    seconds = time_to_display % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time_to_display > 0:
        global TIMER
        TIMER = window.after(1000, start_countdown, time_to_display - 1)
    else:
        start_timer()



# ==============UI CODE==============================#


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=40, pady=20)

heading = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
heading.grid(row=0, column=1, pady=(20, 20))

img = PhotoImage(file="tomato.png")
canvas = Canvas(window, width=210, height=230, highlightthickness=0)
canvas.create_image(100, 112, anchor=CENTER, image=img)
canvas.config(bg=YELLOW)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg="black", fg="white", command=start_timer)
start.grid(row=2, column=0, padx=20, pady=(30, 20))

reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg="black", fg="white", command=reset)
reset.grid(row=2, column=2, padx=20, pady=(30, 20))

tick = Label(text="", font=("", 15), fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1)

completed_cycle = Label(text=f"Completed Cycle : {COMPLETED_CYCLE}", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
completed_cycle.grid(row=4, column=1)

window.mainloop()
