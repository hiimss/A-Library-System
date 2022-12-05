from re import M
from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import messagebox
import pymysql
from datetime import datetime
from datetime import timedelta



#Connect to librarysystem database

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="PlaceholderPassword",
  database="librarysystem"
)

#Create Cursor
mycursor = mydb.cursor()

LARGEFONT = ("Verdana",15)
MAINMENUFONT = ("Verdana", 20)
NORMALFONT = ("Helvetica",10)
class MainFrame(tk.Tk) :
    '''
    Frame object holding all our different pages
    '''
    #__init__ function for class tkinterApp
    def __init__(self, *args, **kwargs) :

        #__init__ function for class Tk
        tk.Tk.__init__(self, *args, *kwargs)

        #Creating a container
        container = tk.Frame(self)
        container.pack(side= "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Initializing frames to an empty array
        self.frames = {}

        #Iterating through a tuple consisting of the different page layouts
        for F in (MainMenu, Members_Page, Books_Page, Loans_Page, Reservation_Page, Fines_Page, Reports_Page, Creation_Page, Deletion_Page, Update_Page, \
            Acquisition_Page, Withdrawal_Page, Borrow_Page, Return_Page, Reserve_Page, CancelReserve_Page, FinePayment_Page, BookSearch_Page, BookOnLoan_Page, \
                BookOnReservation_Page, OutstandingFine_Page, BookOnLoanToMember_Page):

            frame = F(container, self)

            #Initialize frame of the object from startpage, page1, page2 respectively with for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(MainMenu)


    #Displays the current frame passed as a parameter
    def show_frame(self, cont) :
        frame = self.frames[cont]
        frame.tkraise()

#FIRST FRAME MAIN MENU
class MainMenu(tk.Frame): 
    def __init__(self, parent, controller): 

        tk.Frame.__init__(self, parent) 
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Label of the frame and putting in place.
        label = Label(self, text = "ALS Main Menu", font = MAINMENUFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, pady = (30,0))

        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, pady= 10)

        #Creation of the 6 Buttons [ Membership, Books, Loans, Reservations, Fines, Reports ] 
        # [ Members_Page, Books_Page, Loans_Page, Reservation_Page, Fines_Page, Reports_Page]

         #Membership_button
        Membership_button = Button(self, text = "Membership", command = lambda : controller.show_frame(Members_Page), font = NORMALFONT)
        Membership_button.grid(row = 2, column = 0, pady = 30, sticky = "S")

        #Book_button
        Book_button = Button(self, text = "Books", command = lambda : controller.show_frame(Books_Page),font = NORMALFONT)
        Book_button.grid(row = 2, column = 1, pady = 30, sticky = "S")

        #Loan_button
        Loan_button = Button(self, text = "Loans", command = lambda : controller.show_frame(Loans_Page), font = NORMALFONT)
        Loan_button.grid(row = 2, column = 2, pady = 30, sticky = "S")
        
        #Reservation_button
        Reservation_button = Button(self, text = "Reservations", command = lambda : controller.show_frame(Reservation_Page), font = NORMALFONT)
        Reservation_button.grid(row = 3, column = 0, pady = 30, sticky = "S")

        #Fines_button
        Fines_button = Button(self, text = "Fines", command = lambda : controller.show_frame(Fines_Page), font = NORMALFONT)
        Fines_button.grid(row = 3, column = 1, pady = 30, sticky = "S")
       
        #Reports_button
        Reports_button = Button(self, text = "Reports", command = lambda : controller.show_frame(Reports_Page), font = NORMALFONT)
        Reports_button.grid(row = 3, column = 2, pady = 30, sticky = "S")

class Members_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Membership", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))

        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #4 Buttons on this Page [ Creation, Deletion, Update, BackToMain ]
        # [ Creation_Page, Deletion_Page, Update_Page ]

        #Creation_button
        Creation_button = Button(self, text = "Creation", command = lambda : controller.show_frame(Creation_Page),font = NORMALFONT)
        Creation_button.grid(row = 2, column = 0, pady = 10, sticky = "S")

        #Deletion_button
        Deletion_button = Button(self, text = "Deletion", command = lambda : controller.show_frame(Deletion_Page),font = NORMALFONT)
        Deletion_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        #Update_button
        Update_button = Button(self, text = "Update", command = lambda : controller.show_frame(Update_Page),font = NORMALFONT)
        Update_button.grid(row = 4, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu),font = NORMALFONT)
        BackToMain_button.grid(row = 5, column = 0, pady = 10, sticky = "S")

