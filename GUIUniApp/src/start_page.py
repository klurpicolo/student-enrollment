import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class StartPage(tk.Frame):
    def __init__(self, parent, *args):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="GUIUniApp", font=LARGEFONT)
        label.pack()

        select_label = ttk.Label(self, text="Select student or admin page", font=("Verdana", 12))
        select_label.pack()

    def re_render(self):
        pass
