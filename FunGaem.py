import tkinter as tk
from tkinter import ttk
import random

#app window
window = tk.Tk()
window.title("Roll the dice!")
window.geometry("500x500")

#Start Screen
fontstyle=("Comic Sans MS", 35)
start_label = ttk.Label(master = window, text="click to roll",font=fontstyle)
start_label.pack()

#dice
def roll():
    dice = random.randint(1,20)
    number.set(dice)
    button.config(state="disabled") #Prevents spam clicking
    window.after(3000, window.destroy) #closes the window in 5 seconds





#input
input_frame = ttk.Frame(master=window)
button = ttk.Button(master = input_frame, text="roll", command=roll)
button.pack()
input_frame.pack(pady=10)

#output
number=tk.StringVar()
bottom_text = ttk.Label(master=window, text="Bottom text", font="Calibri 77", textvariable=number)
bottom_text.pack(pady=5)



#run
window.mainloop()
