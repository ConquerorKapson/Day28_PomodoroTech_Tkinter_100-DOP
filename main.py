from tkinter import *
import time


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=40, pady=20)


heading = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
heading.grid(row=0, column=1, pady=(20, 20))


img = PhotoImage(file="tomato.png")
canvas = Canvas(window, width=210, height=230, highlightthickness=0)
canvas.create_image(100, 112, anchor=CENTER, image=img)
canvas.config(bg=YELLOW)
canvas.create_text(100,135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


start = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg="black", fg="white")
start.grid(row=2, column=0, padx=20, pady=(30, 20))

reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg="black", fg="white")
reset.grid(row=2, column=2, padx=20, pady=(30, 20))


window.mainloop()
