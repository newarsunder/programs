from tkinter import *
import time

root = Tk()
root.configure(bg="#151D3B")
root.geometry("400x640+1000+80")


def click(n, btn):
    btn.configure(bg="#6EBF8B")
    x = int(canvas.coords(elev)[1])
    current_floor = (x - 2) // 100
    val = 0
    if current_floor-n < 0:
        val = 1
    elif current_floor-n > 0:
        val = -1
    for i in range(abs(current_floor-n)):
        root.update()
        time.sleep(1)
        canvas.move(elev, 0, val*100)

    btn.configure(bg="white")


text = Label(root, text="ELEVATOR", bg="#151D3B", fg="#DADBBD")
text.pack()
pos = 4
canvas = Canvas(root, width=50, height=498)
canvas.pack()
elev = canvas.create_rectangle(2, 100*pos+2, 98, 100*pos+98, outline="#D82148", fill="#D82148")

fourth = Label(root, bg="#151D3B")
fourth.place(x=300, y=50)
b4 = Button(fourth, text="o", bg="white", bd=0, command=lambda: click(0, b4))
b4.pack()

third = Label(root, bg="#151D3B")
third.place(x=300, y=150)
b3 = Button(third, text="o", bg="white", bd=0, command=lambda: click(1, b3))
b3.pack()

second = Label(root, bg="#151D3B")
second.place(x=300, y=250)
b2 = Button(second, text="o", bg="white", bd=0, command=lambda: click(2, b2))
b2.pack()

first = Label(root, bg="#151D3B")
first.place(x=300, y=350)
b1 = Button(first, text="o", bg="white", bd=0, command=lambda: click(3, b1))
b1.pack()

ground = Label(root, bg="#151D3B")
ground.place(x=300, y=450)
b0 = Button(ground, text="o", bg="white", bd=0, command=lambda: click(4, b0))
b0.pack()

keypad = Label(root, bg="#151D3B")
keypad.pack()
bt4 = Button(keypad, text="4", bd=0, command=lambda: click(0, bt4))
bt4.grid(row=0, column=0, pady=10)
bt3 = Button(keypad, text="3", bd=0, command=lambda: click(1, bt3))
bt3.grid(row=0, column=2)
bt2 = Button(keypad, text="2", bd=0, command=lambda: click(2, bt2))
bt2.grid(row=1, column=0, pady=10)
bt1 = Button(keypad, text="1", bd=0, command=lambda: click(3, bt1))
bt1.grid(row=1, column=2)
bt0 = Button(keypad, text="G", bd=0, command=lambda: click(4, bt0))
bt0.grid(row=2, column=1, pady=10)

root.mainloop()
