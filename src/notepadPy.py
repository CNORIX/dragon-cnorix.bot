import tkinter
from tkinter import *

root = Tk()
root.title("DragonTextEditor")

mainmenu = Menu(root)
root.config(menu = mainmenu)

text = Text(width=1280, height=720, bg="gray")
text.pack(side=LEFT)

def about():
    label = Label(text="About NotepadPy", bg="green")
    text.window_create(INSERT, window=label)

    label = Label(text="Version 1.0", bg="green")
    text.window_create(INSERT, window=label)

def make_print():
    text.insert(1.0, "print(f'')")

def make_defWithArg():
    text.insert(1.0, "def function(arg1, arg2):\n")
    text.insert(2.0, "    # your code here")

def make_class():
    text.insert(1.0, "class ClassName(args):\n")
    text.insert(2.0, "    def __init__(args):\n")
    text.insert(3.0, "        # Init commands here\n")
    text.insert(4.0, "    def JustAFunction(user):\n")
    text.insert(5.0, "        print(f'Hello { user }')")

npmenu = Menu(mainmenu, tearoff=0)
npmenu.add_command(label="About", command=about)
npmenu.add_command(label="Exit")

codeBlocks = Menu(mainmenu, tearoff=0)
codeBlocks.add_command(label="print()", command=make_print)
codeBlocks.add_command(label="def(arg):", command=make_defWithArg)
codeBlocks.add_command(label="class(arg):", command=make_class)

mainmenu.add_cascade(label="NotepadPy", menu=npmenu)
mainmenu.add_cascade(label="Code Blocks", menu=codeBlocks)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()