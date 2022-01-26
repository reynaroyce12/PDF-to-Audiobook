from tkinter import *
from toSpeech import *


BACK_GROUND_COLOR = '#9AD0EC'
FOREGROUND = '#041562'
BUTTON_BG = '#F3C5C5'
BUTTON_FG = '#041562'


def get_path():
    file_path = fr'{path_entry.get()}'.strip('"')
    text_to_speech(file_path)
    message_label.destroy()
    error_label.destroy()
    convert_button.config(state=DISABLED)

    # error_label.config(text="Invalid path!")


def pause():
    pause_speech()


def unpause():
    unpause_speech()


def stop():
    stop_speech()
    window.destroy()


def handle_click(event):
    path_entry.delete(0, END)


window = Tk()
window.title("Pdf to Audiobook")
window.config(padx=50, pady=30, bg=BACK_GROUND_COLOR)

image_canvas = Canvas(width=250, height=260, bg=BACK_GROUND_COLOR, highlightthickness=0)
img = PhotoImage(file='image/book-image.png')
image_canvas.create_image(125, 130, image=img)
image_canvas.grid(row=1, column=2, pady=40)

path_entry = Entry(width=50, bg='#EFDAD7')
path_entry.grid(row=3, column=2, pady=5)
path_entry.insert(0, "Your Pdf file path")
path_entry.bind("<1>", handle_click)

convert_button = Button(text="Read", font=('Courier', 10, 'bold'), command=get_path, width=10, bg=BUTTON_BG, fg=BUTTON_FG)
convert_button.grid(row=5, column=2, pady=10)

pause_game = Button(text="Pause", font=('Courier', 10, 'bold'), command=pause, width=10, bg=BUTTON_BG, fg=BUTTON_FG)
pause_game.grid(row=6, column=2, pady=10)

unpause_button = Button(text="UnPause", font=('Courier', 10, 'bold'), command=unpause, width=10, bg=BUTTON_BG, fg=BUTTON_FG)
unpause_button.grid(row=7, column=2, pady=10)

stop_button = Button(text="Stop", font=('Courier', 10, 'bold'), command=stop, width=10, bg=BUTTON_BG, fg=BUTTON_FG)
stop_button.grid(row=8, column=2, pady=15)

message_label = Label(text="Click on Read button and wait for few seconds :)", font=('Courier', 10, 'bold'),
                      wraplength=300, bg=BACK_GROUND_COLOR, fg=FOREGROUND)
message_label.grid(row=9, column=2)

error_label = Label(text="", font=('Courier', 10, 'bold'), bg=BACK_GROUND_COLOR, fg='#DA1212')
error_label.grid(row=4, column=2, pady=3)

window.mainloop()
