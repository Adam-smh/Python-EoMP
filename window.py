from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lottery")
root.geometry("800x500")
root.config(bg="#B7094C")


class game:
    def __init__(self, window):
        self.title = Label(window, text="Good Luck!", font="sans-serif 18 bold", bg="#B7094C", fg="#FEFCFB")
        self.title.place(relx="0.28", rely="0.04")

        self.frame = Frame(window, width=700, height=380, relief="groove", borderwidth=0, bg="#A01A58")
        self.frame.place(relx="0.065", rely="0.2")

        self.head = Label(self.frame, text="How many turns would you like?", font="sans-serif 18", bg="#A01A58",
                          fg="#FEFCFB")
        self.head.place(relx="0.23", rely="0.01")

        self




game(root)
root.mainloop()
