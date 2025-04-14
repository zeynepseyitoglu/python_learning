from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1A5D1A"
YELLOW = "#80C4E9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='POMODORO\nTIMER')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec= WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #count is number of seconds
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds <= 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '🍅' 
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text='POMODORO\nTIMER', fg=GREEN, bg=YELLOW ,font=('System', 25, 'bold'))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato2png.png')
canvas.create_image(100, 100, image=tomato)
timer_text = canvas.create_text(100, 115, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
#choose color from colorhunt.co

canvas.grid(column=1, row=1)

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(20))
check_marks.grid(column=1, row=2)

window.mainloop()

