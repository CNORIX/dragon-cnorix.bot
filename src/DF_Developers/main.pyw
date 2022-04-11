import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label
import sys
import os
import tkinterweb
import webbrowser

def open_publish_page():
	publishPage = Tk()
	publishPage.title(f'Publish app | DragonStore')
	frame = tkinterweb.HtmlFrame(publishPage, messages_enabled = False)
	frame.load_website("http://dragonstore.7m.pl/en/publish/publish.html")
	frame.pack(fill="both", expand=True)
	publishPage.mainloop()

def open_cyberforum_page():
	cyberforum = Tk()
	cyberforum.title(f'CyberForum.ru')
	frame = tkinterweb.HtmlFrame(cyberforum, messages_enabled = False)
	frame.load_website("https://www.cyberforum.ru/")
	frame.pack(fill="both", expand=True)
	cyberforum.mainloop()

def hotkeys_window():
	hotkeys = Tk()
	hotkeys.geometry("700x300")
	hotkeys.resizable(width = False, height = False)
	hotkeys.title(f'Hotkeys')

	enfs = Label(hotkeys, text = f'F11 - Enable Fullscreen')
	enfs.grid(column=0, row=0)

	dufs = Label(hotkeys, text = f'F12 - Disable Fullscreen')
	dufs.grid(column=0, row=1)

	hotkeys.mainloop()

root = Tk()
root.geometry("700x300")
root.resizable(width = False, height = False)
root.title(f'DragonFire Developer Portal')

mainmenu = Menu(root)
root.config(menu = mainmenu)

file = Menu(mainmenu, tearoff = 0)
projectmenu = Menu(mainmenu, tearoff = 0)
devPortals = Menu(mainmenu, tearoff = 0)
forums = Menu(mainmenu, tearoff = 0)
about = Menu(mainmenu, tearoff = 0)

file.add_command(label = "Hotkeys", activebackground = 'black', command = lambda: hotkeys_window())
file.add_command(label = "Exit", activebackground = 'black', command = lambda: sys.exit(1))

projectmenu.add_command(label = "Publish application in DragonStore", activebackground = 'black', command = lambda: open_publish_page())
projectmenu.add_command(label = "Edit project file", activebackground = 'black', command = lambda: os.system("notepad project.dfproj.json"))

devPortals.add_command(label = "Discord developers", activebackground = 'black', command = lambda: webbrowser.open(url = "https://discord.com/developers/applications"))
devPortals.add_command(label = "GitHub", activebackground = 'black', command = lambda: webbrowser.open(url = "https://github.com"))

forums.add_command(label = "Stack Overflow (English)", activebackground = 'black', command = lambda: webbrowser.open(url = "https://stackoverflow.com"))
forums.add_command(label = "CyberForum (Russian)", activebackground = 'black', command = lambda: open_cyberforum_page())

about.add_command(label = "DragonFire Developer Portal", activebackground = 'black')
about.add_command(label = "By DragonFire", activebackground = 'black')
about.add_command(label = "Powered by Python", activebackground = 'black')

mainmenu.add_cascade(label = "File", menu = file)
mainmenu.add_cascade(label = "Project", menu = projectmenu)
mainmenu.add_cascade(label = "Other developer portals", menu = devPortals)
mainmenu.add_cascade(label = "Forums", menu = forums)
mainmenu.add_cascade(label = "About", menu = about)

textm = Label(text = f'DragonFire Developer Portal')
textm.grid(column=0, row=0)

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

root.mainloop()