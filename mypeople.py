from tkinter import *
import sqlite3
from display import Display
from addpeople import Addpeople
from updatepeople import Update
from tkinter import messagebox
con =sqlite3.connect('database.db')
cur = con.cursor()
class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("My People")
        self.resizable(False,False)

        # Frame
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="RoyalBlue1")
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='5.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=100, y=10)

        self.heading = Label(self.top, text="My", font="Times 32 bold", bg="white", fg="#426ff5")
        self.heading.place(x=240, y=40)

        self.heading = Label(self.top, text="People", font="Times 32 bold", bg="white", fg="#111")
        self.heading.place(x=305, y=40)

        self.scrollbar =Scrollbar(self.bottom,orient =VERTICAL)

        self.listbox = Listbox(self.bottom,width =40, height= 27)
        self.listbox.grid(row=0,column=0,padx=(40,0))
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)



        persons = cur.execute("select * from 'addressbook1'").fetchall()
        print(persons)
        count = 0
        for person in persons:

            self.listbox.insert(count,str(person[0])+ "." +person[1] + " " + person[2])
            count +=1

        self.scrollbar.grid(row=0,column=1 ,sticky="ns")

        # buttons
        btnadd= Button(self.bottom,text = "Add", width="20" ,font="times 12 bold",bg="#0d0c0c",fg="white",command = self.add_people)
        btnadd.place(x=390,y=50)
        btnupdate = Button(self.bottom, text="Update", width="20", font="times 12 bold", bg="#0d0c0c", fg="white",command=self.update_function)
        btnupdate.place(x=390, y=120)
        btndisplay = Button(self.bottom, text="Display", width="20", font="times 12 bold", bg="#0d0c0c", fg="white",command=self.display_person)
        btndisplay.place(x=390, y=190)
        btndelete = Button(self.bottom, text="Delete", width="20", font="times 12 bold", bg="#0d0c0c", fg="white",command=self.delete_person)
        btndelete.place(x=390, y=260)
    def add_people(self):
        add_page = Addpeople()
        self.destroy()
    def update_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]


        updatepage =Update(person_id)
    def display_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        displaypage =Display(person_id )

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        query = "delete from addressbook1 where person_id='{}'".format(person_id)
        string_for_mbox = "Are you sure you wanna delete",person.split(".")[1] ,"?"
        answer = messagebox.askquestion("Warning!","Are you sure you wanna delete ?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success", "Deleted")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info",str(e))


