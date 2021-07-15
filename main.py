from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import Addpeople
from Aboutus import About

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self,master):
        self.master =master



        # frame
        self.top =Frame(master, height =150 , bg="white")
        self.top.pack(fill =X)

        self.bottom = Frame(master, height=500, bg="RoyalBlue1")
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file = '4.png')
        self.top_image_label = Label(self.top,image = self.top_image,bg="white")
        self.top_image_label.place(x=100,y=10)

        self.heading =Label(self.top,text="PhoneBook",font="Times 26 bold",bg="white",fg = "#426ff5")
        self.heading.place(x=220,y=40)

        self.heading = Label(self.top, text="App", font="Times 26 bold", bg="white", fg="#111")
        self.heading.place(x=400, y=40)

        # date
        self.date_label = Label(self.top,text="Date: "+date, font="times 12 bold",fg="#111",bg="white")
        self.date_label.place(x=520,y=5)


        # button1 view People
        self.viewbtn =Button(self.bottom, text ="My People" ,font="times 12 bold",width ="20",bg="RoyalBlue3",fg="white",command=self.my_people)
        self.viewbtn.place(x=250,y=40)
        self.bottom_image = PhotoImage(file='5.1.png')
        self.bottom_image_label = Label(self.bottom, image=self.bottom_image,bg="RoyalBlue1")
        self.bottom_image_label.place(x=180, y=30)

        # button2 add People
        self.addpeople = Button(self.bottom, text="Add People", font="times 12 bold", width="20",bg="RoyalBlue3",fg="white",command = self.addpeoplefunction)
        self.addpeople.place(x=250, y=180)
        self.bottom_image1 = PhotoImage(file='6.1.png')
        self.bottom_image1_label = Label(self.bottom, image=self.bottom_image1, bg="RoyalBlue1")
        self.bottom_image1_label.place(x=180, y=170)



        # button3 about us
        self.aboutus = Button(self.bottom, text="About Us", font="times 12 bold", width="20",bg="RoyalBlue3",fg="white",command = self.about_us)
        self.aboutus.place(x=250, y=290)
        self.bottom_image2 = PhotoImage(file='8.1.png')
        self.bottom_image2_label = Label(self.bottom, image=self.bottom_image2, bg="RoyalBlue1")
        self.bottom_image2_label.place(x=180, y=280)

    def my_people(self):
        people = Mypeople()
    def addpeoplefunction(self):
        addpeoplewindow = Addpeople()
    def about_us(self):
        about_page= About()
def main():
    root=Tk()
    app= Application(root)
    root.title("PhoneBook")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()


if __name__== '__main__':
 main()