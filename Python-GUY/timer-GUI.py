import tkinter as tk
import time 

class TimerApp:
  def __init__(self, master):
    self.master = master 
    master.title = ("Timer App")

    self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
    self.label.pack()

    self.start_button = tk.Button(master, text="Start", command=self.start_timer)
    self.start_button.pack()

    self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
    self.stop_button.pack()
    self.stop_button.config(state="disabled")

    self.running = False
    self.start_time = None

  def start_timer(self):
    if not self.running: 
      self.running = True 
      self.start_button.config(state="disabled")
      self.stop_button.config(state="normal")
      self.start_time = time.time()
      self.update_timer()

  def stop_timer(self):
    if self.running:
      self.running = False
      self.start_button.config(state="normal")
      self.stop_button.config(state="disabled")
  
  def update_timer(self):
    if self.running:
      elapsed_time = time.time() - self.start_time 
      hours, remainder = divmod(elapsed_time, 3600)
      minutes, seconds = divmod(remainder, 60)
      time_str = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
      self.label.config(text=time_str)
      self.master.after(1000, self.update_timer)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()

