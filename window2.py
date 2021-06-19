import smtplib
from tkinter import *
import requests
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email import validate_email
import rsaidnumber
from datetime import datetime
import uuid

# window calibration
root = Tk()
root.title("Lottery")
root.geometry("800x500")
root.config(bg="#B7094C")


class send:
    def __init__(self, window):

        with open('Database.txt', 'r') as f:
            for _line in f:
                if "Winnings" in _line:
                    self.amount = round(float(_line[9:-1]), 2)
                    print(self.amount)

        self.value = IntVar()

        self.title = Label(window, text="Please Enter Your Details", font="sans-serif 18")
        self.title.place(relx="0.3", rely="0.05")
        self.title.config(bg="#B7094C", fg="#FEFCFB")

        self.frame = Frame(window, width=700, height=400, relief="groove", borderwidth=0, bg="#A01A58")
        self.frame.place(relx="0.065", rely="0.15")

        self.bankl = Label(self.frame, text="Select Your Bank:", font="sans-serif 18", bg="#A01A58",
                           fg="#FEFCFB")
        self.bankl.place(relx="0.1", rely="0.2")

        self.options = ["Select..", "FNB", "ABSA", "Nedbank", "Standard Bank"]
        self.variable = StringVar(self.frame)
        self.variable.set(self.options[0])
        self.bank = OptionMenu(self.frame, self.variable, *self.options)
        self.bank.config(width=12, borderwidth="0", bg="#FEFCFB",
                         activebackground='#B7094C', highlightbackground="#B7094C",
                         activeforeground="#FEFCFB")
        self.bank.place(relx="0.7", rely="0.2")

        self.Name = Label(self.frame, text="Name of Recipient:", font="sans-serif 18", bg="#A01A58",
                          fg="#FEFCFB")
        self.Name.place(relx="0.1", rely="0.35")

        self.NameE = Entry(self.frame, width="20", borderwidth="0")
        self.NameE.place(relx="0.7", rely="0.36")

        self.num = Label(self.frame, text="Bank Number:", font="sans-serif 18", bg="#A01A58",
                         fg="#FEFCFB")
        self.num.place(relx="0.1", rely="0.5")

        self.numE = Entry(self.frame, width="20", borderwidth="0")
        self.numE.place(relx="0.7", rely="0.5")

        self.cur = Label(self.frame, text="Select Currency:", font="sans-serif 18", bg="#A01A58",
                         fg="#FEFCFB")
        self.cur.place(relx="0.1", rely="0.65")

        self.curE = Entry(self.frame, width="20", borderwidth="0")
        self.curE.place(relx="0.7", rely="0.65")

        self.currency = Label(self.frame, text="", font="sans-serif 18", bg="#A01A58",
                              fg="#FEFCFB")
        self.currency.place(relx="0.1", rely="0.8")
        self.currency2 = 0

        self.con = Button(self.frame, command=self.Convert, text="Convert Currency", width="12", borderwidth="0",
                          bg="#FEFCFB",
                          activebackground='#B7094C', highlightbackground="#B7094C",
                          activeforeground="#FEFCFB")
        self.con.place(relx="0.585", rely="0.8")

        self.send = Button(self.frame, command=self.Send, text="Send Email", width="12", borderwidth="0",
                           bg="#FEFCFB",
                           activebackground='#B7094C', highlightbackground="#B7094C",
                           activeforeground="#FEFCFB")
        self.send.place(relx="0.76", rely="0.8")

    def Convert(self):
        try:

            currency = requests.get("https://v6.exchangerate-api.com/v6/b8b53279722ad58c70d2a2de/latest/ZAR")
            data = currency.json()
            win = self.amount * data["conversion_rates"][self.curE.get()]

            if self.currency == "":
                messagebox.showerror()

            else:
                self.currency.config(text=round(float(win), 2))
                self.currency2 = round(float(win), 2)

        except ValueError:
            messagebox.showerror()

        except KeyError:
            messagebox.showerror("Error", "Please Enter Currency")

    def Send(self):

        with open("Database.txt", "r") as f:
            for _line in f:
                if "Email" in _line:
                    emailU = _line[7:-1]
                    print(emailU)
                if "Player ID" in _line:
                    player_id = _line[12:-1]
                    print(player_id)

        try:

            if self.variable.get() == "Select..":
                messagebox.showerror("Error", "Please Select Bank...")

            elif self.currency == "":
                messagebox.showerror("Error", "Please Enter Your preferred Currency...")

            elif self.NameE.get() == "":
                messagebox.showerror("Error", "Please Enter Name...")

            elif self.numE.get() == "":
                messagebox.showerror("Error", "Please Enter Bank Number..")

            elif self.currency2 == 0:
                messagebox.showerror("Error", "You are required to convert money into a currency of your choosing...")

            else:

                sender_email_id = 'adamafrica.dev@gmail.com'
                receiver_email_id = [emailU]
                password = 'TaxiDriver8'
                subject = "Well Done!"
                msg = MIMEMultipart()
                msg['From'] = sender_email_id
                msg['To'] = ','.join(receiver_email_id)
                msg['Subject'] = subject
                body = "Congratulations, You Have Won A Total of {} {}\n" \
                       "Please find your details below\n\n" \
                       "Your Bank: {}\n" \
                       "Account Name: {}\n" \
                       "Account Number: {}\n" \
                       "Player ID: {}\n\n" \
                       "sincerely\n" \
                       "Lotto!".format(self.currency2, self.curE.get(), self.variable.get(), self.NameE.get(), self.numE.get(),
                                       player_id)

                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s = smtplib.SMTP('smtp.gmail.com', 587)

                s.starttls()

                s.login(sender_email_id, password)

                s.sendmail(sender_email_id, receiver_email_id, text)

                s.quit()

                root.destroy()

        except ValueError:
            messagebox.showerror("brah")


send(root)
root.mainloop()
