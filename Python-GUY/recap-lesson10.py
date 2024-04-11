import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("lesson10")
root.geometry("300x300")
root.resizable(False, False)

btn = ttk.Button(root, text="Click me")
btn.pack()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<FocusIn>', lambda event:print("Entry field selected"))
entry.bind("<FocusOut>", lambda event:print("Event field deselected"))

root.mainloop()



# this is about the lesson 10 and this is the same code in lesson 10 
# this code for the practice again about the python GUY
