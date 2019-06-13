from tkinter import *
from tkinter import filedialog
from tkinter.constants import *
import platform
import os
import re

class Window(Frame):
    desktop_path = os.path.expanduser("~/Desktop")

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        
        self.file = None

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack()

        # create Menu instance 
        menu = Menu(self.master)
        self.master.config(menu=menu)

        self.init_file_menu(menu)
        self.init_edit_menu(menu)

        # main text field
        self.main_text_field = Text(self.master)
        self.main_text_field.config()
        self.main_text_field.pack(fill=BOTH, expand=1)

    def init_file_menu(self, menu_instance):
        # add upper_menu (open, save etc)
        file_menu = Menu(menu_instance)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.quit_client)
        menu_instance.add_cascade(label="File", menu=file_menu)

    def init_edit_menu(self, menu_instance):
        # add Edit menu
        edit = Menu(menu_instance)
        edit.add_command(label="Undo", command=self.undo_changes)
        edit.add_command(label="Redo", command=self.redo_changes)
        menu_instance.add_cascade(label="Edit", menu=edit)

    def open_file(self):
        print("Open file!")
        self.file = filedialog.askopenfilename(initialdir = self.desktop_path, title = "Select file", filetypes = (("TXT files","*.txt"),("all files","*.*")))
        if(self.file is not None):
            self.main_text_field.insert(END, self.read_file(self.file))

    def read_file(self, filename):
        f = open(filename)
        text = f.read()
        return text 

    def save_file(self):
        print("Save file!")

    def undo_changes(self):
        print("Undo changes!")

    def redo_changes(self):
        print("Redo changes!")

    def quit_client(self):
        exit()

root = Tk()
root.grid_columnconfigure(0, weight=1)
if(platform.system() != 'Linux'):
    root.attributes("-fullscreen", True)
else:
    root.attributes("-zoomed", True)

app = Window(root)

root.mainloop()