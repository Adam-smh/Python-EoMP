from tkinter import *
from tkinter import messagebox
from random import randrange

root = Tk()
root.title("Lottery")
root.geometry("800x500")
root.config(bg="#B7094C")

random1 = randrange(1, 49)
print(random1)
random2 = randrange(1, 49)
print(random2)
random3 = randrange(1, 49)
print(random3)
random4 = randrange(1, 49)
print(random4)
random5 = randrange(1, 49)
print(random5)
random6 = randrange(1, 49)
print(random6)
lottonum = [random1, random2, random3, random4, random5, random6]
print(lottonum)


class game:
    def __init__(self, window):
        self.title = Label(window, text="Good Luck!", font="sans-serif 18 bold", bg="#B7094C", fg="#FEFCFB")
        self.title.place(relx="0.4", rely="0.04")

        self.frame = Frame(window, width=700, height=380, relief="groove", borderwidth=0, bg="#A01A58")
        self.frame.place(relx="0.065", rely="0.2")

        self.head = Label(self.frame, text="Select your lucky numbers", font="sans-serif 18", bg="#A01A58",
                          fg="#FEFCFB")
        self.head.place(relx="0.25", rely="0.01")

        self.box1 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box1.place(relx="0.1", rely="0.3")
        self.box2 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box2.place(relx="0.2", rely="0.3")
        self.box3 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box3.place(relx="0.3", rely="0.3")
        self.box4 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box4.place(relx="0.4", rely="0.3")
        self.box5 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box5.place(relx="0.5", rely="0.3")
        self.box6 = Spinbox(self.frame, borderwidth="0", width="5", from_="1", to="49")
        self.box6.place(relx="0.6", rely="0.3")

        self.enter = Button(self.frame, text="Enter", command=self.check, width="12", borderwidth="0", bg="#FEFCFB",
                            activebackground='#B7094C', highlightbackground="#B7094C",
                            activeforeground="#FEFCFB")
        self.enter.place(relx="0.8", rely="0.3")

        self.exit = Button(self.frame, command=self.exit, text="Exit", width="12", borderwidth="0", bg="#FEFCFB",
                           activebackground='#B7094C', highlightbackground="#B7094C",
                           activeforeground="#FEFCFB")
        self.exit.place(relx="0.8", rely="0.5")

        self.clear = Button(self.frame, command=self.delete, text="Clear", width="12", borderwidth="0", bg="#FEFCFB",
                            activebackground='#B7094C', highlightbackground="#B7094C",
                            activeforeground="#FEFCFB")
        self.clear.place(relx="0.8", rely="0.7")

    def delete(self):
        self.box1.delete(0, END)
        self.box2.delete(0, END)
        self.box3.delete(0, END)
        self.box4.delete(0, END)
        self.box5.delete(0, END)
        self.box6.delete(0, END)

    def exit(self):
        res = messagebox.askyesno("Wait!!", "Are you sure you would like to exit?")
        if res:
            root.destroy()

    def check(self):
        res = messagebox.askyesno("Wait!!", "Would You Like To See Your Results?")
        if res:
            self.new()

    def new(self):
        result = Toplevel()
        result.title("Results")
        result.config(bg="#B7094C")
        result.geometry("600x800")

        title = Label(result, text="Your Numbers:", font="sans-serif 14 bold", bg="#B7094C", fg="#FEFCFB")
        title.place(relx="0.4", rely="0.04")

        frame = Frame(result, width=500, height=700, relief="groove", borderwidth=0, bg="#A01A58")
        frame.place(relx="0.08", rely="0.1")

        pa = Button(window)

        Set1 = [self.box1.get(), self.box2.get(), self.box3.get(), self.box4.get(), self.box5.get(), self.box6.get()]
        print(Set1)


        # lotto1 = Label(frame, text=random1, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto1.place(relx="0.1", rely="0.1")
        #
        # lotto2 = Label(frame, text=random2, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto2.place(relx="0.2", rely="0.1")
        #
        # lotto3 = Label(frame, text=random3, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto3.place(relx="0.3", rely="0.1")
        #
        # lotto4 = Label(frame, text=random4, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto4.place(relx="0.4", rely="0.1")
        #
        # lotto5 = Label(frame, text=random5, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto5.place(relx="0.5", rely="0.1")
        #
        # lotto6 = Label(frame, text=random6, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        # lotto6.place(relx="0.6", rely="0.1")
        #
        # if int(random1) == int(self.box1.get()):
        #     lotto1.config(fg="green")
        # if int(random2) == int(self.box2.get()):
        #     lotto2.config(fg="green")



game(root)
root.mainloop()