class Creation_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Membership Creation", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, pady = (30,0))

        label2 = Label(self, text = "To Create Member, Please Enter Requested Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, pady= 10)

        #Creating Textbox to enter Member row
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 2, column = 1, sticky = S, pady = 3)

        f_name = Entry(self, width = 30)
        f_name.grid(row = 3, column = 1, sticky = S, pady = 3)

        l_name = Entry(self, width = 30)
        l_name.grid(row = 4, column = 1, sticky = S, pady = 3)

        faculty = Entry(self, width = 30)
        faculty.grid(row = 5, column = 1, sticky = S, pady = 3)

        phone = Entry(self, width = 30)
        phone.grid(row = 6, column = 1, sticky = S, pady = 3)

        email = Entry(self, width = 30)
        email.grid(row = 7, column = 1, sticky = S, pady = 3)
        
        #Creating Textbox Labels
        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 2, column = 0, sticky = E)

        f_name_label = Label(self, text = "First Name:", background = "#856ff8", fg = "#fff") 
        f_name_label.grid(row = 3, column = 0,  sticky = E)

        l_name_label = Label(self, text = "Last Name:", background = "#856ff8", fg = "#fff") 
        l_name_label.grid(row = 4, column = 0, sticky = E)

        faculty_label = Label(self, text = "Faculty:", background = "#856ff8", fg = "#fff") 
        faculty_label.grid(row = 5, column = 0, sticky = E)

        phone_label = Label(self, text = "Phone Number:", background = "#856ff8", fg = "#fff") 
        phone_label.grid(row = 6, column = 0, sticky = E)

        email_label = Label(self, text = "Email Address:", background = "#856ff8", fg = "#fff") 
        email_label.grid(row = 7, column = 0, sticky = E)

        #BackToMembers_Page
        BackToMain_button = Button(self, text = "Back To Membership Menu", command = lambda : controller.show_frame(Members_Page))
        BackToMain_button.grid(row = 9, column = 1, pady = 10, sticky = S)

        #Create submit Button 
        def addMember(): 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            member_insert = memberID.get()
            f_name_insert = f_name.get()
            l_name_insert = l_name.get()
            faculty_insert = faculty.get()
            phone_insert = phone.get()
            email_insert = email.get()
            fine_amount_insert = 0

            if member_insert == "" or f_name_insert == "" or faculty_insert == "" or phone_insert == "" or email_insert == "" : 
                    messagebox.showerror(title = "Error", message = "Missing or Incomplete Fields")
            
            else : 
                data = (member_insert, f_name_insert, l_name_insert, faculty_insert, phone_insert, email_insert, fine_amount_insert)
                addmember_query = """INSERT INTO member (memberID, fName, lName, faculty, phone, eMail, fineAmount) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

                try :
                    with mycursor:  
                        mycursor.execute(addmember_query,data)
                        messagebox.showinfo(title = "Success!", message = "ALS Membership created.")
                        

                except pymysql.err.IntegrityError : 
                    #Produce a popup
                    messagebox.showerror(title = "Error!", message = "Member already exists; Missing or incomplete fields.")

                #commit
                mydb.commit()

                #Temporary clear the textboxes
                memberID.delete(0,END) 
                f_name.delete(0,END) 
                l_name.delete(0,END) 
                faculty.delete(0,END) 
                phone.delete(0,END) 
                email.delete(0,END) 

                #close connection
                mydb.close() 

        addMember_btn = Button(self, text = "Create Member", command = addMember)
        addMember_btn.grid(row = 8, column = 1, pady = 10, sticky = "S")

class Deletion_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Membership Deletion", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))

        label2 = Label(self, text = "To Delete Member, Please Enter Membership ID", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #TextBox to enter MemberID to delete
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 2, column = 1, pady = 3, sticky = "S")

        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 2, column = 0, sticky = "E")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            member_delete = memberID.get()
            data = (member_delete,)
            
            memberDetails_query = """ SELECT fname, lname, faculty, phone, eMail FROM member WHERE memberID = %s"""
            mycursor.execute(memberDetails_query, memberID.get())
            records = mycursor.fetchall()
            
            if data[0] == "":
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            elif len(records) == 0:
                messagebox.showerror(title = "Error!", message = "Member does not exist.")
            else:
                FineAmount_query = """ SELECT fineAmount FROM member WHERE memberID = %s"""
                mycursor.execute(FineAmount_query,data)
                records1 = mycursor.fetchall()
                fineAmount = int(records1[0][0])
                #print(fineAmount)

                #get books currently borrowed
                BooksBorrowed_query = """ SELECT COUNT(memberID) as NumberBooksBorrowed FROM Book WHERE memberID = %s"""
                mycursor.execute(BooksBorrowed_query, data)
                records2 = mycursor.fetchall()
                BooksBorrowed = int(records2[0][0])
                #print(BooksBorrowed)

                #get books on reserve
                BooksReserve_query = """ SELECT COUNT(memberID) as NumberReservationsMade FROM bookHasReservation WHERE memberID = %s;"""
                mycursor.execute(BooksReserve_query, data)
                records3 = mycursor.fetchall()
                BooksReserved = int(records3[0][0])
                #print(BooksReserved)

                if fineAmount > 0 or BooksBorrowed > 0 or BooksReserved > 0 :
                    messagebox.showerror(title = "Error!", message = "Member has outstanding loans, reservations or fines.")
                else:
                    #Creating popup window
                    popup = Tk()
                    popup.title("Member Details")
                    popup.geometry("500x500")
                    popup.config(background = "#856ff8")

                    popup_label =  Label(popup, text = "Please Confirm Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                    popup_label.pack(pady=10)

                    memberDetails = records[0]
                    faculty = memberDetails[2]
                    phoneNumber = memberDetails[3]
                    eMail = memberDetails[4]
                    name = memberDetails[0] 
                    if memberDetails[1] != None:
                        name += (" " + memberDetails[1])
                
                    #Showing member data
                    memberID_label =  Label(popup, text = "Member ID: " + memberID.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                    memberID_label.pack(pady=10)

                    name_label =  Label(popup, text = "Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                    name_label.pack(pady=10)

                    faculty_label =  Label(popup, text = "Faculty: " + faculty, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                    faculty_label.pack(pady=10)

                    phoneNumber_label =  Label(popup, text = "Phone Number: " + phoneNumber, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                    phoneNumber_label.pack(pady=10)

                    eMail_label =  Label(popup, text = "Email Address: " + eMail, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                    eMail_label.pack(pady=10) 

                    #Creating buttons
                    confirmDeletion_btn = Button(popup, text = "Confirm Deletion", command = lambda : deleteMember(popup))
                    confirmDeletion_btn.pack(pady=10)

                    BackToDelete_btn = Button(popup, text = "Back to Delete Function", command = lambda : popup.destroy())
                    BackToDelete_btn.pack(pady=10)
                
                    popup.mainloop()

        def deleteMember(popup) : 
             #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            member_delete = memberID.get()
            data = (member_delete,)

            class FineorBorrowedorReserved(Exception) : 
                pass

            class EmptyFields(Exception) : 
                pass

            try : 
                #get fineamount
                FineAmount_query = """ SELECT fineAmount FROM member WHERE memberID = %s"""
                mycursor.execute(FineAmount_query,data)
                records = mycursor.fetchall()
                fineAmount = int(records[0][0])
                #print(fineAmount)

                #get books currently borrowed
                BooksBorrowed_query = """ SELECT COUNT(memberID) as NumberBooksBorrowed FROM Book WHERE memberID = %s"""
                mycursor.execute(BooksBorrowed_query, data)
                records2 = mycursor.fetchall()
                BooksBorrowed = int(records2[0][0])
                #print(BooksBorrowed)

                #get books on reserve
                BooksReserve_query = """ SELECT COUNT(memberID) as NumberReservationsMade FROM bookHasReservation WHERE memberID = %s;"""
                mycursor.execute(BooksReserve_query, data)
                records3 = mycursor.fetchall()
                BooksReserved = int(records3[0][0])
                #print(BooksReserved)

                if fineAmount > 0 or BooksBorrowed > 0 or BooksReserved > 0 : 
                    raise FineorBorrowedorReserved
                
                elif member_delete == "" : 
                    raise EmptyFields 
                
                else : 
                    with mycursor :
                        deleteMember_query = """ DELETE FROM Member WHERE memberID = %s """ 
                        mycursor.execute(deleteMember_query, data)
                        messagebox.showinfo(title = "Success!", message = "Member Deleted.")

            except EmptyFields : 
                #Produce a popup
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            
            except IndexError :
                #Produce a popup
                messagebox.showerror(title = "Error!", message = "Member does not exist.")
            
            except FineorBorrowedorReserved : 
                #Produce a popup
                messagebox.showerror(title = "Error!", message = "Member has outstanding loans, reservations or fines.")
        
            mydb.commit()

            #Temporary clear the textboxes
            memberID.delete(0,END) 

            mydb.close()

            popup.destroy()

        deleteMember_btn = Button(self, text = "Delete Member", command = popupmsg)
        deleteMember_btn.grid(row = 3, column = 1, pady = 10, sticky = "S")

        #BackToMembers_Page
        BackToMain_button = Button(self, text = "Back To Membership Menu", command = lambda : controller.show_frame(Members_Page))
        BackToMain_button.grid(row = 4, column = 1, pady = 10, sticky = "S")

class Update_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        
        label = Label(self, text ="Membership Update", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))

        label2 = Label(self, text = "To Update a Member, Please Enter Membership ID:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #Creating Textbox to enter Member row
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 2, column = 1, sticky = S, pady = 3)

        f_name = Entry(self, width = 30)
        f_name.grid(row = 3, column = 1, sticky = S, pady = 3)

        l_name = Entry(self, width = 30)
        l_name.grid(row = 4, column = 1, sticky = S, pady = 3)

        faculty = Entry(self, width = 30)
        faculty.grid(row = 5, column = 1, sticky = S, pady = 3)

        phone = Entry(self, width = 30)
        phone.grid(row = 6, column = 1, sticky = S, pady = 3)

        email = Entry(self, width = 30)
        email.grid(row = 7, column = 1, sticky = S, pady = 3)
        
        #Creating Textbox Labels
        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 2, column = 0, sticky = E, pady = 3)

        f_name_label = Label(self, text = "First Name:", background = "#856ff8", fg = "#fff") 
        f_name_label.grid(row = 3, column = 0, sticky = E)

        l_name_label = Label(self, text = "Last Name:", background = "#856ff8", fg = "#fff") 
        l_name_label.grid(row = 4, column = 0, sticky = E)

        faculty_label = Label(self, text = "Faculty:", background = "#856ff8", fg = "#fff") 
        faculty_label.grid(row = 5, column = 0, sticky = E)

        phone_label = Label(self, text = "Phone Number:", background = "#856ff8", fg = "#fff") 
        phone_label.grid(row = 6, column = 0, sticky = E)

        email_label = Label(self, text = "Email Address:", background = "#856ff8", fg = "#fff") 
        email_label.grid(row = 7, column = 0, sticky = E)

        #BackToMembers_Page
        BackToMain_button = Button(self, text = "Back To Membership Menu", command = lambda : controller.show_frame(Members_Page))
        BackToMain_button.grid(row = 9, column = 1, sticky = S, pady = 10)

        def popupmsg(f_name, l_name, faculty, phone, email):
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            member_info = memberID.get()
            data = (member_info,) 

            memberDetails_query = """ SELECT fname, lname, faculty, phone, eMail FROM member WHERE memberID = %s"""
            mycursor.execute(memberDetails_query, memberID.get())
            records = mycursor.fetchall()
            
            if member_info == "" or f_name == "" or l_name == "" or faculty == "" or phone == "" or email == "":
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            elif len(records) == 0:
                messagebox.showerror(title = "Error!", message = "Member does not exist.")
            else:
                #Creating popup window
                popup = Tk()
                popup.title("Member Details")
                popup.geometry("500x500")
                popup.config(background = "#856ff8")

                popup_label =  Label(popup, text = "Please Confirm Updated Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                popup_label.pack(pady=10)

                name = f_name + " " + l_name
            
                #Showing member data
                memberID_label =  Label(popup, text = "Member ID: " + memberID.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                memberID_label.pack(pady=10)

                name_label =  Label(popup, text = "Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                name_label.pack(pady=10)

                faculty_label =  Label(popup, text = "Faculty: " + faculty, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                faculty_label.pack(pady=10)

                phoneNumber_label =  Label(popup, text = "Phone Number: " + phone, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                phoneNumber_label.pack(pady=10)

                eMail_label =  Label(popup, text = "Email Address: " + email, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                eMail_label.pack(pady=10) 

                #Creating buttons
                confirmDeletion_btn = Button(popup, text = "Confirm Update", command = lambda : UpdateMember(popup))
                confirmDeletion_btn.pack(pady=10)

                BackToDelete_btn = Button(popup, text = "Back to Update Function", command = lambda : popup.destroy())
                BackToDelete_btn.pack(pady=10)
            
                popup.mainloop()

        #Create submit Button 
        def UpdateMember(popup): 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            try : 
                #get fineamount
                data1 = (memberID.get(),)
                FineAmount_query = """ SELECT fineAmount FROM member WHERE memberID = %s"""
                mycursor.execute(FineAmount_query, data1)
                records = mycursor.fetchall()
                fineAmount = int(records[0][0])        
                
                #Insert Into Table
                member_update = memberID.get()
                f_name_update = f_name.get()
                l_name_update = l_name.get()
                faculty_update = faculty.get()
                phone_update = phone.get()
                email_update = email.get()
                fine_amount_update = fineAmount 

                if member_update == "" or f_name_update == "" or faculty_update == "" or phone_update == "" or email_update == "" : 
                    messagebox.showerror(title = "Error!", message = "Missing or incomplete Fields.")

                else : 
                    #Update the row 
                    data2 = (member_update, f_name_update, l_name_update, faculty_update, phone_update, email_update, fine_amount_update, member_update)
                    Update_query = """UPDATE Member SET memberID = %s, fName = %s, lName = %s, faculty = %s, phone = %s, eMail= %s, fineAmount= %s WHERE memberID = %s"""
                    mycursor.execute(Update_query, data2)
                    messagebox.showinfo(title = "Success!", message = "ALS Membership updated.")

                #Temporary clear the textboxes
                memberID.delete(0,END) 
                f_name.delete(0,END) 
                l_name.delete(0,END) 
                faculty.delete(0,END) 
                phone.delete(0,END) 
                email.delete(0,END) 

            except IndexError : 
                #Produce a popup
                messagebox.showerror(title = "Error!", message = "Member does not exist.")

            #commit
            mydb.commit()

            #close connection
            mydb.close() 

            popup.destroy()

        updateMember_btn = Button(self, text = "Update Member", command = lambda : popupmsg(f_name.get(), l_name.get(), 
        faculty.get(), phone.get(), email.get()))
        updateMember_btn.grid(row = 8, column = 1, sticky = S, pady = 10)

class Books_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Books", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #2 Buttons on this Page [ Acquisition , Withdrawal]
        #[ Acquisition_Page, Withdrawal_Page ]

        #Acquisiton Button
        Acquisition_button = Button(self, text = "Acquisition", command = lambda : controller.show_frame(Acquisition_Page))
        Acquisition_button.grid(row = 2, column = 0, pady = 10, sticky = "S")

        #Withdrawal Button
        Withdrawal_button = Button(self, text = "Withdrawal", command = lambda : controller.show_frame(Withdrawal_Page))
        Withdrawal_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu))
        BackToMain_button.grid(row = 4, column = 0, pady = 10, sticky = "S")

class Acquisition_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Book Acquisition", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, pady = (30,0))

        label2 = Label(self, text = "For New Book Acquisition, Please Enter Required Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, padx = 10, pady= 10)

        #Creating Textbox to enter Book Row
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, pady = 3, sticky = S)

        title = Entry(self, width = 30)
        title.grid(row = 3, column = 1, pady = 3, sticky = S)

        author = Entry(self, width = 30) #Will be a List
        author.grid(row = 4, column = 1, pady = 3, sticky = S)

        ISBN = Entry(self, width = 30)
        ISBN.grid(row = 5, column = 1, pady = 3, sticky = S)

        publisher = Entry(self, width = 30) 
        publisher.grid(row = 6, column = 1,  pady = 3, sticky = S)

        publicationYear = Entry(self, width = 30)
        publicationYear.grid(row = 7, column = 1, pady = 3, sticky = S)

        #Creating Textbox Labels
        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, sticky = E)

        title_label = Label(self, text = "Book Title:", background = "#856ff8", fg = "#fff") 
        title_label.grid(row = 3, column = 0, sticky = E)
        
        author_label = Label(self, text = "Authors:", background = "#856ff8", fg = "#fff") 
        author_label.grid(row = 4, column = 0, sticky = E)

        ISBN_label = Label(self, text = "ISBN:", background = "#856ff8", fg = "#fff") 
        ISBN_label.grid(row = 5, column = 0, sticky = E)

        publisher_label = Label(self, text = "Publisher:", background = "#856ff8", fg = "#fff") 
        publisher_label.grid(row = 6, column = 0, sticky = E)

        publicationYear_label = Label(self, text = "Publication Year:", background = "#856ff8", fg = "#fff") 
        publicationYear_label.grid(row = 7, column = 0, sticky = E)
        
        #BackToBooks_Page
        BackToMain_button = Button(self, text = "Back To Books Menu", command = lambda : controller.show_frame(Books_Page))
        BackToMain_button.grid(row = 9, column = 1, pady = 10, sticky = "S")

        def AddBook(): 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            title_insert = title.get()
            author_insert = author.get()
            ISBN_insert = ISBN.get()
            publisher_insert = publisher.get()
            publicationYear_insert = publicationYear.get()
            memberID_insert = None
            borrowDate_insert = None
            dueDate_insert = None
            returnDate_insert = None
            numOfReservations = 0

            author_list = author_insert.split(",") 

            #If any fields are missing
            if accessionNumber_insert == "" or title_insert == "" or author_insert == "" or ISBN_insert == "" or publisher_insert == "" or publicationYear_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete Fields")
            
            else : 
                try :
                    try : 
                        #Insert into publisher
                        data1 = (publisher_insert,)
                        addpublisher_query = """ INSERT INTO Publisher VALUES (%s) """
                        mycursor.execute(addpublisher_query,data1)
                    
                    except pymysql.IntegrityError: 
                        #If publisher already present, ignore and move on
                        pass

                    #Insert into author
                    for a in author_list :
                        try : 
                            data2 = (a,)
                            addauthor_query = """ INSERT INTO Author VALUES (%s) """
                            mycursor.execute(addauthor_query, data2)
                        
                        except pymysql.IntegrityError: 
                            #If author already present, ignore and move on
                            pass

                    #Insert into Book
                    data = (accessionNumber_insert, title_insert, ISBN_insert, publicationYear_insert, publisher_insert, memberID_insert, borrowDate_insert, dueDate_insert, returnDate_insert, numOfReservations) 
                    addbook_query = """INSERT INTO Book VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    mycursor.execute(addbook_query,data)
                    messagebox.showinfo(title = "Success!", message = "Book Added.")    

                    #Insert into BookhasAuthor
                    for b in author_list : 
                        data3 = (b, accessionNumber_insert)
                        addBookHasAuthor_query = """ INSERT INTO BookHasAuthor(authorName, accessionNumber) VALUES (%s, %s) """
                        mycursor.execute(addBookHasAuthor_query, data3) 

                except pymysql.IntegrityError: 
                    #Produce a popup if accession Number already present, 
                    messagebox.showerror(title = "Error!", message = "Book already exists; Missing or incomplete fields.")

                #commit
                mydb.commit()
                #close connection
                mydb.close() 

        addBook_btn = Button(self, text = "Add Book", command = AddBook)
        addBook_btn.grid(row = 8, column = 1, pady = 10, sticky = "S")

