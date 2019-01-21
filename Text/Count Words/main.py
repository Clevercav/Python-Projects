from tkinter import Tk, Label, Button, Entry, filedialog, Text
from tkinter.constants import *
import os
import re

class CountWordsGUI:
    text = ""
    desktop_path = os.path.expanduser("~/Desktop")
    amount_of_words_label = "Amount of words:"
    introduction = """
        1. Open file or type directly in the text field
        2. Press the count button
        3. Profit
    """
    def __init__(self, master):
        self.master = master
        master.title("Count words")

        # Introduction
        self.introduction_label = Label(master, text=self.introduction, justify=LEFT)
        self.introduction_label.pack()

        # Open file
        self.open_file_button = Button(master, text="Open file", command=self.open_file_dialog)
        self.open_file_button.pack(fill=X)

        # Input
        self.input = Text(master, height=5)
        self.input.pack()

        # Count button
        self.count_button = Button(master, text="Count", command=self.count_words)
        self.count_button.pack(fill=X)

        # Output
        self.output = Label(master, text=self.amount_of_words_label)
        self.output.pack(fill=X)

    def count_words(self):
        input_text = self.input.get(0.0, END)
        match_words_regex = r'\b\w+\b'
        words = re.findall(match_words_regex, input_text)
        words_amount = len(words)
        # Output result
        self.output.config(text='{} {}'.format(self.amount_of_words_label, words_amount))

    def open_file_dialog(self):
        file = filedialog.askopenfilename(initialdir = self.desktop_path, title = "Select file", filetypes = (("TXT files","*.txt"),("all files","*.*")))
        if file != '':
            self.input.insert(END, self.get_text_from_file(file))

    def get_text_from_file(self, filename):
        f = open(filename)
        text = f.read()
        return text

root = Tk()
root.geometry("500x300")
my_gui = CountWordsGUI(root)
root.mainloop()
