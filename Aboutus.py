from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("About Us")
        self.resizable(False,False)
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="RoyalBlue1")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='8.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=110, y=10)

        self.heading = Label(self.top, text="About", font="Times 32 bold", bg="white", fg="#426ff5")
        self.heading.place(x=240, y=40)

        self.heading = Label(self.top, text="Us", font="Times 32 bold", bg="white", fg="#111")
        self.heading.place(x=360, y=40)


        # Content
        self.text = Label(self.bottom, text=
                          'Phonebook allows you to upload your plain text contact file from your'
                          '\n\ncomputer, and search your contact.  Its designed for people who'
                          '\n\nlikes to keep all their contacts in a text file.The contact file format'
                          '\n\nis very flexible and its documented on. It allow the user to add '
                          '\n\npeople, Update,Display, Delete an existing contact',
                          font="Times 15 bold", bg='RoyalBlue1', fg="#111")
        self.text.place(x=10, y=40)
        # "Phonebook allows you to upload your plain text contact file from your computer, and search contact onyour phone. It's designed for people who likes to keep all their contacts in a text file.The contact file format is very flexible and it's documented on.It allow the user to Update,Display, Delete an existing contact


