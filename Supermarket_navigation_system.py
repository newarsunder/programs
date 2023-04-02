
from tkinter import *

window = Tk()
window.geometry("1000x800")
window.title("WNS (Walmart Navigation System)")


def duplicate(double):
    if len(double) == len(set(double)):
        return False
    elif len(double) == 1:
        return False
    else:
        return True


def looping(a):
    global sum_path, path
    for i in routes.get(a):
        x.append(i)
        if i == end:
            path = []
            for k in x:
                path.append(k)
            y.append(path)
            sum_path += routes[a][i]
            dis.append(sum_path)
            sum_path -= routes[a][i]
            x.pop(-1)

        elif duplicate(x):
            x.pop(-1)
        else:
            sum_path += routes[a][i]
            looping(i)
            sum_path -= routes[a][i]

    x.pop(-1)
    return x


def matching():
    for p in y:
        check = all(item in p for item in product)
        if check:
            d = y.index(p)
            serial.append(d)
            total_dis.append(dis[d])
    return total_dis, serial


def click(text,btn):
    global initial
    initial.append(text)
    btn['bg'] = "green"
    return initial


def submit():
    global running, start, end, minimum, mini
    print(initial)
    running = True
    for i in products:
        for j in products.get(i):
            for k in initial:
                if k == j:
                    product.append(i)
    start = "a"
    end = "i"
    x.append(start)
    looping(start)
    minimum = dis.index(min(dis))
    matching()
    mini = total_dis.index(min(total_dis))
    print(min(total_dis))
    print(y[serial[mini]])
    direction()
    stops()


def stops():
    for i in products:
        for j in products.get(i):
            for k in initial:
                if j == k:
                    h = mart_map.get(i)
                    l = h[0]
                    b = h[1]
                    dot = canvas.create_oval(l-5, b-5, l+5, b+5, fill="black")


def direction():
    u = mart_map.get("a")
    for i in y[serial[mini]]:
        for j in mart_map:
            if i == "a" and j == "a":
                break
            elif i == j:
                z = mart_map.get(i)
                line = canvas.create_line(u, z, width=4, fill="green")
                u = z


def delete_circle():
    for i in products:
        for j in products.get(i):
            for k in initial:
                if j == k:
                    h = mart_map.get(i)
                    l = h[0]
                    b = h[1]
                    dot = canvas.create_oval(l-6, b-6, l+6, b+6, fill="gray64", outline="")


def delete_lines():
    u = mart_map.get("a")
    for i in y[serial[mini]]:
        for j in mart_map:
            if i == "a" and j == "a":
                break
            elif i == j:
                z = mart_map.get(i)
                line = canvas.create_line(u, z, width=10, fill="gray64")
                u = z


def reload():
    global initial, x, dis, y, path, total_dis, serial, product
    delete_circle()
    delete_lines()
    dis = []
    y = []
    path = []
    x = []
    initial = []
    total_dis = []
    serial = []
    product = []
    btn1['bg'] = "white"
    btn2['bg'] = "white"
    btn3['bg'] = "white"
    btn4['bg'] = "white"
    btn5['bg'] = "white"
    btn6['bg'] = "white"
    btn7['bg'] = "white"
    btn8['bg'] = "white"
    btn9['bg'] = "white"
    btn10['bg'] = "white"
    btn11['bg'] = "white"
    btn12['bg'] = "white"
    btn13['bg'] = "white"
    btn14['bg'] = "white"
    btn15['bg'] = "white"
    btn16['bg'] = "white"
    btn17['bg'] = "white"
    btn18['bg'] = "white"
    btn19['bg'] = "white"
    btn20['bg'] = "white"
    btn21['bg'] = "white"





# *************Variables**************
sum_path = 0
dis = []
y = []
path = []
x = []
initial = []
total_dis = []
serial = []
product = []
running = False
# *************************************


