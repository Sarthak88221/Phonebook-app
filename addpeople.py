from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

class Addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("Add New Person")
        self.resizable(False,False)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="RoyalBlue1")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='6.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=100, y=10)

        self.heading = Label(self.top, text="Add", font="Times 32 bold", bg="white", fg="#426ff5")
        self.heading.place(x=240, y=40)

        self.heading = Label(self.top, text="New Person", font="Times 32 bold", bg="white", fg="#111")
        self.heading.place(x=320, y=40)


        #name
        self.label_name=Label(self.bottom, text="Name:", font="Times 15 bold",bg='RoyalBlue1' ,fg="#111")
        self.label_name.place(x=40,y=40)
        self.entry_name = Entry(self.bottom,width=30,bd=2)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=200,y=44)


        #Surname
        self.label_surname = Label(self.bottom, text="Surname:", font="Times 15 bold", bg='RoyalBlue1', fg="#111")
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottom, width=30, bd=2)
        self.entry_surname.insert(0, "Enter Surname")
        self.entry_surname.place(x=200, y=84)

        #email
        self.label_email= Label(self.bottom, text="Email:", font="Times 15 bold", bg='RoyalBlue1', fg="#111")
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottom, width=30, bd=2)
        self.entry_email.insert(0, "Enter Email")
        self.entry_email.place(x=200, y=124)

        #Phone_number
        self.label_phone = Label(self.bottom, text="Phone Number:", font="Times 15 bold", bg='RoyalBlue1', fg="#111")
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottom, width=30, bd=2)
        self.entry_phone.insert(0, "Enter Phone Number")
        self.entry_phone.place(x=200, y=164)

        #address
        self.label_address = Label(self.bottom, text="Address:", font="Times 15 bold", bg='RoyalBlue1', fg="#111")
        self.label_address.place(x=40, y=200)
        self.entry_address = Text(self.bottom, width=22, bd=2,height=6)

        self.entry_address.place(x=200, y=204)

        #button
        button =Button(self.bottom,text="Add Person",bg="black",fg="white",width=25, font="Times 10 ",command=self.add_people)
        button.place(x=200,y=320)


    #Getting input data from the user
    def add_people(self):
        name = self.entry_name.get()
        surname= self.entry_surname.get()
        email = self.entry_email.get()
        phone =self.entry_phone.get()
        address= self.entry_address.get(1.0,'end-1c')

        if name and surname and email and phone and address !="":
            try:

                #add to database
                query = 'insert into addressbook1 (person_name,person_surname, person_email,person_phone,person_address)' 'VALUES (?,?,?,?,?)'
                cur.execute(query, (name,surname,phone,email,address))
                con.commit()
                messagebox.showinfo("Success","Person is added")
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","Fill all the fields", icon ='warning')

