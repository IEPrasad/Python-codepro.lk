import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Lesson11")
root.geometry("500x400")
root.resizable(False, False)

canvas = tk.Canvas(root, bg='white')
canvas.pack()

brush_width = 3

def draw(event):
  x = event.x
  y = event.y
  canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width), fill="Black")

def start_drawing(event):
  x = event.x 
  y = event.y

  # canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width))
  canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width), fill="black")
  canvas.bind('<B1-Motion>', draw)

canvas.bind('<Button-1>', start_drawing)

root.mainloop()

  # this is the same code as lesson 11
