import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every second

# Create the main window
root = tk.Tk()
root.title('🕒 Digital Clock')
root.geometry('400x200')
root.resizable(False, False)

# Clock styling
label = tk.Label(root, font=('Arial', 50), background='black', foreground='cyan')
label.pack(anchor='center', expand=True)

time()  # Start the clock

root.mainloop()
