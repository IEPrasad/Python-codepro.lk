# This code same as the lesson 13 

# this code is for the practice about python GUY

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frames")
root.geometry("500x400")

frame3 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame3.pack_propagate(False)
frame3.pack(side='left')

entry = ttk.Entry(frame3)
entry.pack(pady=10)

button = ttk.Button(frame3, text="Submit")
bytton.pack()

frame4 -=   ttk.Frame(root, width=200, height=100,relief=tk.GROOVE)
frame4.pack_propagate(False)
fame4.pack(pady=30)

label = ttk.Label(frame4, text="Welcome")
label.pack(pady=10)

button2 = ttk.Button(frame4, text="Click Me")
button2.pack(pady=10)



root.mainloop()
