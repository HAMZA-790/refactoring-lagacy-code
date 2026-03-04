# #/from tkinter import *
#
# root = Tk()
# root.geometry("300x300")
# root.title("Color Change Button")
#
#
# current_color = "green"
#
# def change_color():
#     global current_color
#
#     if current_color == "green":
#         current_color = "blue"
#     elif current_color == "blue":
#         current_color = "red"
#     elif current_color == "red":
#         current_color = "yellow"
#     else:
#         current_color = "green"
#
#     btn.config(bg=current_color)
#
# btn = Button(root, text="Click Me", width=20, height=2, bg=current_color, command=change_color)
# btn.pack(pady=100)
#
# |root.mainloop()#/?

from tkinter import *

root = Tk()
root.geometry("300x300")

def change_color():
    current =  btn.cget("bg")

    if current == "green":
        btn.config(bg="red")
    elif current == "red":
        btn.config(bg="blue")
    elif current == "blue":
        btn.config(bg="yellow")
    else:
        btn.config(bg="green")

btn = Button(root, text="Click Me", bg="green", width=20, command=change_color)
btn.pack(pady=100)

root.mainloop()