routes = {
    "a": {"b": 20,
          },
    "b": {"a": 20,
          "c": 20,
          "l": 30,
          },
    "c": {"b": 20,
          "p": 20,
          "j": 30
          },
    "d": {"d": 30,
          "e": 30,
          },
    "e": {"d": 30,
          "f": 30,
          "n": 10
          },
    "f": {"e": 30,
          "q": 30
          },
    "g": {"q": 20,
          "k": 30,
          "h": 20
          },
    "h": {"g": 20,
          "m": 30,
          "i": 20,
          },
    "j": {"c": 30,
          "n": 30
          },
    "k": {"n": 30,
          "g": 30
          },
    "l": {"b": 30,
          "o": 30
          },
    "m": {"o": 30,
          "h": 30
          },
    "n": {"k": 30,
          "g": 30,
          "e": 10,
          "o": 20
          },
    "o": {"n": 20,
          "l": 30,
          "m": 30
          },
    "p": {"c": 20,
          "d": 30
          },
    "q": {"g": 20,
          "f": 30
          }
}

products = {
    "b": ["milk", "eggs", "cheese", "curd"],
    "c": ["chicken", "beef", "pork"],
    "d": ["cake", "pastries", "bread"],
    "e": ["hammer", "nails", "screws", "screw-driver"],
    "f": ["jeans", "t-shirts", "sweaters", "jackets"],
    "g": ["toys", "kids-cloths", "kids-shoes", "comics"],
    "h": ["iron", "hairdryer", "trimmer", "mixer"],
    "j": ["crab", "fish", "sardine", "tuna"],
    "k": ["lipstick", "nail-paint", "cream", "sunscreen"],
    "l": ["chair", "bed", "sofa", "table"],
    "m": ["trainer", "sneakers", "sports", "casuals"]
}

# Coordinates for shops
mart_map = {
    "a": (100, 280),
    "b": (100, 195),
    "c": (100, 125),
    "d": (150, 55),
    "e": (300, 55),
    "f": (450, 55),
    "g": (500, 125),
    "h": (500, 195),
    "i": (500, 280),
    "j": (200, 125),
    "k": (400, 125),
    "l": (200, 195),
    "m": (400, 195),
    "n": (300, 125),
    "o": (300, 195),
    "p": (100, 55),
    "q": (500, 55)
}

# **********Shops*************
canvas = Canvas(window, width=600, height=300)
canvas.pack()
canvas.create_rectangle(0, 0, 600, 300, fill="gray64")
canvas.create_rectangle(80, 280, 120, 300, fill="red", outline="")  # Entrance
canvas.create_text(100, 290, text="In")
canvas.create_rectangle(0, 150, 80, 250, fill="lavenderblush2", outline="")
canvas.create_text(40, 200, text="Dairy")
canvas.create_rectangle(0, 40, 80, 140, fill="indianred1", outline="")
canvas.create_text(40, 90, text="Meat")
canvas.create_rectangle(90, 0, 210, 40, fill="lightsalmon", outline="")
canvas.create_text(150, 20, text="Bakery")
canvas.create_rectangle(240, 0, 360, 40, fill="seashell4", outline="")
canvas.create_text(300, 20, text="Hardware")
canvas.create_rectangle(390, 0, 510, 40, fill="thistle4", outline="")
canvas.create_text(450, 20, text="Clothing")
canvas.create_rectangle(520, 40, 600, 140, fill="deeppink", outline="")
canvas.create_text(560, 90, text="Kids")
canvas.create_rectangle(520, 150, 600, 250, fill="gold", outline="")
canvas.create_text(560, 200, text="Electronics")
canvas.create_rectangle(120, 70, 280, 110, fill="royalblue1", outline="")
canvas.create_rectangle(120, 140, 280, 160, fill="royalblue1", outline="")
canvas.create_text(200, 90, text="SeaFood")
canvas.create_rectangle(320, 70, 480, 110, fill="darkorange1", outline="")
canvas.create_rectangle(320, 140, 480, 160, fill="darkorange1", outline="")
canvas.create_text(400, 90, text="Cosmetics")
canvas.create_rectangle(120, 160, 280, 180, fill="chocolate3", outline="")
canvas.create_rectangle(120, 210, 280, 250, fill="chocolate3", outline="")
canvas.create_text(200, 230, text="Furniture")
canvas.create_rectangle(320, 160, 480, 180, fill="limegreen", outline="")
canvas.create_rectangle(320, 210, 480, 250, fill="limegreen", outline="")
canvas.create_text(400, 230, text="Shoes")
canvas.create_rectangle(480, 280, 520, 300, fill="red", outline="")  # Exit
canvas.create_text(500, 290, text="Out")

