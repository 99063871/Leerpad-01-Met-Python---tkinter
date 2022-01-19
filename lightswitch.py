import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
def lightSwitch():
    button.config(text = "Switch light off")
    window.configure(bg="yellow")

button.config(text = "Switch light on")
button.config(command=lightSwitch)
window.configure(bg="black")

# schijf hier tussen je code

window.mainloop()