class Withdrawal_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Book Withdrawal", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
        
        label2 = Label(self, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10) 

        #Create TextBox for Accession Number
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, pady = 3, sticky = S)

        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, stick = E) 

        #BackToBooks_Page
        BackToMain_button = Button(self, text = "Back To Books Menu", command = lambda : controller.show_frame(Books_Page))
        BackToMain_button.grid(row = 4, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            accessionNumber_insert = accessionNumber.get()
            data = (accessionNumber_insert,)
            
            bookDetails_query = """ SELECT accessionNumber, title, ISBN, publisherName, publicationYear FROM book WHERE accessionNumber = %s"""
            mycursor.execute(bookDetails_query, accessionNumber.get())
            records = mycursor.fetchall()

            bookAuthors_query = """ SELECT authorName FROM bookhasauthor WHERE accessionNumber = %s"""
            mycursor.execute(bookAuthors_query, accessionNumber.get())
            records1 = mycursor.fetchall()
            
            if data[0] == "":
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            elif len(records) == 0:
                messagebox.showerror(title = "Error!", message = "Book does not exist.")
            else:
                memberID_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                mycursor.execute(memberID_query,data)
                records2 = mycursor.fetchall()
                if len(records2) == 0:
                    messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
                else:
                    member = records2[0][0]
                    if member != None:
                        messagebox.showerror(title = "Error!", message = "Book is currently on loan.")
                    else:
                        reservation_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                        mycursor.execute(reservation_query, data)
                        records3 = mycursor.fetchall()
                        reservationNumber = records3[0][0] 
                        if (reservationNumber > 0) : 
                            messagebox.showerror(title = "Error!", message = "Book is currently reserved.")              
                        else:
                            #Creating popup window
                            popup = Tk()
                            popup.title("Book Details")
                            popup.geometry("500x500")
                            popup.config(background = "#856ff8")

                            popup_label =  Label(popup, text = "Please Confirm Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                            popup_label.pack(pady=10)

                            bookDetails = records[0]
                            title = bookDetails[1]
                            ISBN = bookDetails[2]
                            publisher = bookDetails[3]
                            year = bookDetails[4]
                            tplAuthors = map(lambda v: v[0], records1)
                            authors = ', '.join(list(tplAuthors))
                        
                            #Showing member data
                            accessionNum_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            accessionNum_label.pack(pady=10)

                            title_label =  Label(popup, text = "Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            title_label.pack(pady=10)

                            authors_label =  Label(popup, text = "Authors: " + authors, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            authors_label.pack(pady=10)

                            ISBN_label =  Label(popup, text = "ISBN: " + ISBN, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            ISBN_label.pack(pady=10)

                            publisher_label =  Label(popup, text = "Publisher: " + publisher, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            publisher_label.pack(pady=10) 

                            year_label =  Label(popup, text = "Year: " + year, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            year_label.pack(pady=10)

                            #Creating buttons
                            confirmWithdrawal_btn = Button(popup, text = "Confirm Withdrawal", command = lambda : WithdrawBook(popup))
                            confirmWithdrawal_btn.pack(pady=10)

                            BackToWithdrawal_btn = Button(popup, text = "Back to Withdrawal Function", command = lambda : popup.destroy())
                            BackToWithdrawal_btn.pack(pady=10)
                        
                            popup.mainloop()

        def WithdrawBook(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
            
            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()

            #If any fields are missing
            if accessionNumber_insert == "" : 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete Fields.")
            
            else : 
                class OnLoan(Exception) : 
                    pass 
                class OnReservation(Exception):
                    pass
                
                try : 
                    with mycursor: 
                        #Check MemberID 
                        data1 = (accessionNumber_insert,)
                        memberID_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(memberID_query,data1)
                        records1 = mycursor.fetchall()
                        member = records1[0][0]

                        if (member != None) : 
                            raise OnLoan

                        reservation_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                        mycursor.execute(reservation_query, data1)
                        records2 = mycursor.fetchall() 
                        reservationNumber = records2[0][0] 

                        if (reservationNumber > 0) : 
                            raise OnReservation

                        #IF ALL CONDITIONS PASS, MEANS CAN WITHDRAW
                        deleteBook_query = """ DELETE FROM Book WHERE accessionNumber = (%s) """ 
                        mycursor.execute(deleteBook_query, data1)
                        messagebox.showinfo(title = "Success!", message = "Book Withdrawn.")

                except OnLoan : 
                    messagebox.showerror(title = "Error!", message = "Book is currently on loan.")
                
                except OnReservation : 
                    messagebox.showerror(title = "Error!", message = "Book is currently reserved.")

                except IndexError : 
                    messagebox.showerror(title = "Error!", message = "Book does not exist.")

            #commit
            mydb.commit()
            #close connection
            mydb.close() 

            popup.destroy()
        
        withdrawBook_btn = Button(self, text = "Withdraw Book", command = popupmsg)
        withdrawBook_btn.grid(row = 3, column = 1, pady = 10, sticky = "S")

class Loans_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Loans", font = LARGEFONT,  background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #2 Buttons on this page [ Borrow, Return ]
        # [ Borrow_Page, Return_Page ]

        #Borrow Button
        Borrow_button = Button(self, text = "Borrow Book", command = lambda : controller.show_frame(Borrow_Page))
        Borrow_button.grid(row = 2, column = 0, pady = 10, sticky = "S")

        #Return Button
        Return_button = Button(self, text = "Return Book", command = lambda : controller.show_frame(Return_Page))
        Return_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu))
        BackToMain_button.grid(row = 4, column = 0, pady = 10, sticky = "S")

class Borrow_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Borrow Book", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
        
        
        label2 = Label(self, text = "To Borrow a Book, Please Enter Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #Create TextBox for Accession Number
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, pady = 3, sticky = S)

        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, stick = E) 

        #Create TextBox for MembershipID 
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 3, column = 1, pady = 3, sticky = S)

        memberID_label = Label(self, text = "Member ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 3, column = 0,  stick = E) 

        #BackToLoans Page
        BackToMain_button = Button(self, text = "Back To Loans Menu", command = lambda : controller.show_frame(Loans_Page))
        BackToMain_button.grid(row = 5, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get() 

            bookDetails_query = """ SELECT accessionNumber, title, ISBN, publisherName, publicationYear FROM book WHERE accessionNumber = %s"""
            mycursor.execute(bookDetails_query, accessionNumber.get())
            records = mycursor.fetchall()

            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            else :  
                class MaxBook(Exception) : 
                    pass 

                class FineExist(Exception) : 
                    pass 

                class MemberAlreadyBorrowing(Exception) :
                    pass

                try : 
                    with mycursor : 
                        #Check if Fine > 0 
                        data1 = (memberID_insert,) 
                        FineExist_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineExist_query, data1) 
                        records1 = mycursor.fetchall() 
                        FineAmount = int(records1[0][0])
                        
                        if FineAmount > 0 : 
                            raise FineExist 

                        #Check Number of Books member is currently borrowing
                        data2 = (memberID_insert,)
                        BorrowNum_query = """ SELECT COUNT(memberID) FROM Book WHERE memberID = (%s) """
                        mycursor.execute(BorrowNum_query,data2)
                        records2 = mycursor.fetchall()
                        BooksBorrowed = records2[0][0]
                        
                        if BooksBorrowed >= 1 : 
                            if BooksBorrowed == 2 : 
                                raise MaxBook(Exception) 
                            else : 
                            #Check if any books currently overdue
                                data3 = (memberID_insert,) 
                                BooksBorrowed_query = """ SELECT DATEDIFF(CURDATE(), dueDate) FROM Book WHERE memberID = (%s) """
                                mycursor.execute(BooksBorrowed_query, data3)
                                records3 = mycursor.fetchall() 
                                DateDiff = records3[0] 
                                for i in DateDiff : 
                                    if i > 0 : 
                                        raise FineExist 
                                        break 
                                    else : 
                                        continue  
                        
                        #Check if current member is already borrowing this book 
                        data4 = (accessionNumber_insert,) 
                        getBorrower_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(getBorrower_query,data4)
                        records4 = mycursor.fetchall()
                        member = records4[0][0]

                        if member == memberID_insert : 
                            raise MemberAlreadyBorrowing

                        elif member != None :
                            data = (accessionNumber_insert,) 
                            getBorrower_query = """ SELECT dueDate FROM Book WHERE accessionNumber = (%s) """
                            mycursor.execute(getBorrower_query,data)
                            records = mycursor.fetchall()
                            dueDate = records[0][0]
                            messagebox.showerror(title = "Error!", message = "Book currently on Loan until: " + dueDate.strftime('%Y-%m-%d'))

                        else:
                            #Check if there is reservations and if member is currently reserving book 
                            data5 = (accessionNumber_insert,)
                            getReservations_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                            mycursor.execute(getReservations_query, data5)
                            records5 = mycursor.fetchall()
                            reservations = int(records5[0][0])

                            if reservations > 0 : 
                                #check if member reserved book 
                                data6 = (accessionNumber_insert,)
                                getReserveMember_query = """ SELECT memberID FROM bookHasReservation WHERE accessionNumber = (%s) """
                                mycursor.execute(getReserveMember_query,data6)
                                records6 = mycursor.fetchall() 
                                reservelist = records6

                                if memberID_insert in reservelist[0] :                
                                    #Creating popup window
                                    popup = Tk()
                                    popup.title("Borrowing Details")
                                    popup.geometry("500x500")
                                    popup.config(background = "#856ff8")

                                    popup_label =  Label(popup, text = "Confirm Loan Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                                    popup_label.pack(pady=10)

                                    bookDetails_query = """ SELECT accessionNumber, title, ISBN, publisherName, publicationYear FROM book WHERE accessionNumber = %s"""
                                    mycursor.execute(bookDetails_query, accessionNumber.get())
                                    records = mycursor.fetchall()

                                    memberDetails_query = """ SELECT fname, lname, faculty, phone, eMail FROM member WHERE memberID = %s"""
                                    mycursor.execute(memberDetails_query, memberID_insert)
                                    records1 = mycursor.fetchall()                            

                                    bookDetails = records[0]
                                    memberDetails = records1[0]
                                    title = bookDetails[1]
                                    name = memberDetails[0] 
                                    if memberDetails[1] != None:
                                        name += (" " + memberDetails[1])

                                    borrowDate = datetime.today()
                                    dueDate = borrowDate + timedelta(days=14)
                                
                                    #Showing member data
                                    accessionNum_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    accessionNum_label.pack(pady=10)

                                    title_label =  Label(popup, text = "Book Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    title_label.pack(pady=10)

                                    borrowdate_label =  Label(popup, text = "Borrow Date: " + borrowDate.strftime('%Y-%m-%d'), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    borrowdate_label.pack(pady=10)

                                    membershipID_label =  Label(popup, text = "Membership ID: " + memberID.get() , font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    membershipID_label.pack(pady=10)

                                    name_label =  Label(popup, text = "Member Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    name_label.pack(pady=10) 

                                    dueDate_label =  Label(popup, text = "Due Date: " + dueDate.strftime('%Y-%m-%d'), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                    dueDate_label.pack(pady=10)

                                    #Creating buttons
                                    confirmLoan_btn = Button(popup, text = "Confirm Loan", command = lambda : BorrowBook(popup))
                                    confirmLoan_btn.pack(pady=10)

                                    BackToBorrow_btn = Button(popup, text = "Back to Borrow Function", command = lambda : popup.destroy())
                                    BackToBorrow_btn.pack(pady=10)
                                
                                    popup.mainloop()

                                else : 
                                    messagebox.showerror(title = "Error!", message = "Book has existing reservations.")

                            else :
                                #Creating popup window
                                popup = Tk()
                                popup.title("Borrowing Details")
                                popup.geometry("500x500")
                                popup.config(background = "#856ff8")

                                popup_label =  Label(popup, text = "Confirm Loan Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                                popup_label.pack(pady=10)

                                bookDetails_query = """ SELECT accessionNumber, title, ISBN, publisherName, publicationYear FROM book WHERE accessionNumber = %s"""
                                mycursor.execute(bookDetails_query, accessionNumber.get())
                                records = mycursor.fetchall()

                                memberDetails_query = """ SELECT fname, lname, faculty, phone, eMail FROM member WHERE memberID = %s"""
                                mycursor.execute(memberDetails_query, memberID.get())
                                records1 = mycursor.fetchall()

                                bookDetails = records[0]
                                memberDetails = records1[0]
                                title = bookDetails[1]
                                name = memberDetails[0] 
                                if memberDetails[1] != None:
                                    name += (" " + memberDetails[1])

                                borrowDate = datetime.today()
                                dueDate = borrowDate + timedelta(days=14)
                            
                                #Showing member data
                                accessionNum_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                accessionNum_label.pack(pady=10)

                                title_label =  Label(popup, text = "Book Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                title_label.pack(pady=10)

                                borrowDate_label =  Label(popup, text = "Borrow Date: " + borrowDate.strftime('%Y-%m-%d'), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                borrowDate_label.pack(pady=10)

                                membershipID_label =  Label(popup, text = "Membership ID: " + memberID.get() , font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                membershipID_label.pack(pady=10)

                                name_label =  Label(popup, text = "Member Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                name_label.pack(pady=10) 

                                dueDate_label =  Label(popup, text = "Due Date: " + dueDate.strftime('%Y-%m-%d'), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                dueDate_label.pack(pady=10)

                                #Creating buttons
                                confirmLoan_btn = Button(popup, text = "Confirm Loan", command = lambda : BorrowBook(popup))
                                confirmLoan_btn.pack(pady=10)

                                BackToBorrow_btn = Button(popup, text = "Back to Borrow Function", command = lambda : popup.destroy())
                                BackToBorrow_btn.pack(pady=10)
                            
                                popup.mainloop()
        
                except MemberAlreadyBorrowing : 
                    messagebox.showerror(title = "Error!", message = "Member is already borrowing this book.")
                                                
                except FineExist : 
                    messagebox.showerror(title = "Error!", message = "Member has outstanding fines/overdue books.")

                except MaxBook : 
                    messagebox.showerror(title = "Error!", message = "Member loan quota exceeded.")

                except IndexError :
                    messagebox.showerror(title = "Error!", message = "Accession Number or MemberID does not exist.")

        def BorrowBook(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
            
            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get() 

            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            
            else :  
                class MaxBook(Exception) : 
                    pass 

                class FineExist(Exception) : 
                    pass 

                class MemberAlreadyBorrowing(Exception) :
                    pass

                try : 
                    with mycursor : 
                        #Check if Fine > 0 
                        data1 = (memberID_insert,) 
                        FineExist_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineExist_query, data1) 
                        records1 = mycursor.fetchall() 
                        FineAmount = int(records1[0][0])
                        
                        if FineAmount > 0 : 
                            raise FineExist 

                        #Check Number of Books member is currently borrowing
                        data2 = (memberID_insert,)
                        BorrowNum_query = """ SELECT COUNT(memberID) FROM Book WHERE memberID = (%s) """
                        mycursor.execute(BorrowNum_query,data2)
                        records2 = mycursor.fetchall()
                        BooksBorrowed = records2[0][0]
                        
                        if BooksBorrowed >= 1 : 
                            if BooksBorrowed == 2 : 
                                raise MaxBook(Exception) 
                            else : 
                            #Check if any books currently overdue
                                data3 = (memberID_insert,) 
                                BooksBorrowed_query = """ SELECT DATEDIFF(CURDATE(), dueDate) FROM Book WHERE memberID = (%s) """
                                mycursor.execute(BooksBorrowed_query, data3)
                                records3 = mycursor.fetchall() 
                                DateDiff = records3[0] 
                                for i in DateDiff : 
                                    if i > 0 : 
                                        raise FineExist 
                                        break 
                                    else : 
                                        continue  
                        
                        #Check if current member is already borrowing this book 
                        data4 = (accessionNumber_insert,) 
                        getBorrower_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(getBorrower_query,data4)
                        records4 = mycursor.fetchall()
                        member = records4[0][0]

                        if member == memberID_insert : 
                            raise MemberAlreadyBorrowing

                        elif member != None : 
                            data = (accessionNumber_insert,) 
                            getBorrower_query = """ SELECT dueDate FROM Book WHERE accessionNumber = (%s) """
                            mycursor.execute(getBorrower_query,data)
                            records = mycursor.fetchall()
                            dueDate = records[0][0]
                            messagebox.showerror(title = "Error!", message = "Book currently on loan until: " + dueDate.strftime('%Y-%m-%d'))

                        else:
                            #Check if there is reservations and if member is currently reserving book 
                            data5 = (accessionNumber_insert,)
                            getReservations_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                            mycursor.execute(getReservations_query, data5)
                            records5 = mycursor.fetchall()
                            reservations = int(records5[0][0])

                            if reservations > 0 : 
                                #check if member reserved book 
                                data6 = (accessionNumber_insert,)
                                getReserveMember_query = """ SELECT memberID FROM bookHasReservation WHERE accessionNumber = (%s) """
                                mycursor.execute(getReserveMember_query,data6)
                                records6 = mycursor.fetchall() 
                                reservelist = records6

                                if memberID_insert in reservelist[0] :  
                                    #Proceed with borrowing and numOfReservations - 1
                                    data7 = (memberID_insert, reservations - 1, accessionNumber_insert)
                                    Borrow_query = """ UPDATE Book SET borrowDate = CURDATE(), memberID = (%s), numOfReservations = (%s) WHERE accessionNumber = (%s) """
                                    mycursor.execute(Borrow_query,data7)

                                    #Remove From bookHasReservations
                                    data8 = (memberID_insert, accessionNumber_insert)
                                    remove_query = """ DELETE FROM BookHasReservation WHERE memberID = (%s) AND accessionNumber = (%s) """
                                    mycursor.execute(remove_query, data8)
                                    messagebox.showinfo(title = "Success!", message = "Book Borrowed.")

                                else : 
                                    messagebox.showerror(title = "Error!", message = "Book has existing reservations.")

                            else : 
                                #proceed with borrowing 
                                data9 = (memberID_insert, accessionNumber_insert) 
                                Borrow2_query = """ UPDATE Book SET borrowDate = CURDATE(), memberID = (%s) WHERE accessionNumber = (%s) """
                                mycursor.execute(Borrow2_query,data9)
                                messagebox.showinfo(title = "Success!", message = "Book Borrowed.")
        
                except MemberAlreadyBorrowing : 
                    messagebox.showerror(title = "Error", message = "Member is already borrowing this book.")
                                
                except FineExist : 
                    messagebox.showerror(title = "Error", message = "Member has outstanding fines/overdue books.")

                except MaxBook : 
                    messagebox.showerror(title = "Error", message = "Member loan quota exceeded.")

                except IndexError :
                    messagebox.showerror(title = "Error", message = "Accession Number or MemberID does not exist.")
            
            #commit
            mydb.commit()
            #close connection
            mydb.close() 

            popup.destroy()
            
        BorrowBook_btn = Button(self, text = "Borrow Book", command = popupmsg)
        BorrowBook_btn.grid(row = 4, column = 1, pady = 10, sticky = "S")

class Return_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Return Book", font = LARGEFONT,  background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
        
        label2 = Label(self, text = "To Return a Book, Please Enter Information Below:", background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S,  pady= 10)

        #Create TextBox for Accession Number
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, pady = 3, sticky = S)

        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, sticky = E ) 

        #Create TextBox for ReturnDate 
        returnDate = Entry(self, width = 30) 
        returnDate.grid(row = 3, column = 1, pady = 3, sticky = S)

        returnDate_label = Label(self, text = "Return Date (YYYY-MM-DD):", background = "#856ff8", fg = "#fff") 
        returnDate_label.grid(row = 3, column = 0, stick = E) 

        #Back to Loans Page
        BackToMain_button = Button(self, text = "Back To Loans Menu", command = lambda : controller.show_frame(Loans_Page))
        BackToMain_button.grid(row = 5, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            returnDate_insert = returnDate.get() 

            #If any fields are missing
            if accessionNumber_insert == "" or returnDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or Incomplete Fields.")
            
            else : 
                class NotBorrowed(Exception) : 
                    pass 
                class IndexError(Exception):
                    pass
                class TypeError(Exception):
                    pass

                try : 
                    with mycursor: 
                        #get Fine Amount of Book, get Fine Amount of member, Update fineAmount in member 
                        data1 = (returnDate_insert, accessionNumber_insert)
                        FineOwedBook_query = """ SELECT DATEDIFF( (%s) , dueDate) FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(FineOwedBook_query,data1)
                        record1 = mycursor.fetchall()
                        if len(record1) == 0:
                            raise IndexError
                        else:
                            BookFine = (record1[0][0])
                            if BookFine == None : 
                                raise NotBorrowed
                            else:
                                BookFineOwed = int(BookFine)

                        #Get MemberID of member returning the book 
                        data2 = (accessionNumber_insert,)
                        member_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(member_query,data2)
                        record2 = mycursor.fetchall()
                        memberID = record2[0][0]

                        if memberID == "" : 
                            raise NotBorrowed

                        #Get Fine Amount of member returning the book
                        data3 = (memberID,)
                        FineAmount_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineAmount_query, data3)
                        record3 = mycursor.fetchall()
                        if len(record3) == 0:
                            raise NotBorrowed
                        else:
                            FineAmount = int(record3[0][0])
                        
                        if len(record3) != 0:   
                            #Creating popup window
                            popup = Tk()
                            popup.title("Returning Details")
                            popup.geometry("500x500")
                            popup.config(background = "#856ff8")

                            popup_label =  Label(popup, text = "Confirm Return Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                            popup_label.pack(pady=10)

                            bookDetails_query = """ SELECT accessionNumber, title, memberID FROM book WHERE accessionNumber = %s"""
                            mycursor.execute(bookDetails_query, accessionNumber.get())
                            records = mycursor.fetchall()

                            bookDetails = records[0]
                            title = bookDetails[1]

                            #Get Fine Amount of member returning the book
                            data3 = (memberID,)
                            FineAmount_query = """ SELECT fname, lname, fineAmount FROM Member WHERE memberID = (%s) """
                            mycursor.execute(FineAmount_query, data3)
                            record3 = mycursor.fetchall()

                            memberDetails = record3[0]
                            name = memberDetails[0] 
                            if memberDetails[1] != None:
                                name += (" " + memberDetails[1])

                            if BookFine < 0:
                                BookFine = 0
                        
                            #Showing member data
                            memberID_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            memberID_label.pack(pady=10)

                            name_label =  Label(popup, text = "Book Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            name_label.pack(pady=10)

                            faculty_label =  Label(popup, text = "Membership ID: " + memberID, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            faculty_label.pack(pady=10)

                            phoneNumber_label =  Label(popup, text = "Member Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            phoneNumber_label.pack(pady=10)

                            eMail_label =  Label(popup, text = "Return Date: " + returnDate.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            eMail_label.pack(pady=10) 

                            eMail_label =  Label(popup, text = "Fine:$" + str(BookFine), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            eMail_label.pack(pady=10)

                            #Creating buttons
                            confirmDeletion_btn = Button(popup, text = "Confirm Return", command = lambda : ReturnBook(popup))
                            confirmDeletion_btn.pack(pady=10)

                            BackToDelete_btn = Button(popup, text = "Back to Return Function", command = lambda : popup.destroy())
                            BackToDelete_btn.pack(pady=10)
                        
                            popup.mainloop()
                
                except TypeError : 
                    messagebox.showerror(title = "Error!", message = "Please enter the date in YYYY-MM-DD Format.")
                
                except NotBorrowed : 
                    messagebox.showerror(title = "Error!", message = "Book is currently not borrowed / Please enter the date in YYYY-MM-DD Format.")

                except IndexError : 
                    messagebox.showerror(title = "Error!", message = "Book does not exist.")

        def ReturnBook(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
            
            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            returnDate_insert = returnDate.get()

            #If any fields are missing
            if accessionNumber_insert == "" or returnDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            
            else : 
                class NotBorrowed(Exception) : 
                    pass 

                try : 
                    with mycursor: 
                        #get Fine Amount of Book, get Fine Amount of member, Update fineAmount in member 
                        data1 = (returnDate_insert, accessionNumber_insert)
                        FineOwedBook_query = """ SELECT DATEDIFF( (%s) , dueDate) FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(FineOwedBook_query,data1)
                        record1 = mycursor.fetchall()
                        BookFine = (record1[0][0])

                        if BookFine == None : 
                            raise NotBorrowed
                        else : 
                            BookFineOwed = int(BookFine)

                        #Get MemberID of member returning the book 
                        data2 = (accessionNumber_insert,)
                        member_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(member_query,data2)
                        record2 = mycursor.fetchall()
                        memberID = record2[0][0] 

                        if memberID == "" : 
                            raise NotBorrowed

                        #Get Fine Amount of member returning the book
                        data3 = (memberID,)
                        FineAmount_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineAmount_query, data3)
                        record3 = mycursor.fetchall() 
                        FineAmount = int(record3[0][0])

                        newFineAmount = FineAmount + BookFineOwed 
                        #If BookFineOwed > 0 then update member FineAmount else dont need. 
                        if BookFineOwed > 0 : 
                            data4 = (newFineAmount, memberID) 
                            UpdateFine_query = """ UPDATE Member SET fineAmount = (%s) WHERE memberID = (%s) """
                            mycursor.execute(UpdateFine_query, data4)
                            
                            #proceed to return
                            data5 = (accessionNumber_insert,)
                            returnBook_query = """ UPDATE Book SET memberID = NULL WHERE accessionNumber = (%s) """
                            mycursor.execute(returnBook_query,data5) 
                            messagebox.showinfo(title = "Book returned", message = "Book returned successfully but has fines.")

                        else : 
                            #Proceed to return 
                            data5 = (accessionNumber_insert,)
                            returnBook_query = """ UPDATE Book SET memberID = NULL WHERE accessionNumber = (%s) """
                            mycursor.execute(returnBook_query,data5) 
                            messagebox.showinfo(title = "Book returned", message = "Book returned successfully.")
                
                except TypeError : 
                    messagebox.showerror(title = "Error!", message = "Please enter the date in YYYY-MM-DD Format.")
                
                except NotBorrowed : 
                    messagebox.showerror(title = "Error!", message = "Book is currently not borrowed / Please enter the date in YYYY-MM-DD Format.")

                except IndexError : 
                    messagebox.showerror(title = "Error!", message = "Book does not exist.")
            
            #Commit 
            mydb.commit()
            mydb.close() 

            popup.destroy()

        ReturnBook_btn = Button(self, text = "Return Book", command = popupmsg)
        ReturnBook_btn.grid(row = 4, column = 1, pady = 10, sticky = "S")

class Reservation_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Reservations", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0), sticky = "S")
        
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, pady= 10, sticky = "S")

        #2 Buttons on this page [ Reserve, CancelReservation ]
        # [Reserve_Page, CancelReserve_Page]

        #Reserve Button
        Borrow_button = Button(self, text = "Reserve Book", command = lambda : controller.show_frame(Reserve_Page))
        Borrow_button.grid(row = 2, column = 0, pady = 10, sticky = "S")
        
        #Cancel Reserve Button
        CancelReservation_button = Button(self, text = "Cancel Reservation", command = lambda : controller.show_frame(CancelReserve_Page))
        CancelReservation_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu))
        BackToMain_button.grid(row = 4, column = 0, pady = 10, sticky = "S")

class Reserve_Page(tk.Frame) :
     def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Reserve Book", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1,sticky = "S", pady = (30,0))
        
        label2 = Label(self, text = "To Reserve a Book, Please Enter Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1,sticky = "S", pady= 10)

        #Create TextBox for Accession Number
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, sticky = "S", pady = 3)

        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, sticky = E) 

        #Create TextBox for MemberID
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 3, column = 1, pady = 3,sticky = "S")

        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 3, column = 0, sticky = "E") 

        #Create TextBox for Reserve_date
        reserveDate = Entry(self, width = 30) 
        reserveDate.grid(row = 4, column = 1, pady = 3,sticky = "S")

        reserveDate_label = Label(self, text = "Reserve Date (YYYY-MM-DD):", background = "#856ff8", fg = "#fff") 
        reserveDate_label.grid(row = 4, column = 0,  stick = "E") 

        #Back to Reservation Page
        BackToMain_button = Button(self, text = "Back To Reservation Menu", command = lambda : controller.show_frame(Reservation_Page))
        BackToMain_button.grid(row = 6, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get()
            reserveDate_insert = reserveDate.get()
            
            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "" or reserveDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete Fields.")

            else : 
                class FineExist(Exception) : 
                    def __init__(self, amount) : 
                        self.amount = amount

                class OverdueBook(Exception) : 
                    pass 

                class MemberAlreadyBorrowing(Exception) : 
                    pass 
                
                class BookNotBeingBorrowed(Exception) : 
                    pass

                class MaxedOut(Exception) : 
                    pass

                try :
                    with mycursor : 
                    #Check if member has Outstanding Fines
                    #Check if Fine > 0 
                        data1 = (memberID_insert,) 
                        FineExist_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineExist_query, data1) 
                        records1 = mycursor.fetchall() 
                        FineAmount = int(records1[0][0])
                        
                        if FineAmount > 0 : 
                            raise FineExist((FineAmount))

                    #Check Number of Books member is currently borrowing
                        data2 = (memberID_insert,)
                        BorrowNum_query = """ SELECT COUNT(memberID) FROM Book WHERE memberID = (%s) """
                        mycursor.execute(BorrowNum_query,data2)
                        records2 = mycursor.fetchall()
                        BooksBorrowed = records2[0][0]

                        #Check if member has any overdue books  
                        if BooksBorrowed >= 1 : 
                            data3 = (memberID_insert,) 
                            BooksBorrowed_query = """ SELECT DATEDIFF(CURDATE(), dueDate) FROM Book WHERE memberID = (%s) """
                            mycursor.execute(BooksBorrowed_query, data3)
                            records3 = mycursor.fetchall() 
                            DateDiff = records3[0] 
                            for i in DateDiff : 
                                if i > 0 : 
                                    raise OverdueBook
                                    break 
                                else : 
                                    continue  
                        
                        #Check if book is currently borrowed 
                        data4 = (accessionNumber_insert,) 
                        getBorrower_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(getBorrower_query,data4)
                        records4 = mycursor.fetchall()
                        member = records4[0][0]

                        if member == memberID_insert : 
                            raise MemberAlreadyBorrowing

                        elif member == None : 
                            raise BookNotBeingBorrowed
                        
                        #Check the number of reservations made by member
                        data5 = (memberID_insert,)
                        getReserveMember_query = """ SELECT COUNT(memberID) FROM bookHasReservation WHERE memberID = (%s) """
                        mycursor.execute(getReserveMember_query,data5)
                        records5 = mycursor.fetchall() 
                        NumOfReservations = int(records5[0][0])

                        if NumOfReservations > 1 : 
                            raise MaxedOut 
                        
                        else :
                            #Creating popup window
                            popup = Tk()
                            popup.title("Reserving Details")
                            popup.geometry("500x500")
                            popup.config(background = "#856ff8")

                            popup_label =  Label(popup, text = "Confirm Reservation Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                            popup_label.pack(pady=10)

                            bookDetails_query = """ SELECT accessionNumber, title FROM book WHERE accessionNumber = %s"""
                            mycursor.execute(bookDetails_query, accessionNumber.get())
                            records = mycursor.fetchall()

                            memberDetails_query = """ SELECT fname, lname FROM member WHERE memberID = %s"""
                            mycursor.execute(memberDetails_query, memberID.get())
                            records1 = mycursor.fetchall()

                            bookDetails = records[0]
                            memberDetails = records1[0]
                            title = bookDetails[1]
                            name = memberDetails[0] 
                            if memberDetails[1] != None:
                                name += (" " + memberDetails[1])
                        
                            #Showing member data
                            accessionNum_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            accessionNum_label.pack(pady=10)

                            title_label =  Label(popup, text = "Book Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            title_label.pack(pady=10)

                            membershipID_label =  Label(popup, text = "Membership ID: " + memberID.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            membershipID_label.pack(pady=10)

                            name_label =  Label(popup, text = "Member Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            name_label.pack(pady=10)

                            reserveDate_label =  Label(popup, text = "Reserve Date: " + reserveDate.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                            reserveDate_label.pack(pady=10)

                            #Creating buttons
                            confirmReservation_btn = Button(popup, text = "Confirm Reservation", command = lambda : ReserveBook(popup))
                            confirmReservation_btn.pack(pady=10)

                            BackToReserve_btn = Button(popup, text = "Back to Reserve Function", command = lambda : popup.destroy())
                            BackToReserve_btn.pack(pady=10)
                        
                            popup.mainloop()

                except FineExist as e : 
                    s = "Member has outstanding fine of: $" + str(e.amount)
                    messagebox.showerror(title = "Error", message = s)

                except OverdueBook : 
                    messagebox.showerror(title = "Error!", message = "Member currently has overdue books.")

                except MemberAlreadyBorrowing : 
                    messagebox.showerror(title = "Error!", message = "Member is already borrowing this book.")

                except BookNotBeingBorrowed : 
                    messagebox.showerror(title = "Error!", message = "Book is currently not loaned and is free to be borrowed.")

                except MaxedOut : 
                    messagebox.showerror(title = "Error!", message = "Member already has 2 Reservations.")

                except IndexError : 
                    messagebox.showerror(title = "Error!", message = "Accession Number or MemberID is wrong.")

                except pymysql.err.OperationalError : 
                    messagebox.showerror(title = "Error!", message = "Date format is wrong. Please enter Date with format YYYY-MM-DD.")

                except pymysql.err.IntegrityError : 
                    messagebox.showerror(title = "Error!", message = "Member is already reserving the book.")

        def ReserveBook(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
            
            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get() 
            reserveDate_insert = reserveDate.get()

            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "" or reserveDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete Fields.")

            else : 
                class FineExist(Exception) : 
                    def __init__(self, amount) : 
                        self.amount = amount

                class OverdueBook(Exception) : 
                    pass 

                class MemberAlreadyBorrowing(Exception) : 
                    pass 
                
                class BookNotBeingBorrowed(Exception) : 
                    pass

                class MaxedOut(Exception) : 
                    pass

                try :
                    with mycursor : 
                    #Check if member has Outstanding Fines
                    #Check if Fine > 0 
                        data1 = (memberID_insert,) 
                        FineExist_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s) """
                        mycursor.execute(FineExist_query, data1) 
                        records1 = mycursor.fetchall() 
                        FineAmount = int(records1[0][0])
                        
                        if FineAmount > 0 : 
                            raise FineExist((FineAmount))

                    #Check Number of Books member is currently borrowing
                        data2 = (memberID_insert,)
                        BorrowNum_query = """ SELECT COUNT(memberID) FROM Book WHERE memberID = (%s) """
                        mycursor.execute(BorrowNum_query,data2)
                        records2 = mycursor.fetchall()
                        BooksBorrowed = records2[0][0]

                        #Check if member has any overdue books  
                        if BooksBorrowed >= 1 : 
                            data3 = (memberID_insert,) 
                            BooksBorrowed_query = """ SELECT DATEDIFF(CURDATE(), dueDate) FROM Book WHERE memberID = (%s) """
                            mycursor.execute(BooksBorrowed_query, data3)
                            records3 = mycursor.fetchall() 
                            DateDiff = records3[0] 
                            for i in DateDiff : 
                                if i > 0 : 
                                    raise OverdueBook
                                    break 
                                else : 
                                    continue  
                        
                        #Check if book is currently borrowed 
                        data4 = (accessionNumber_insert,) 
                        getBorrower_query = """ SELECT memberID FROM Book WHERE accessionNumber = (%s) """
                        mycursor.execute(getBorrower_query,data4)
                        records4 = mycursor.fetchall()
                        member = records4[0][0]

                        if member == memberID_insert : 
                            raise MemberAlreadyBorrowing

                        elif member == None : 
                            raise BookNotBeingBorrowed
                        
                        #Check the number of reservations made by member
                        data5 = (memberID_insert,)
                        getReserveMember_query = """ SELECT COUNT(memberID) FROM bookHasReservation WHERE memberID = (%s) """
                        mycursor.execute(getReserveMember_query,data5)
                        records5 = mycursor.fetchall() 
                        NumOfReservations = int(records5[0][0])

                        if NumOfReservations > 1 : 
                            raise MaxedOut 
                        
                        else : 
                            #proceed with reserving book
                            data6 = (accessionNumber_insert, memberID_insert, reserveDate_insert)
                            Reserve_query = """ INSERT INTO bookHasReservation VALUES(%s, %s, %s) """
                            mycursor.execute(Reserve_query, data6)

                            #Update Book numOfReservations 
                            data7 = (accessionNumber_insert,)
                            getReservations_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                            mycursor.execute(getReservations_query, data7)
                            records6 = mycursor.fetchall()
                            reservations = int(records6[0][0])
                            
                            data8 = (reservations, accessionNumber_insert)
                            Update_query = """ UPDATE Book SET numOfReservations = (%s) WHERE accessionNumber = (%s) """
                            mycursor.execute(Update_query,data8)
                            messagebox.showinfo(title = "Success!", message = "Book has been reserved.")


                except FineExist as e : 
                    s = "Member has outstanding fine of: $" + str(e.amount)
                    messagebox.showerror(title = "Error", message = s)

                except OverdueBook : 
                    messagebox.showerror(title = "Error", message = "Member currently has overdue Books")

                except MemberAlreadyBorrowing : 
                    messagebox.showerror(title = "Error", message = "Member is already borrowing this book")

                except BookNotBeingBorrowed : 
                    messagebox.showerror(title = "Error", message = "Book is currently not loaned and is free to be borrowed.")

                except MaxedOut : 
                    messagebox.showerror(title = "Error", message = "Member already has 2 Reservations")

                except IndexError : 
                    messagebox.showerror(title = "Error", message = "Accession Number or MemberID is wrong")

                except pymysql.err.OperationalError : 
                    messagebox.showerror(title = "Error", message = "Date format is wrong. Please enter Date with format YYYY-MM-DD")

                except pymysql.err.IntegrityError : 
                    messagebox.showerror(title = "Error", message = "Member is already reserving the book")
            
            #commit
            mydb.commit()
            mydb.close() 

            popup.destroy()
        
        ReserveBook_btn = Button(self, text = "Reserve Book", command = popupmsg)
        ReserveBook_btn.grid(row = 5, column = 1, pady = 10, sticky = "S")

class CancelReserve_Page(tk.Frame) : 
    
    def __init__(self, parent, controller): 
            
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Cancel Reservation for Book", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
            
        label2 = Label(self, text = "To Cancel a Reservation, Please Enter Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #Create TextBox for Accession Number
        accessionNumber = Entry(self, width = 30) 
        accessionNumber.grid(row = 2, column = 1, pady = 3, sticky = "S")

        accessionNumber_label = Label(self, text = "Accession Number:", background = "#856ff8", fg = "#fff") 
        accessionNumber_label.grid(row = 2, column = 0, sticky = "E") 

        #Create TextBox for MemberID
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 3, column = 1, pady = 3, sticky = "S")

        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 3, column = 0, sticky = "E") 

        #Create TextBox for Cancel_date
        cancelDate = Entry(self, width = 30) 
        cancelDate.grid(row = 4, column = 1, pady = 3, sticky = "S")

        cancelDate_label = Label(self, text = "Cancel Date (YYYY-MM-DD):", background = "#856ff8", fg = "#fff") 
        cancelDate_label.grid(row = 4, column = 0, stick = "E") 

        #Back to Reservation
        BackToMain_button = Button(self, text = "Back To Reservation Menu", command = lambda : controller.show_frame(Reservation_Page))
        BackToMain_button.grid(row = 6, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get() 
            cancelDate_insert = cancelDate.get()

            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "" or cancelDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
                
            else : 
                try : 
                    class NoReservations(Exception) :
                        pass

                    class MemberNoReservations(Exception) : 
                        pass

                    with mycursor: 
                        #Check if there is reservations and if member is currently reserving book 
                        data1 = (accessionNumber_insert,)
                        getReservations_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                        mycursor.execute(getReservations_query, data1)
                        records1 = mycursor.fetchall()
                        reservations = int(records1[0][0])
                            
                        if reservations > 0 : 
                            #check if member reserved book 
                            data2 = (accessionNumber_insert,)
                            getReserveMember_query = """ SELECT memberID FROM bookHasReservation WHERE accessionNumber = (%s) """
                            mycursor.execute(getReserveMember_query,data2)
                            records2 = mycursor.fetchall() 
                            reservelist = records2

                            if memberID_insert in reservelist[0] :  
                                #Creating popup window
                                popup = Tk()
                                popup.title("Cancelling Reservation Details")
                                popup.geometry("500x500")
                                popup.config(background = "#856ff8")

                                popup_label =  Label(popup, text = "Confirm Cancellation Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                                popup_label.pack(pady=10)

                                bookDetails_query = """ SELECT accessionNumber, title FROM book WHERE accessionNumber = %s"""
                                mycursor.execute(bookDetails_query, accessionNumber.get())
                                records = mycursor.fetchall()

                                memberDetails_query = """ SELECT fname, lname FROM member WHERE memberID = %s"""
                                mycursor.execute(memberDetails_query, memberID.get())
                                records1 = mycursor.fetchall()

                                bookDetails = records[0]
                                memberDetails = records1[0]
                                title = bookDetails[1]
                                name = memberDetails[0] 
                                if memberDetails[1] != None:
                                    name += (" " + memberDetails[1])
                            
                                #Showing member data
                                accessionNum_label =  Label(popup, text = "Accession Number: " + accessionNumber.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                accessionNum_label.pack(pady=10)

                                title_label =  Label(popup, text = "Book Title: " + title, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                title_label.pack(pady=10)

                                membershipID_label =  Label(popup, text = "Membership ID: " + memberID.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                membershipID_label.pack(pady=10)

                                name_label =  Label(popup, text = "Member Name: " + name, font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                name_label.pack(pady=10)

                                cancellationDate_label =  Label(popup, text = "Cancellation Date: " + cancelDate.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                cancellationDate_label.pack(pady=10)

                                #Creating buttons
                                confirmCancellation_btn = Button(popup, text = "Confirm Cancellation", command = lambda : CancelReservationBook(popup))
                                confirmCancellation_btn.pack(pady=10)

                                BackToCancellation_btn = Button(popup, text = "Back to Cancellation Function", command = lambda : popup.destroy())
                                BackToCancellation_btn.pack(pady=10)
                            
                                popup.mainloop()
                                
                            else : 
                                raise MemberNoReservations 
                        else : 
                            raise NoReservations
                    
                except NoReservations : 
                    messagebox.showerror(title = "Error!", message = "There are no reservations for this book.")

                except MemberNoReservations : 
                    messagebox.showerror(title = "Error!", message = "Member has no such reservation.")
                    
        def CancelReservationBook(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
                
            #Insert Into Table
            accessionNumber_insert = accessionNumber.get()
            memberID_insert = memberID.get() 
            cancelDate_insert = cancelDate.get()

            #If any fields are missing
            if accessionNumber_insert == "" or memberID_insert == "" or cancelDate_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
                
            else : 
                try : 
                    class NoReservations(Exception) :
                        pass

                    class MemberNoReservations(Exception) : 
                        pass

                    with mycursor: 
                        #Check if there is reservations and if member is currently reserving book 
                        data1 = (accessionNumber_insert,)
                        getReservations_query = """ SELECT COUNT(accessionNumber) FROM bookHasReservation WHERE accessionNumber = (%s) """
                        mycursor.execute(getReservations_query, data1)
                        records1 = mycursor.fetchall()
                        reservations = int(records1[0][0])
                            
                        if reservations > 0 : 
                            #check if member reserved book 
                            data2 = (accessionNumber_insert,)
                            getReserveMember_query = """ SELECT memberID FROM bookHasReservation WHERE accessionNumber = (%s) """
                            mycursor.execute(getReserveMember_query,data2)
                            records2 = mycursor.fetchall() 
                            reservelist = records2

                            if memberID_insert in reservelist[0] :  
                                #Delete instance from bookHasReservation
                                data3 = (memberID_insert, accessionNumber_insert)
                                remove_query = """ DELETE FROM BookHasReservation WHERE memberID = (%s) AND accessionNumber = (%s) """
                                mycursor.execute(remove_query, data3)

                                #numOfReservation for book -=1 
                                data4 = (reservations - 1, accessionNumber_insert)
                                Update_query = """ UPDATE Book SET numOfReservations = (%s) WHERE accessionNumber = (%s) """
                                mycursor.execute(Update_query,data4)

                                messagebox.showinfo(title = "Success!", message = "Reservation cancelled.")
                                
                            else : 
                                raise MemberNoReservations 
                        else : 
                            raise NoReservations
                    
                except NoReservations : 
                    messagebox.showerror(title = "Error!", message = "There are no reservations for this book.")

                except MemberNoReservations : 
                    messagebox.showerror(title = "Error!", message = "Member has no such reservation.")
                    
            #commit
            mydb.commit()
            #close connection
            mydb.close() 

            popup.destroy()
        
        CancelReserveBook_btn = Button(self, text = "Cancel Reservation", command = popupmsg)
        CancelReserveBook_btn.grid(row = 5, column = 1, pady = 10, sticky = "S")

class Fines_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Fines", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #1 Button on this page [ Fine Payment ]
        # [ FinePayment_Page ]

        #Payment Button
        Payment_button = Button(self, text = "Fine Payment", command = lambda : controller.show_frame(FinePayment_Page))
        Payment_button.grid(row = 2, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu))
        BackToMain_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

class FinePayment_Page(tk.Frame) : 
    
    def __init__(self, parent, controller): 
            
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Fine Payment", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
            
        label2 = Label(self, text = "To Pay a Fine, Please Enter Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #Create TextBox for memberID
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 2, column = 1, pady = 3, sticky = "S")

        memberID_label = Label(self, text = "Membership ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 2, column = 0, sticky = "E") 

        #Create TextBox for Payment Date
        paymentDate = Entry(self, width = 30) 
        paymentDate.grid(row = 3, column = 1, pady = 3, sticky = "S")

        paymentDate_label = Label(self, text = "Payment Date (YYYY-MM-DD):", background = "#856ff8", fg = "#fff") 
        paymentDate_label.grid(row = 3, column = 0, sticky = "E") 

        #Create TextBox for Fine Amount
        fineAmount = Entry(self, width = 30) 
        fineAmount.grid(row = 4, column = 1, pady = 3, sticky = "S")

        fineAmount_label = Label(self, text = "Total Fine Amount:", background = "#856ff8", fg = "#fff") 
        fineAmount_label.grid(row = 4, column = 0, sticky = "E") 

        #Back to FinePage
        BackToMain_button = Button(self, text = "Back To Fines Page", command = lambda : controller.show_frame(Fines_Page))
        BackToMain_button.grid(row = 6, column = 1, pady = 10, sticky = "S")

        def popupmsg():
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            paymentDate_insert = paymentDate.get()
            memberID_insert = memberID.get() 
            fineAmount_insert = (fineAmount.get())

            if paymentDate_insert == "" or memberID_insert == "" or fineAmount_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            
            else : 
                class IncorrectFineAmount(Exception) : 
                    pass

                class NoFine(Exception) : 
                    pass 

                try : 
                    with mycursor: 
                        #Get the fineAmount owed by member 
                        data1 = (memberID_insert,)
                        getFineAmount_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s)"""
                        mycursor.execute(getFineAmount_query, data1)
                        record1 = mycursor.fetchall()
                        if len(record1) == 0:
                            raise NoFine
                        else:
                            fineOwed = int(record1[0][0])

                        data2 = (memberID_insert,)
                        getDates_query = """ SELECT paymentDate FROM finepayment WHERE memberID = (%s)"""
                        mycursor.execute(getDates_query, data2)
                        record2 = mycursor.fetchall()

                        allPaymentDates = ()
                        newTuple = map(lambda v: v[0], record2)
                        for x in newTuple:
                            allPaymentDates += (x.strftime('%Y/%m/%d'),)

                        #If member has no Fines 
                        if fineOwed == 0 : 
                            raise NoFine
                        elif paymentDate_insert in allPaymentDates:
                            raise pymysql.err.IntegrityError
                        else :                   
                            #make sure fineAmount_insert == fineOwed
                            if int(fineAmount_insert) != fineOwed : 
                                raise IncorrectFineAmount
                            else : 
                                #Creating popup window
                                popup = Tk()
                                popup.title("Paying Fine Details")
                                popup.geometry("500x500")
                                popup.config(background = "#856ff8")

                                popup_label =  Label(popup, text = "Please Confirm Details to Be Correct", font = LARGEFONT, background = "#856ff8", fg = "#fff")
                                popup_label.pack(pady=10)

                                popup_label =  Label(popup, text = "Exact Fee Only", font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                popup_label.pack(pady=10)
                            
                                #Showing member data
                                membershipID_label =  Label(popup, text = "Member ID: " + memberID.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                membershipID_label.pack(pady=10)

                                paymentDue_label =  Label(popup, text = "Payment Due:$" + fineAmount.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                paymentDue_label.pack(pady=10)

                                paymentnDate_label =  Label(popup, text = "Payment Date: " + paymentDate.get(), font = NORMALFONT, background = "#856ff8", fg = "#fff")
                                paymentnDate_label.pack(pady=10)

                                #Creating buttons
                                confirmPayment_btn = Button(popup, text = "Confirm Payment", command = lambda : PayFines(popup))
                                confirmPayment_btn.pack(pady=10)

                                BackToPayment_btn = Button(popup, text = "Back to Payment Function", command = lambda : popup.destroy())
                                BackToPayment_btn.pack(pady=10)
                            
                                popup.mainloop()

                except NoFine : 
                    messagebox.showerror(title = "Error!", message = "Member has no fine.")
                
                except IncorrectFineAmount : 
                    messagebox.showerror(title = "Error!", message = "Incorrect fine payment amount:\nMember total fine amount is ${fine}\nExact fees only".format(fine = fineOwed))

                except pymysql.err.OperationalError : 
                    messagebox.showerror(title = "Error!", message = "Incorrect Date format. Please enter date in YYYY-MM-DD format.")

                except pymysql.err.IntegrityError :
                    messagebox.showerror(title = "Error!", message = "Member can only pay once per day.")

        def PayFines(popup) : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
                
            #Insert Into Table
            paymentDate_insert = paymentDate.get()
            memberID_insert = memberID.get() 
            fineAmount_insert = (fineAmount.get())

            #If any fields are missing
            if paymentDate_insert == "" or memberID_insert == "" or fineAmount_insert == "": 
                messagebox.showerror(title = "Error!", message = "Missing or incomplete fields.")
            else : 
                class IncorrectFineAmount(Exception) : 
                    pass

                class NoFine(Exception) : 
                    pass 

                try : 
                    with mycursor: 
                        #Get the fineAmount owed by member 
                        data1 = (memberID_insert,)
                        getFineAmount_query = """ SELECT fineAmount FROM Member WHERE memberID = (%s)"""
                        mycursor.execute(getFineAmount_query, data1)
                        record1 = mycursor.fetchall() 
                        if len(record1) == 0:
                            raise NoFine
                        else:
                            fineOwed = int(record1[0][0])

                        data2 = (memberID_insert,)
                        getDates_query = """ SELECT paymentDate FROM finepayment WHERE memberID = (%s)"""
                        mycursor.execute(getDates_query, data2)
                        record2 = mycursor.fetchall()

                        allPaymentDates = ()
                        newTuple = map(lambda v: v[0], record2)
                        for x in newTuple:
                            allPaymentDates += (x.strftime('%Y/%m/%d'),)

                        #If member has no Fines 
                        if fineOwed == 0 : 
                            raise NoFine
                        elif paymentDate_insert in allPaymentDates:
                            raise pymysql.err.IntegrityError
                        else :                   
                            #make sure fineAmount_insert == fineOwed
                            if int(fineAmount_insert) != fineOwed :
                                raise IncorrectFineAmount
                            #Proceed with finepayment : Insert row into Finepayment and change fineAmount to 0 
                            else : 
                                data2 = (memberID_insert, fineAmount_insert, paymentDate_insert)
                                payFine_query = """ INSERT INTO finepayment VALUES(%s, %s, %s) """
                                mycursor.execute(payFine_query, data2)

                                data3 = (0, memberID_insert) 
                                UpdateFine_query = """ UPDATE Member SET fineAmount = (%s) WHERE memberID = (%s) """
                                mycursor.execute(UpdateFine_query, data3)
                                messagebox.showinfo(title = "Success!", message = "Fine successfully paid.")

                except NoFine : 
                    messagebox.showerror(title = "Error!", message = "Member has no fine")
                
                except IncorrectFineAmount : 
                    messagebox.showerror(title = "Error!", message = "Incorrect fine payment amount.")

                except pymysql.err.OperationalError : 
                    messagebox.showerror(title = "Error!", message = "Incorrect Date format. Please enter date in YYYY-MM-DD format.")

                except pymysql.err.IntegrityError :
                    messagebox.showerror(title = "Error!", message = "Member can only pay once per day.")
            
            #Commit 
            mydb.commit()
            mydb.close()

            popup.destroy()

        PayFine_btn = Button(self, text = "Pay Fine", command = popupmsg)
        PayFine_btn.grid(row = 5, column = 1, pady = 10, sticky = "S")

class Reports_Page(tk.Frame) : 

    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Reports", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #5 buttons on this page [ BookSearch, BookOnLoan, BookOnReservation, OutstandingFine, BookOnLoanToMember ]
        # [ BookSearch_Page, BookOnLoan_Page, BookOnReservation_Page, OutstandingFine_Page, BookOnLoanToMember_Page]

        #BookSearch_button
        BookSearch_button = Button(self, text = "Book Search", command = lambda : controller.show_frame(BookSearch_Page))
        BookSearch_button.grid(row = 2, column = 0, pady = 10, sticky = "S")

        #BookOnLoan_button
        BookOnLoan_button = Button(self, text = "Books on Loan", command = lambda : controller.show_frame(BookOnLoan_Page))
        BookOnLoan_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        #BookOnReservation_button
        BookOnReservation_button = Button(self, text = "Books on Reservation", command = lambda : controller.show_frame(BookOnReservation_Page))
        BookOnReservation_button.grid(row = 4, column = 0, pady = 10, sticky = "S")

        #OutstandingFine_button
        OutstandingFine_button = Button(self, text = "Members with Outstanding Fines", command = lambda : controller.show_frame(OutstandingFine_Page))
        OutstandingFine_button.grid(row = 5, column = 0, pady = 10, sticky = "S")

        #BookOnLoanToMember_button
        BookOnLoanToMember_button = Button(self, text = "Books on loan to Member", command = lambda : controller.show_frame(BookOnLoanToMember_Page))
        BookOnLoanToMember_button.grid(row = 6, column = 0, pady = 10, sticky = "S")

        #BackToMain
        BackToMain_button = Button(self, text = "Back To Main Menu", command = lambda : controller.show_frame(MainMenu))
        BackToMain_button.grid(row = 7, column = 0, pady = 10, sticky = "S")

class BookSearch_Page(tk.Frame) : 
    
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Book Search", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))

        label2 = Label(self, text ="To Search Book, Please Enter Requested Information Below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #Creating Textbox to enter Book Row
        title = Entry(self, width = 30)
        title.grid(row = 2, column = 1, sticky = S, pady = 3)

        author = Entry(self, width = 30)
        author.grid(row = 3, column = 1, sticky = S, pady = 3)

        ISBN = Entry(self, width = 30)
        ISBN.grid(row = 4, column = 1, sticky = S, pady = 3)

        publisher = Entry(self, width = 30) 
        publisher.grid(row = 5, column = 1, sticky = S, pady = 3)

        publicationYear = Entry(self, width = 30)
        publicationYear.grid(row = 6, column = 1, sticky = S, pady = 3)
        
        #Creating Textbox Labels
        title_label = Label(self, text = "Book Title:", background = "#856ff8", fg = "#fff") 
        title_label.grid(row = 2, column = 0, sticky = "E")
        
        author_label = Label(self, text = "Authors:", background = "#856ff8", fg = "#fff") 
        author_label.grid(row = 3, column = 0, sticky = "E")

        ISBN_label = Label(self, text = "ISBN:", background = "#856ff8", fg = "#fff") 
        ISBN_label.grid(row = 4, column = 0, sticky = "E")

        publisher_label = Label(self, text = "Publisher:", background = "#856ff8", fg = "#fff") 
        publisher_label.grid(row = 5, column = 0, sticky = "E")

        publicationYear_label = Label(self, text = "Publication Year:", background = "#856ff8", fg = "#fff") 
        publicationYear_label.grid(row = 6, column = 0, sticky = "E")
        
        #BackToReports_Page
        BackToReports_button = Button(self, text = "Back To Reports Menu", command = lambda : controller.show_frame(Reports_Page))
        BackToReports_button.grid(row = 8, column = 1, pady = 10, sticky = "S")

        def Search() : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            #Insert Into Table
            title_insert = title.get()
            author_insert = author.get()
            ISBN_insert = ISBN.get()
            publisher_insert = publisher.get()
            publicationYear_insert = publicationYear.get()

            chosenField = "" 
            breaker = False
            #if more than one field is filled
            if title_insert != "" : 
                if (author_insert != "" or ISBN_insert != "" or publisher_insert != "" or publicationYear_insert != "") : 
                    messagebox.showerror(title = "Error!", message = "Please only fill in one of the search categories.")
                    breaker = True
                
                elif (" " in title_insert) or ("," in title_insert) : 
                    messagebox.showerror(title = "Error!", message = "Only One Word is allowed in the search box.")
                    breaker = True
                    
                else : 
                    chosenField = title_insert

            elif author_insert != "" :
                if (title_insert != "" or ISBN_insert != "" or publisher_insert != "" or publicationYear_insert != "") : 
                    messagebox.showerror(title = "Error!", message = "Please only fill in one of the search categories.")
                    breaker = True
                
                elif (" " in author_insert) or ("," in author_insert) : 
                    messagebox.showerror(title = "Error!", message = "Only One Word is allowed in the search box.")
                    breaker = True

                else : 
                    chosenField = author_insert

            elif ISBN_insert != "" :
                if (title_insert != "" or author_insert != "" or publisher_insert != "" or publicationYear_insert != "") : 
                    messagebox.showerror(title = "Error!", message = "Please only fill in one of the search categories.")
                    breaker = True
                
                elif (" " in ISBN_insert) or ("," in ISBN_insert) : 
                    messagebox.showerror(title = "Error!", message = "Only One Word is allowed in the search box.")
                    breaker = True

                else : 
                    chosenField = ISBN_insert

            elif publisher_insert != "" :
                if (title_insert != "" or author_insert != "" or ISBN_insert != "" or publicationYear_insert != "") : 
                    messagebox.showerror(title = "Error!", message = "Please only fill in one of the search categories.")
                    breaker = True

                elif (" " in publisher_insert) or ("," in publisher_insert) : 
                    messagebox.showerror(title = "Error!", message = "Only One Word is allowed in the search box.")
                    breaker = True

                else : 
                    chosenField = publisher_insert

            elif publicationYear_insert != "" :
                if (title_insert != "" or author_insert != "" or ISBN_insert != "" or publisher_insert != "") : 
                    messagebox.showerror(title = "Error!", message = "Please only fill in one of the search categories.")
                    breaker = True

                elif (" " in publicationYear_insert) or ("," in publicationYear_insert) : 
                    messagebox.showerror(title = "Error!", message = "Only One Word is allowed in the search box.")
                    breaker = True

                else : 
                    chosenField = publicationYear_insert

            if chosenField == "" and breaker == False : 
                messagebox.showerror(title = "Error!", message = "Search Fields are empty. Please Fill in One search Field with a word.")

            elif chosenField != "" and breaker == False : 
                record1 = "" #Placeholder to declare variable
                if chosenField == title_insert :
                    #Search based on title :
                    
                    titlestring1 = '\\b' + title_insert + '\\b'
                    titlestring2 = title_insert
                    data1 = (titlestring1,titlestring2)
                    titleSearch_query = ( """ SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                            FROM 
                                            (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, a.authors 
                                            FROM 
                                            book b, 
                                            (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                            FROM bookhasauthor
                                            GROUP BY accessionNumber) a
                                            WHERE b.accessionNumber = a.accessionNumber) c
                                            WHERE title REGEXP %s  or title = %s """ )
                    
                    mycursor.execute(titleSearch_query, data1)
                    record1 = mycursor.fetchall() #list of lists [ [-Book1-], [-Book2-], .... ]

                elif chosenField == author_insert : 
                    #Search based on authorName
                    
                    authorstring1 = '\\b' + author_insert + '\\b'
                    authorstring2 = author_insert
                    data1 = (authorstring1, authorstring2)
                    authorSearch_query = ( """ SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                            FROM 
                                            (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, a.authors 
                                            FROM 
                                            book b, 
                                            (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                            FROM bookhasauthor
                                            GROUP BY accessionNumber) a
                                            WHERE b.accessionNumber = a.accessionNumber) c
                                            WHERE authors REGEXP %s or authors = %s """ )

                    mycursor.execute(authorSearch_query, data1)
                    record1 = mycursor.fetchall() #list of lists [ [-Book1-], [-Book2-], .... ]
                
                elif chosenField == ISBN_insert : 
                    #Search based on ISBN
                    
                    data1 = (ISBN_insert,)
                    ISBNSearch_query = ( """ SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                            FROM 
                                            (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, a.authors 
                                            FROM 
                                            book b, 
                                            (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                            FROM bookhasauthor
                                            GROUP BY accessionNumber) a
                                            WHERE b.accessionNumber = a.accessionNumber) c
                                            WHERE ISBN = (%s) """ )
                    
                    mycursor.execute(ISBNSearch_query, data1)
                    record1 = mycursor.fetchall() #list of lists [ [-Book1-], [-Book2-], .... ]
                
                elif chosenField == publisher_insert : 
                    #Search based on publisherName

                    publisherstring1 = '\\b' + publisher_insert + '\\b'
                    publisherstring2 = publisher_insert
                    data1 = (publisherstring1, publisherstring2 )
                    publisherSearch_query = ( """ SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                            FROM 
                                            (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, a.authors 
                                            FROM 
                                            book b, 
                                            (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                            FROM bookhasauthor
                                            GROUP BY accessionNumber) a
                                            WHERE b.accessionNumber = a.accessionNumber) c
                                            WHERE publisherName REGEXP %s or publisherName = %s """ )

                    mycursor.execute(publisherSearch_query, data1)
                    record1 = mycursor.fetchall() #list of lists [ [-Book1-], [-Book2-], .... ]
                
                elif chosenField == publicationYear_insert :
                    #Search based on publicationYear 
                    data1 = (publicationYear_insert,)
                    publicationYearSearch_query = ( """ SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                            FROM 
                                            (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, a.authors 
                                            FROM 
                                            book b, 
                                            (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                            FROM bookhasauthor
                                            GROUP BY accessionNumber) a
                                            WHERE b.accessionNumber = a.accessionNumber) c
                                            WHERE publicationYear = (%s) """ )

                    mycursor.execute(publicationYearSearch_query, data1)
                    record1 = mycursor.fetchall() #list of lists [ [-Book1-], [-Book2-], .... ]
                
                try : 
                    global pop
                    pop = Toplevel(app) 
                    pop.title = ("Search Results")
                    tree = Treeview(pop)
                    tree['show'] = 'headings'
                    with mycursor : 
                        #Define number of columns
                        tree["columns"] = ("accessionNumber", "title", "ISBN", "publicationYear", "publisherName", "authors")

                        #Assign the width, mindith and anchor 
                        tree.column("accessionNumber", width = 150, minwidth = 50, anchor = tk.CENTER)
                        tree.column("title", width = 150, minwidth = 150, anchor = tk.CENTER)
                        tree.column("ISBN", width = 150, minwidth = 150, anchor = tk.CENTER)
                        tree.column("publicationYear", width = 200, minwidth = 50, anchor = tk.CENTER)
                        tree.column("publisherName", width = 200, minwidth = 50, anchor = tk.CENTER)
                        tree.column("authors", width = 300, minwidth = 150, anchor = tk.CENTER)

                        #Assign Heading names
                        tree.heading("accessionNumber", text = "Accession Number", anchor = tk.CENTER)
                        tree.heading("title", text = "Title", anchor = tk.CENTER)
                        tree.heading("ISBN", text = "ISBN", anchor = tk.CENTER)
                        tree.heading("publicationYear", text = "Publication Year", anchor = tk.CENTER)
                        tree.heading("publisherName", text = "Publisher Name", anchor = tk.CENTER)
                        tree.heading("authors", text = "Authors", anchor = tk.CENTER)

                        i = 0
                        for row in record1 : 
                            tree.insert('',i, text='', values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                            i = i + 1
                        
                        tree.pack() 
                
                except IndexError :
                     messagebox.showerror(title = "Error!", message = "Error.")

            #commit
            mydb.commit()
            #close connection
            mydb.close() 

        searchBook_btn = Button(self, text = "Search Book", command = Search)
        searchBook_btn.grid(row = 7, column = 1, pady = 10, sticky = "S")

class BookOnLoan_Page(tk.Frame) : 
    #Get all the books where memberID != None 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label = Label(self, text ="Search for Books Currently on Loan", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #BacktoReports
        BackToReports_button = Button(self, text = "Back To Reports Menu", command = lambda : controller.show_frame(Reports_Page))
        BackToReports_button.grid(row = 3, column = 1, pady = 10, sticky = "S")

        def SearchLoan() : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            searchLoan_query = (""" SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                    FROM 
                                    (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, b.memberID, a.authors 
                                    FROM 
                                    book b, 
                                    (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                    FROM bookhasauthor
                                    GROUP BY accessionNumber) a
                                    WHERE b.accessionNumber = a.accessionNumber) c
                                    WHERE memberID IS NOT Null """)
            
            mycursor.execute(searchLoan_query)
            record1 = mycursor.fetchall() 
            
            global pop
            pop = Toplevel(app) 
            pop.title = ("Search Results")
            tree = Treeview(pop)
            tree['show'] = 'headings'

            #Define number of columns
            tree["columns"] = ("accessionNumber", "title", "ISBN", "publicationYear", "publisherName", "authors")

            #Assign the width, mindith and anchor 
            tree.column("accessionNumber", width = 150, minwidth = 50, anchor = tk.CENTER)
            tree.column("title", width = 150, minwidth = 150, anchor = tk.CENTER)
            tree.column("ISBN", width = 150, minwidth = 150, anchor = tk.CENTER)
            tree.column("publicationYear", width = 200, minwidth = 50, anchor = tk.CENTER)
            tree.column("publisherName", width = 200, minwidth = 50, anchor = tk.CENTER)
            tree.column("authors", width = 300, minwidth = 150, anchor = tk.CENTER)

            #Assign Heading names
            tree.heading("accessionNumber", text = "Accession Number", anchor = tk.CENTER)
            tree.heading("title", text = "Title", anchor = tk.CENTER)
            tree.heading("ISBN", text = "ISBN", anchor = tk.CENTER)
            tree.heading("publicationYear", text = "Publication Year", anchor = tk.CENTER)
            tree.heading("publisherName", text = "Publisher Name", anchor = tk.CENTER)
            tree.heading("authors", text = "Authors", anchor = tk.CENTER)

            i = 0
            for row in record1 : 
                tree.insert('',i, text='', values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                i = i + 1
                        
            tree.pack()             
            
            #commit
            mydb.commit()
            #close connection
            mydb.close() 

        searchLoan_btn = Button(self, text = "Search for Books on Loan", command = SearchLoan)
        searchLoan_btn.grid(row = 2, column = 1, pady = 10, sticky = "S")
    
class BookOnReservation_Page(tk.Frame) : 
    #Get all the books where numOfReservation > 0 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Search for Books Currently on Reservation", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #BacktoReports
        BackToReports_button = Button(self, text = "Back To Reports Menu", command = lambda : controller.show_frame(Reports_Page))
        BackToReports_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        def SearchReserve() : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            Reserve_query = ( """ SELECT br.accessionNumber, b.title, br.memberID, concat(m.fName,' ',IFNULL(m.lName, '')) AS MemberName
                                FROM book b, Member m, bookhasreservation br
                                WHERE b.numOfReservations > 0 AND m.memberID = br.memberID AND br.accessionNumber = b.accessionNumber """)
            
            mycursor.execute(Reserve_query)
            record1 = mycursor.fetchall() 
            
            global pop
            pop = Toplevel(app) 
            pop.title = ("Search Results")
            tree = Treeview(pop)
            tree['show'] = 'headings'

            #Define number of columns
            tree["columns"] = ("accessionNumber", "title", "memberID", "MemberName")

            #Assign the width, mindith and anchor 
            tree.column("accessionNumber", width = 150, minwidth = 50, anchor = tk.CENTER)
            tree.column("title", width = 150, minwidth = 150, anchor = tk.CENTER)
            tree.column("memberID", width = 150, minwidth = 150, anchor = tk.CENTER)
            tree.column("MemberName", width = 200, minwidth = 50, anchor = tk.CENTER)

            #Assign Heading names
            tree.heading("accessionNumber", text = "Accession Number", anchor = tk.CENTER)
            tree.heading("title", text = "Title", anchor = tk.CENTER)
            tree.heading("memberID", text = "MembershipID", anchor = tk.CENTER)
            tree.heading("MemberName", text = "MemberName", anchor = tk.CENTER)

            i = 0
            for row in record1 : 
                tree.insert('',i, text='', values = (row[0],row[1],row[2],row[3]))
                i = i + 1
                        
            tree.pack()             
            
            #commit
            mydb.commit()
            #close connection
            mydb.close() 

        searchReserve_btn = Button(self, text = "Search for Books on Reserve", command = SearchReserve)
        searchReserve_btn.grid(row = 2, column = 0, pady = 10, sticky = "S")

class OutstandingFine_Page(tk.Frame) : 
    #Get all the members where fineamount > 0 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        label = Label(self, text ="Search for Members with Outstanding Fines", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 0, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 0, padx = 10, pady= 10)

        #BacktoReports
        BackToReports_button = Button(self, text = "Back To Reports Menu", command = lambda : controller.show_frame(Reports_Page))
        BackToReports_button.grid(row = 3, column = 0, pady = 10, sticky = "S")

        def SearchMemberFines() : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()

            memberFine_query = (""" SELECT memberID, concat(fName,' ',IFNULL(lName, '')) AS MemberName, faculty, phone, eMail
                                    FROM member
                                    WHERE fineAmount > 0 """)
            
            mycursor.execute(memberFine_query)
            record1 = mycursor.fetchall()
            
            #Creating Popup
            global pop
            pop = Toplevel(app) 
            pop.title = ("Search Results")
            tree = Treeview(pop)
            tree['show'] = 'headings'

            #Define number of columns
            tree["columns"] = ("memberID", "name", "faculty", "phone", "eMail")

            #Assign the width, mindith and anchor 
            tree.column("memberID", width = 150, minwidth = 50, anchor = tk.CENTER)
            tree.column("name", width = 200, minwidth = 150, anchor = tk.CENTER)
            tree.column("faculty", width = 150, minwidth = 150, anchor = tk.CENTER)
            tree.column("phone", width = 200, minwidth = 50, anchor = tk.CENTER)
            tree.column("eMail", width = 250, minwidth = 50, anchor = tk.CENTER)

            #Assign Heading names
            tree.heading("memberID", text = "MembershipID", anchor = tk.CENTER)
            tree.heading("name", text = "Name", anchor = tk.CENTER)
            tree.heading("faculty", text = "Faculty", anchor = tk.CENTER)
            tree.heading("phone", text = "Phone Number", anchor = tk.CENTER)
            tree.heading("eMail", text = "Email Address", anchor = tk.CENTER)

            i = 0
            for row in record1 : 
                tree.insert('',i, text='', values = (row[0],row[1],row[2],row[3],row[4]))
                i = i + 1
                        
            tree.pack()             
            
            #commit
            mydb.commit()
            #close connection
            mydb.close() 

        searchMemberFines_btn = Button(self, text = "Search for Member with Outstanding Fines", command = SearchMemberFines)
        searchMemberFines_btn.grid(row = 2, column = 0, pady = 10, sticky = "S")

class BookOnLoanToMember_Page(tk.Frame) : 
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent)
        #Change background color
        self.configure(background = "#856ff8")

        #Make the window sticky for every case
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        label = Label(self, text ="Search for Books Currently on Loan to Member", font = LARGEFONT, background = "#856ff8", fg = "#fff")
        label.grid(row = 0, column = 1, sticky = S, pady = (30,0))
        
        label2 = Label(self, text = "Select one of the Options below:", font = NORMALFONT, background = "#856ff8", fg = "#fff")
        label2.grid(row = 1, column = 1, sticky = S, pady= 10)

        #TextBox to enter MemberID to find book on loan to member
        memberID = Entry(self, width = 30) 
        memberID.grid(row = 2, column = 1, pady = 3, sticky = "S")

        memberID_label = Label(self, text = "Member ID:", background = "#856ff8", fg = "#fff") 
        memberID_label.grid(row = 2, column = 0, stick = "E")

        #BacktoReports
        BackToReports_button = Button(self, text = "Back To Reports Menu", command = lambda : controller.show_frame(Reports_Page))
        BackToReports_button.grid(row = 4, column = 1, pady = 10, sticky = "S")

        def SearchBookMember() : 
            #Connect to database
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="PlaceholderPassword",
            database="librarysystem"
            )
            #Create Cursor
            mycursor = mydb.cursor()
            memberID_insert = memberID.get()

            if memberID_insert == "" : 
                messagebox.showerror(title = "Error!", message = "Missing MemberID field.")
            
            else : 
                try : 
                    with mycursor: 
                        
                        data1 = (memberID_insert,)
                        MemberBooks_query = ("""SELECT c.accessionNumber, c.title, c.ISBN, c.publicationYear, c.publisherName, c.authors
                                                FROM 
                                                (SELECT b.accessionNumber, b.title, b.ISBN, b.publicationYear, b.publisherName, b.memberID, a.authors 
                                                FROM 
                                                book b, 
                                                (SELECT accessionNumber, GROUP_CONCAT(authorName) as "authors"
                                                FROM bookhasauthor
                                                GROUP BY accessionNumber) a
                                                WHERE b.accessionNumber = a.accessionNumber) c
                                                WHERE memberID = (%s) """)
                        
                        mycursor.execute(MemberBooks_query,data1)
                        record1 = mycursor.fetchall()
                        
                        global pop
                        pop = Toplevel(app) 
                        pop.title = ("Search Results")
                        tree = Treeview(pop)
                        tree['show'] = 'headings'

                        #Define number of columns
                        tree["columns"] = ("accessionNumber", "title", "ISBN", "publicationYear", "publisherName", "authors")

                        #Assign the width, mindith and anchor 
                        tree.column("accessionNumber", width = 150, minwidth = 50, anchor = tk.CENTER)
                        tree.column("title", width = 150, minwidth = 150, anchor = tk.CENTER)
                        tree.column("ISBN", width = 150, minwidth = 150, anchor = tk.CENTER)
                        tree.column("publicationYear", width = 200, minwidth = 50, anchor = tk.CENTER)
                        tree.column("publisherName", width = 200, minwidth = 50, anchor = tk.CENTER)
                        tree.column("authors", width = 300, minwidth = 150, anchor = tk.CENTER)

                        #Assign Heading names
                        tree.heading("accessionNumber", text = "Accession Number", anchor = tk.CENTER)
                        tree.heading("title", text = "Title", anchor = tk.CENTER)
                        tree.heading("ISBN", text = "ISBN", anchor = tk.CENTER)
                        tree.heading("publicationYear", text = "Publication Year", anchor = tk.CENTER)
                        tree.heading("publisherName", text = "Publisher Name", anchor = tk.CENTER)
                        tree.heading("authors", text = "Authors", anchor = tk.CENTER)

                        i = 0
                        for row in record1 : 
                            tree.insert('',i, text='', values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                            i = i + 1
                                    
                        tree.pack()             
                                        
                except IndexError : 
                    messagebox.showerror(title = "Error!", message = "Member does not exist.")

            #commit
            mydb.commit()
            #close connection
            mydb.close() 

        searchBookMember_btn = Button(self, text = "Search for Books on Loan to Member", command = SearchBookMember)
        searchBookMember_btn.grid(row = 3, column = 1, pady = 10, sticky = "S")       

app = MainFrame()
app.title('ALS')
app.mainloop()