message = Label(window, text="Select Your Products")
message.pack()
# **************Buttons*************************************************************
frame1 = Frame(window)
frame1.pack()
btn1 = Button(frame1, text="Milk", width=10, height=5, command=lambda: click("milk",btn1))
btn1.grid(row=0, column=0)
btn2 = Button(frame1, text="Eggs", width=10, height=5, command=lambda: click("eggs",btn2))
btn2.grid(row=0, column=1)
btn3 = Button(frame1, text="Beef", width=10, height=5, command=lambda: click("beef",btn3))
btn3.grid(row=0, column=2)
btn4 = Button(frame1, text="Pork", width=10, height=5, command=lambda: click("pork",btn4))
btn4.grid(row=0, column=3)
btn5 = Button(frame1, text="Cake", width=10, height=5, command=lambda: click("cake",btn5))
btn5.grid(row=0, column=4)
btn6 = Button(frame1, text="Bread", width=10, height=5, command=lambda: click("bread",btn6))
btn6.grid(row=0, column=5)
btn7 = Button(frame1, text="Hammer", width=10, height=5, command=lambda: click("hammer",btn7))
btn7.grid(row=0, column=6)
btn8 = Button(frame1, text="Nails", width=10, height=5, command=lambda: click("nails",btn8))
btn8.grid(row=1, column=0)
btn9 = Button(frame1, text="Jeans", width=10, height=5, command=lambda: click("jeans",btn9))
btn9.grid(row=1, column=1)
btn10 = Button(frame1, text="Jackets", width=10, height=5, command=lambda: click("jackets",btn10))
btn10.grid(row=1, column=2)
btn11 = Button(frame1, text="Toys", width=10, height=5, command=lambda: click("toys",btn11))
btn11.grid(row=1, column=3)
btn12 = Button(frame1, text="Chair", width=10, height=5, command=lambda: click("chair",btn12))
btn12.grid(row=1, column=4)
btn13 = Button(frame1, text="lipstick", width=10, height=5, command=lambda: click("lipstick",btn13))
btn13.grid(row=1, column=5)
btn14 = Button(frame1, text="Sofa", width=10, height=5, command=lambda: click("sofa",btn14))
btn14.grid(row=1, column=6)
btn15 = Button(frame1, text="Cream", width=10, height=5, command=lambda: click("cream",btn15))
btn15.grid(row=2, column=0)
btn16 = Button(frame1, text="Iron", width=10, height=5, command=lambda: click("iron",btn16))
btn16.grid(row=2, column=1)
btn17 = Button(frame1, text="Mixer", width=10, height=5, command=lambda: click("mixer",btn17))
btn17.grid(row=2, column=2)
btn18 = Button(frame1, text="Crabs", width=10, height=5, command=lambda: click("crab",btn18))
btn18.grid(row=2, column=3)
btn19 = Button(frame1, text="Tuna", width=10, height=5, command=lambda: click("tuna",btn19))
btn19.grid(row=2, column=4)
btn20 = Button(frame1, text="Trainer", width=10, height=5, command=lambda: click("trainer",btn20))
btn20.grid(row=2, column=5)
btn21 = Button(frame1, text="Sneakers", width=10, height=5, command=lambda: click("sneakers",btn21))
btn21.grid(row=2, column=6)


frame2 = Frame(window)
frame2.pack()
btn22 = Button(frame2, text="Submit", width=10, height=5, command=submit)
btn22.grid(row=0, column=0)
btn23 = Button(frame2, text="Reload", width=10, height=5, command=reload)
btn23.grid(row=0, column=1)


window.mainloop()
