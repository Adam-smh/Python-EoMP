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

        self.results = []
        self.i = 0
        self.result = None

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
            self.new(self.result)

    def new(self, result_win):
        result_win = Toplevel()
        result_win.title("Entries")
        result_win.config(bg="#B7094C")
        result_win.geometry("800x500")

        title = Label(result_win, text="Your Numbers:", font="sans-serif 14 bold", bg="#B7094C", fg="#FEFCFB")
        title.place(relx="0.4", rely="0.04")

        frame = Frame(result_win, width=700, height=400, relief="groove", borderwidth=0, bg="#A01A58")
        frame.place(relx="0.08", rely="0.1")

        Set1lbl = Label(frame, text="Entries", font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        Set1lbl.place(relx="0.4", rely="0.1")

        Set1 = Label(frame, text=self.results, font="sans-serif 14 bold", bg="#A01A58", fg="#FEFCFB")
        Set1.place(relx="0.2", rely="0.2")

        btn = Button(result_win, text="exit", command=self.play_again())
        btnmain = Button(frame, text="Play Again?", command=result_win.destroy, width="12", borderwidth="0",
                         bg="#FEFCFB",
                         activebackground='#B7094C', highlightbackground="#B7094C",
                         activeforeground="#FEFCFB")
        btnmain.place(relx="0.1", rely="0.8")

        chesult = Button(frame, text="Results", command=self.realresult)
        chesult.place(relx="0.5", rely="0.9")

        if str(self.box1.get()) == str(random1):
            self.i = self.i + 1
        if str(self.box2.get()) == str(random2):
            self.i = self.i + 1
        if str(self.box3.get()) == str(random3):
            self.i = self.i + 1
        if str(self.box4.get()) == str(random4):
            self.i = self.i + 1
        if str(self.box5.get()) == str(random5):
            self.i = self.i + 1
        if str(self.box6.get()) == str(random6):
            self.i = self.i + 1
            print(self.i)

    # def chesult(self)
    #     :

    def play_again(self):
        if len(self.results) == 3:
            pass
        else:
            self.results.append([self.box1.get(), self.box2.get(), self.box3.get(), self.box4.get(), self.box5.get(),
                                 self.box6.get()])

    def realresult(self):
        root.withdraw()
        self.result.destroy()

        section = Toplevel()
        section.title("Entries")
        section.config(bg="#B7094C")
        section.geometry("800x500")

        title2 = Label(section, text="Results", font="sans-serif 14 bold", bg="#B7094C", fg="#FEFCFB")
        title2.place(relx="0.4", rely="0.04")

        frame = Frame(section, width=700, height=400, relief="groove", borderwidth=0, bg="#A01A58")
        frame.place(relx="0.06", rely="0.1")

        yournum = Label(frame, text="Your Numbers:", font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        yournum.place(relx="0.1", rely="0.2")

        num = Label(frame, text=self.results, font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        num.place(relx="0.4", rely="0.2")

        lotto = Label(frame, text="Lotto Numbers:", font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        lotto.place(relx="0.1", rely="0.3")

        num2 = Label(frame, text=lottonum, font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        num2.place(relx="0.4", rely="0.3")

        Amount_won = Label(frame, text="Amount Won:", font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        Amount_won.place(relx="0.1", rely="0.4")

        num3 = Label(frame, text="", font="sans-serif 12 bold", bg="#A01A58", fg="#FEFCFB")
        num3.place(relx="0.4", rely="0.4")

        if int(self.i) == 0:
            num3.config(text="R0")
        if int(self.i) == 1:
            num3.config(text="R0")
        if int(self.i) == 2:
            num3.config(text="R20")
        if int(self.i) == 3:
            num3.config(text="R100.50")
        if int(self.i) == 4:
            num3.config(text="R2,384")
        if int(self.i) == 5:
            num3.config(text="R8,584")
        if int(self.i) == 6:
            num3.config(text="R10,000,000")

        send = Button(frame, text="Send", command=self.send(), width="12", borderwidth="0", bg="#FEFCFB",
                      activebackground='#B7094C', highlightbackground="#B7094C",
                      activeforeground="#FEFCFB")
        send.place(relx="0.3", rely="0.8")

    def send(self):

        root.withdraw()

        section2 = Toplevel()
        section2.title("Extra Details")
        section2.config(bg="#B7094C")
        section2.geometry("800x500")

        title3 = Label(section2, font="sans-serif 14 bold", bg="#B7094C", fg="#FEFCFB")
        title3.place(relx="0.4", rely="0.04")

        frame = Frame(section2, width=700, height=400, relief="groove", borderwidth=0, bg="#A01A58")
        frame.place(relx="0.06", rely="0.1")


game(root)
root.mainloop()
