import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Hello,, Tkinter!", fg="blue", bg="yellow", padx=100,pady=50)
label.pack()

button = tk.Button(window, text="Click Me", width=15, command=lambda:
print("Button clicked!"))
button.pack()
current_text = label.cget("text") # Using cget()
print("Current text: {current_text}")
current_bg = label.config()["bg"][-1] # Using config() and dictionary access
print("Current background: {current_bg}")
window.mainloop()

window.mainloop()