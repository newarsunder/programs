import tkinter as tk
import pyqrcode
from PIL import Image, ImageTk


window = tk.Tk()
window.title("QR Code Generator")
window.geometry("300x300")

color = '#DD5353'
window.configure(bg=color)


def run():
    url = pyqrcode.create(t.get())
    url.png('myqr.png',scale=5)
    load = Image.open("myqr.png")
    v = ImageTk.PhotoImage(file="myqr.png")
    img.configure(image=v)
    img.image = v

t = tk.StringVar()
txt = tk.Label(window, text="Enter text", bg=color, font='Georgia 10', width=10, height=3).pack()
enter = tk.Entry(window, textvariable=t, font='Georgia 15').pack()
b = tk.Label(window, bg=color).pack()
btn = tk.Button(window, text="Submit", fg="#fff", bg="#FA7070", height=2, width=10, relief='flat', command=run).pack()
b = tk.Label(window, bg=color).pack()
img = tk.Label(window, bg=color)
img.pack()
window.mainloop()
