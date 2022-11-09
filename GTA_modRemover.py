import shutil
import os
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x250")

second = Toplevel()
second.title("Child Window")
second.geometry("400x100")
second.withdraw()

f = open("var.txt", "a+")
print(f.read())
if os. path. getsize('var.txt') == 0:
    second.deiconify()
    window.withdraw()
f.close()
name_var = tk.StringVar()


def submit():
    f = open("var.txt", "a+")
    f.write(name_var.get())
    f.close()
    window.deiconify()
    second.destroy()
    try:
        os.mkdir(os.path.normpath(name_var.get()+"\\badFiles"))
    except OSError as error:
        pass


def run():
    f = open("var.txt","r")
    path = f.readlines()[0]
    f.close()
    source = path+"\\{}"
    destination = path+"\\badfiles\\{}"
    print(source)
    if source == "nil":
        print("error")
        return
    enteries = os.listdir(path)
    goodfiles = ['.egstore', 'badFiles', 'bink2w64.dll', 'Changelog.txt', 'common.rpf', 'd3dcompiler_46.dll',
                 'd3dcsx_46.dll', 'EOSSDK-Win64-Shipping.dll', 'GFSDK_ShadowLib.win64.dll', 'GFSDK_TXAA.win64.dll',
                 'GFSDK_TXAA_AlphaResolve.win64.dll', 'GPUPerfAPIDX11-x64.dll', 'GTA5.exe', 'PlayGTAV.exe', 'ReadMe',
                 'Redistributables', 'update', 'version.txt', 'x64', 'x64a.rpf', 'x64b.rpf', 'x64c.rpf', 'x64d.rpf',
                 'x64e.rpf', 'x64f.rpf', 'x64g.rpf', 'x64h.rpf', 'x64i.rpf', 'x64j.rpf', 'x64k.rpf', 'x64l.rpf',
                 'x64m.rpf', 'x64n.rpf', 'x64o.rpf', 'x64p.rpf', 'x64q.rpf', 'x64r.rpf', 'x64s.rpf', 'x64t.rpf',
                 'x64u.rpf', 'x64v.rpf', 'x64w.rpf']

    for i in enteries:
        if i not in goodfiles:
            file = i
            try:
                shutil.move(source.format(file), destination.format(file))
            except FileNotFoundError as fnfe:
                print(fnfe)


def move():
    f = open("var.txt", "r")
    path = f.readlines()[0]
    f.close()
    source = path + "\\{}"
    destination = path + "\\badfiles\\{}"
    enteries = os.listdir(path+"\\badFiles")

    for i in enteries:
        try:
            shutil.move(destination.format(i), source.format(i))
        except FileNotFoundError as fnfe:
            print(fnfe)


path_label = tk.Label(second, text='Enter GTAV path: ', font=('calibre', 10, 'bold'))
path_entry = tk.Entry(second, textvariable=name_var, font=('calibre', 10, 'normal'), width="50")
path_label.pack()
path_entry.pack()

gap = tk.Label(second, width="20", height="1")
gap.pack()

remove = tk.Button(second, text="Submit", width="10", height="2", border="0", background="#82CD47", foreground="#fff", command=submit)
remove.pack()


remove = tk.Button(window, text="Remove", width="20", height="5", border="0", background="#171717", foreground="#fff", command=run)
remove.pack()

gap = tk.Label(window, width="20", height="1")
gap.pack()

add = tk.Button(window, text="Add", width="20", height="5", border="0", background="#171717", foreground="#fff", command=move)
add.pack()


window.mainloop()
