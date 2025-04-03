from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check = "✔"
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    reps +=1

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global check

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown,count -1 )
    else:
        start_timer()
        if reps %2 == 0:
            check_label.config(text=check)
            print(check)
            check += "✔"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100 ,112, image=tomato)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))



start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
















