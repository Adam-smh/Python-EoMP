from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lottery")
root.geometry("800x500")
root.config(bg="#B7094C")


class LT:
    def __init__(self, window):
        self.Title = Label(window, text="SA Lotto!", font="sans-serif 18")
        self.Title.place(relx="0.43", rely="0.05")
        self.Title.config(bg="#B7094C", fg="#FEFCFB")

        self.frame = Frame(window, width=700, height=350, relief="groove", borderwidth=0, bg="#A01A58")
        self.frame.place(relx="0.065", rely="0.2")

        self.name = Label(self.frame, text="Name", font="sans-serif 18", bg="#A01A58", fg="#FEFCFB")
        self.name.place(relx="0.1", rely="0.1")

        self.namein = Entry(self.frame, width="30", borderwidth="0")
        self.namein.place(relx="0.5", rely="0.13")

        self.email = Label(self.frame, text="E-mail", font="sans-serif 18", bg="#A01A58", fg="#FEFCFB")
        self.email.place(relx="0.1", rely="0.3")

        self.emailin = Entry(self.frame, width="30", borderwidth="0")
        self.emailin.place(relx="0.5", rely="0.32")

        self.ID = Label(self.frame, text="ID Number", font="sans-serif 18", bg="#A01A58", fg="#FEFCFB")
        self.ID.place(relx="0.1", rely="0.5")

        self.IDin = Entry(self.frame, width="30", borderwidth="0")
        self.IDin.place(relx="0.5", rely="0.53")

        self.enter = Button(self.frame, text="Submit", width="27", borderwidth="0", bg="#FEFCFB", command=self.sub,
                            activebackground='#B7094C', highlightbackground="#B7094C",
                            activeforeground="#FEFCFB")
        self.enter.place(relx="0.5", rely="0.7")

        self.exit = Button(self.frame, text="Exit", width="12", borderwidth="0", command=self.exit, bg="#FEFCFB",
                           activebackground='#B7094C', highlightbackground="#B7094C",
                           activeforeground="#FEFCFB")
        self.exit.place(relx="0.5", rely="0.779")

        self.clear = Button(self.frame, text='Clear', width="12", borderwidth="0", command=self.delete, bg="#FEFCFB",
                            activebackground='#B7094C', highlightbackground="#B7094C",
                            activeforeground="#FEFCFB")
        self.clear.place(relx="0.671", rely="0.779")

    def sub(self):
        name = self.namein.get()
        email = self.emailin.get()
        ID = self.IDin.get()

        if len(ID) != 13:
            messagebox.showerror("blah", "blahhhhhhh")

        elif name == " ":
            messagebox.showerror("blahh")

        elif email == " ":
            messagebox.showerror("bro")

        else:
            root.destroy()
            import window

    def delete(self):
        self.namein.delete(0, END)
        self.emailin.delete(0, END)
        self.IDin.delete(0, END)

    def exit(self):
        res = messagebox.askyesno("Wait!!", "Are you sure you would like to exit?")
        if res:
            root.destroy()


LT(root)
root.mainloop()
