from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("hamza")

hamza = Label(root, text="hamza good")
hamza.pack(side="left")

def click():
    label1 = Label(root, text="python gui first", bg="blue", padx=50, pady=25)
    label1.pack()
    print("Label text:", label1.cget("text"))

but = Button(root, text="button", bg="green", width=15, command=click)
but.pack(padx=50, pady=100)
label
root.mainloop()
