print('[LOG] Loading libraries')

from tkinter import *
from tkinter import messagebox as mb
import os

print('[LOG] Initing UI')

root = Tk()
root.title("DragonMegaHack")
root.resizable(False, False)
root.attributes("-topmost", True)
root.geometry('300x270')

print('[LOG] Initing functions')

def enresiz():
    root.resizable(True, True)

def diresiz():
    root.resizable(False, False)

def fps_bypass():
    os.system("fpsbypass\\FPSHack.exe")

def closemh():
    os.system("stopmh.bat")

def closegd():
    os.system("stopgd.bat")

def inject_dll(dll_name, enject_process):
    os.system(f"Injector.exe {dll_name} {enject_process}")

def aboutApp():
    mb.showinfo(
            "About Programm", 
            "Dragon Mega Hack By DragonTeam\nVersion: Beta 1.0")

def unlock_icons():
    os.system("unlockicons\\UnlockIcons.exe")

def practicemusichack():
    os.system("practicemusichack\\PracticeMusicHack.exe")

def cp():
    os.system("creatorhacks\\ColourPicker.exe")

def MultiScaling():
    os.system("creatorhacks\\MultiScaling.exe")

def GDPM():
    os.system("platformermode\\GDPM.exe")

print('[LOG] Initing all UI')

menubar = Menu(root)
root.config(menu=menubar)

aboutMenu = Menu(menubar, tearoff=0)
aboutMenu.add_command(label="About programm", command=aboutApp)
menubar.add_cascade(label="About", menu=aboutMenu)

settingsMenu = Menu(menubar, tearoff=0)
settingsMenu.add_command(label="Enable resizable", command=enresiz)
settingsMenu.add_command(label="Disable resizable", command=diresiz)
menubar.add_cascade(label="Settings", menu=settingsMenu)

about = Label(text="Dragon Mega Hack Beta By DragonFire")
about.pack()

fps = Button(text="FPS Bypass", command=fps_bypass)
fps.pack(side=TOP, ipadx=10)

icons = Button(text="Unlock All Icons", command=unlock_icons)
icons.pack(side=TOP, ipadx=10)

practicemusichac = Button(text="Practice Music Hack", command=practicemusichack)
practicemusichac.pack(side=TOP, ipadx=10)

practicemusichac = Button(text="Colour Picker", command=cp)
practicemusichac.pack(side=TOP, ipadx=10)

practicemusichac = Button(text="Multi Scaling", command=MultiScaling)
practicemusichac.pack(side=TOP, ipadx=10)

gdpm = Button(text="Platformer Mod", command=GDPM)
gdpm.pack(side=TOP, ipadx=10)

dll_name = Entry(width=30)
enject_process = Entry(width=30)
idll = Button(text="Inject DLL (Not working)",
             command=inject_dll(dll_name, enject_process))

dll_name.insert(0, "example.dll")
enject_process.insert(0, "GeometryDash.exe")

dll_name.pack(side=TOP, ipadx=10)
enject_process.pack(side=TOP, ipadx=10)
idll.pack(side=TOP, ipadx=10)

close = Button(text="Close Geometry Dash", command=closegd)
close.pack(side=BOTTOM, ipadx=10)

close = Button(text="Close MegaHack", command=closemh)
close.pack(side=BOTTOM, ipadx=10)

print('[LOG] Starting...')
root.mainloop()
