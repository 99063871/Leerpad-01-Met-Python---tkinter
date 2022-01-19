import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

button.config(text = "Switch light on")
window.configure(bg="black")

# schijf hier tussen je code

window.mainloop()