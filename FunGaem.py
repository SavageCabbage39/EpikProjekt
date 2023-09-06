import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

#app window
window = tk.Tk()
window.title("Roll the dice!")
window.attributes('-fullscreen', True)  # Make the window fullscreen
window.protocol("WM_DELETE_WINDOW", lambda:None) #Prevents closing the tab with X
window.overrideredirect(True)  # Remove title bar and window decorations


# Load and display the background image
background_image = tk.PhotoImage(file="Assets/dice.png")

# Create a label to display the background image
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Send the background label to the back so other widgets can appear on top of it
background_label.lower()

#Start Screen
fontstyle=("Comic Sans MS", 35)
start_label = tk.Label(
    master=window,
    text="click to roll",
    font=fontstyle,
    anchor="n",
    borderwidth=0,
    background="black",
    foreground="white"
    )
start_label.pack()




#dice generator
def roll():
    dice = random.randint(1,20)
    number.set(dice)
    button.config(state="disabled") #Prevents spam clicking
    window.after(3000, window.destroy) #closes the window in 5 seconds




#input
button = ttk.Button(master = window, text="roll", command=roll)
button.pack()


#output
number=tk.StringVar()
bottom_text = tk.Label(master= window, text="Bottom text", font="Calibri 77", textvariable=number,anchor="center",borderwidth=0)
bottom_text.pack(pady=300)


#run
window.mainloop()
