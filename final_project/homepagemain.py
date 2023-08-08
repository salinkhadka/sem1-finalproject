from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import ast
from tkinter import messagebox

root = Tk()
root.title("Hamrorootuits(Home)")
root.geometry("1536x864")
root.resizable(1,1)
root.iconbitmap("aa.ico")
bgimg = Image.open("orgbackground2.png")
resizedbg = bgimg.resize((1525,800))
converted_image=ImageTk.PhotoImage(resizedbg)
background = Label(root, image=converted_image)
background.place(x=0,y=0)
  
# conn=sqlite3.connect("employee.db")
# c=conn.cursor()
# c.execute(""" CREATE TABLE registration(
#     fullname,
#     email,
#     dob,
#     username,
#     password
# )
# """)





def logeen():
    li = Toplevel()
    li.title('Login')
    li.resizable(0, 0)
    li.geometry("1435x850")
    li.iconbitmap("aa.ico")

    my_image = Image.open("login1.png")
    resized_image = my_image.resize((1435, 850))
    converted_image = ImageTk.PhotoImage(resized_image)
    my_label = Label(li, image=converted_image)
    my_label.pack()
    def ram(event):
        if username_entry.get()=='Username':
            username_entry.delete(0,END)
        elif username_entry.get() == '':
            username_entry.insert(0,'Username')
    def ram1(event):
        if password_entry.get()=='Password':
            password_entry.delete(0,END)
        elif password_entry.get() == '':
            password_entry.insert(0,'Password')
    def hide():
        open_eye.config(file='closeye.png')
        password_entry.config(show='*')
        eye_button.config(command=show)
    def show():
        open_eye.config(file='openeye.png')
        password_entry.config(show='')
        eye_button.config(command=hide)
    def verify():
        from tkinter import messagebox
        username = username_entry.get()
        password = password_entry.get()
        try:
            conn=sqlite3.connect("employee.db")
            c=conn.cursor()
            c.execute("SELECT *,oid FROM registration WHERE username =? and password = ?",[username,password])
            record=c.fetchone()
            if(record is None and username !='admin'):
                raise BaseException ("Username or password is not correct")
            elif(record  is not None and username !='admin'):    
            # print(records)
                 messagebox.showinfo("login","logged in sucessfully")


                 dash=Toplevel()
                 dash.iconbitmap("aa.ico")
                 def checkout(row_id):
                    # Function to handle the "Checkout" button click
                    conn = sqlite3.connect("order_details.db")
                    c = conn.cursor()

                    c.execute("DELETE FROM orders WHERE oid=?", (row_id,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("User","sucessfully checked-out")
                    query()

                 def query():
                    # print("apple")
                    conn = sqlite3.connect("order_details.db")
                    c = conn.cursor()

                    c.execute("SELECT *, oid FROM orders")
                    records = c.fetchall()

                    i = 2
                    col = [0, 1, 2, 3, 4, 5]
                    # row_ids = []
                    for record in records:
                        row_id = record[-1]  # Assuming the last column is the primary key (oid)


                        for j in col:
                            output = Label(frame, text=record[j])
                            output.grid(row=i, column=col[j])


                        # Create and associate the "Checkout" button with the current row
                        check = Button(frame, text="Check-out", command=lambda row_id=row_id: checkout(row_id))
                        check.grid(row=i, column=6)



                        i += 1
                    conn.commit()
                    conn.close()

                 # Define image
                 my_image = Image.open("dashboard.png")  # Enter picture name here
                 resized_image = my_image.resize((1435, 850))
                 converted_image = ImageTk.PhotoImage(resized_image)
                 my_label = Label(dash, image=converted_image)
                 my_label.grid()

                 # Creating a frame to contain the Gmail label
                 frame = Frame(dash,width=50,height=50, bg='white')  # Set a background color for the frame
                 frame.place(x=220,y=120)
                 # frame1 = Frame(frame,width=100,height=350, bg='black')  # Set a background color for the frame
                 # frame1.place(x=220,y=120)
                 Name=Label(frame,text='Name',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 Name.grid(row=0,column=0,pady=25)

                 quantity=Label(frame,text='Location',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 quantity.grid(row=0,column=1,padx=25) 

                 Location=Label(frame,text='Contact Details',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 Location.grid(row=0,column=2,padx=25)

                 contact_number=Label(frame,text='Items',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 contact_number.grid(row=0,column=3,padx=25)








                 Items=Label(frame,text='Quantity',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 Items.grid(row=0,column=4,padx=25)

                 oid=Label(frame,text='OID',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 oid.grid(padx=25,row=0,column=5)


                 button=Label(frame,text='button',font=('AkayaTelivigala',20)
                  , fg='firebrick1')
                 button.grid(row=0,column=6)
                 show_records=Button(frame,text="Show Records",command=query)
                 show_records.grid(row=1,column=6)
                 dash.mainloop()
                 


            elif username=="admin" and password=="admin" :
                    ad=Toplevel()
                    ad.title('Admin Dashboard')
                    ad.resizable(0, 0)
                    ad.geometry("1435x850")
                    ad.iconbitmap("aa.ico")

                    def checkout(row_id):
                        # Function to handle the "Checkout" button click
                        conn = sqlite3.connect("employee.db")
                        c = conn.cursor()

                        c.execute("DELETE FROM registration WHERE oid=?", (row_id,))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("admin","sucessfully deleted")
                        query()

                    def query():
                        # print("apple")
                        conn = sqlite3.connect("employee.db")
                        c = conn.cursor()

                        c.execute("SELECT *, oid FROM registration")
                        records = c.fetchall()

                        i = 2
                        col = [0, 1, 2, 3, 4, 5]
                        # row_ids = []
                        for record in records:
                            row_id = record[-1]  # Assuming the last column is the primary key (oid)


                            for j in col:
                                output = Label(frame, text=record[j])
                                output.grid(row=i, column=col[j])


                            # Create and associate the "Checkout" button with the current row
                            check = Button(frame, text="delete", command=lambda row_id=row_id: checkout(row_id))
                            check.grid(row=i, column=6)



                            i += 1
                        conn.commit()
                        conn.close()

                    # Define image
                    image_path = "dashboard.png"
                    my_image = Image.open(image_path)  # Enter picture name here
                    resized_image = my_image.resize((1435, 850))
                    convertedd_image = ImageTk.PhotoImage(resized_image)
                    my_label= Label( ad , image=convertedd_image)
                    my_label.grid()

                    # Creating a frame to contain the Gmail label
                    frame = Frame(ad,width=50,height=50, bg='white')  # Set a background color for the frame
                    frame.place(x=220,y=120)
                    # frame1 = Frame(frame,width=100,height=350, bg='black')  # Set a background color for the frame
                    #frame1.place(x=220,y=120)
                    Name=Label(frame,text='Name',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    Name.grid(row=0,column=0,pady=25)

                    quantity=Label(frame,text='E-mail',font=('AkayaTelivigala',20)
                                , fg='firebrick1')
                    quantity.grid(row=0,column=1,padx=25)

                    Location=Label(frame,text='DOB',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    Location.grid(row=0,column=2,padx=25)

                    contact_number=Label(frame,text='Username',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    contact_number.grid(row=0,column=3,padx=25)








                    Items=Label(frame,text='Password',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    Items.grid(row=0,column=4,padx=25)

                    oid=Label(frame,text='Employee-Id',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    oid.grid(padx=25,row=0,column=5)


                    button=Label(frame,text='button',font=('AkayaTelivigala',20)
                                 , fg='firebrick1')
                    button.grid(row=0,column=6)
                    show_records=Button(frame,text="Show Records",command=query)
                    show_records.grid(row=1,column=6)


                    ad.mainloop()

                    
            # else:
            #         messagebox.showerror("signin","Invalid username or password")
        except BaseException as m:
                messagebox.showerror(title="Error",message=str(m))

            




    def signup():
        su = Toplevel()
        su.iconbitmap("aa.ico")
        su.title("Signup")
        su.geometry("1435x850")
        su.resizable(0, 0)

    





        my_image=Image.open("login1.png")#Enter picture name here
        resized_image=my_image.resize((1435,850))
        coverted_image=ImageTk.PhotoImage(resized_image)
        mylabel=Label(su, image=coverted_image)
        mylabel.pack()


        def confirm():
            from tkinter import messagebox
            conn=sqlite3.connect("employee.db")
            c=conn.cursor()
            c.execute("INSERT INTO registration VALUES (:fullname,:email,:dob,:username,:password)",{
            "fullname":fullnameentry.get(),
            "email":emailentry.get(),
            "dob":dobentry.get(),
            "username":usernameentry.get(),
            "password":Passwordentry.get()
       
    })
            conn.commit()
            conn.close()


            if fullnameentry.get()=='' or emailentry.get()=='' or dobentry.get()=='' or usernameentry.get()=='' or Passwordentry.get()=='':
                messagebox.showerror("signup", "one or more fields are empty")
            elif '@gmail.com' not in emailentry.get() and emailentry.get()=='':
                messagebox.showerror("Sign up","E-mail must contail @gmail.com")
            elif len(Passwordentry.get())<7:
                messagebox.showerror("Sign up","password's length must be at least 8")
            elif not any(char.isdigit() for char in Passwordentry.get()) or not any(char.isalpha() for char in Passwordentry.get()):
                messagebox.showerror("Sign up", "Password must contain at least one letter and one number")
            elif var.get()==0:
                messagebox.showerror("signup","please accept our terms and conditions to sign up")


            else:



                # Clear the input fields after successful registration
                emailentry.delete(0, END)
                usernameentry.delete(0, END)
                fullnameentry.delete(0, END)
                dobentry.delete(0, END)
                Passwordentry.delete(0, END)

                messagebox.showinfo("Sign in", "Signed up successfully")
                su.destroy()




        fullname=Label(su,text='Name',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
        fullname.place(x=120,y=370-60)

        fullnameentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
        fullnameentry.place(x=122,y=400-60)

        email=Label(su,text='E-mail',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
        email.place(x=120,y=430-60)

        emailentry=Entry(su,width=25,font=('AkayaTelivigala',14)
                ,bg='firebrick1' , fg='white')
        emailentry.place(x=122,y=380+70+10-60)

        dob=Label(su,text='Date Of Birth',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
        dob.place(x=120,y=490-60)

        dobentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
        dobentry.place(x=122,y=520-60)

        username=Label(su,text='Username',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
        username.place(x=120,y=550-60)

        usernameentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
        usernameentry.place(x=122,y=580-60)

        Password=Label(su,text='Password',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
        Password.place(x=120,y=550)

        Passwordentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
        Passwordentry.place(x=122,y=580)

        var=IntVar()

        terms=Checkbutton(su,text='I agree to the Terms & Conditions',font=('AkayaTelivigala',12)
            ,bg='white' , fg='firebrick1',variable=var) 
        terms.place(x=120,y=620)

        login=Button(su,width=11,text='Signup',font=('Open Sans',25,'bold')
             ,fg='white',bg='firebrick1',activebackground='white',cursor='hand2',bd=0,command=confirm)
        login.place(x=110,y=650)


        su.mainloop()
    def fp():
        def cps():
            if(password_change.get()!="" or len(password_change.get())<8):
                messagebox.showerror("Password Error","Password must be more than 8 letters")
            else:   
                conn=sqlite3.connect("employee.db")
                c=conn.cursor()
                c.execute("""UPDATE registration SET 

                password=:password
                WHERE email= :email""",
                {
                
                    "password":password_change.get(),
                    "email":email1.get()





                })
                conn.commit()
                conn.close()
                messagebox.showinfo("sucessful","sucessfully changed password")
        
        def save():
            global password_change
            conn=sqlite3.connect("employee.db")
            c=conn.cursor()
            c.execute("SELECT *FROM registration")
            records=c.fetchall()
            print(records)
            for record in records:
                if str(record[0])==fullname1.get() and str(record[1])==email1.get() and str(record[2])==dob1.get() and str(record[3])==username1.get():
                    changepass=Toplevel()
                    changepass.title("change password")
                    password_edit=Label(changepass,text="Password")
                    password_edit.grid(row=0,column=1)
                    password_change=Entry(changepass)
                    password_change.grid(row=0,column=2)
                    
                    updt=Button(changepass,text="save",padx=20,command=cps)
                    updt.grid(row=1,column=1)


                     
                    break
            else:
                   messagebox.showerror("Recover Password","Your user details donot match")











        app=Toplevel()
        global fullname1,email1,dob1,username1


        
        name_edit=Label(app,text="Name")
        name_edit.grid(row=1,column=1)
        fullname1=Entry(app)
        fullname1.grid(row=1,column=2)


        email_edit=Label(app,text="Email")
        email_edit.grid(row=2,column=1)
        email1=Entry(app)
        email1.grid(row=2,column=2)

        dob_edit=Label(app,text="Date Of Birth")
        dob_edit.grid(row=3,column=1)
        dob1=Entry(app)
        dob1.grid(row=3,column=2)

        username_edit=Label(app,text="Username")
        username_edit.grid(row=4,column=1)
        username1=Entry(app)
        username1.grid(row=4,column=2)

        # password_edit=Label(app,text="Password")
        # password_edit.grid(row=5,column=1)
        # password1=Entry(app)
        # password1.grid(row=5,column=2)





        updt=Button(app,text="save",padx=20,command=save)
        updt.grid(row=6,column=1)
        

            





    

    username_entry = Entry(li, width=25, font=('AkayaTelivigala', 18), bg='white', fg='firebrick1', bd=0)
    username_entry.place(x=120, y=250 + 100)
    username_entry.insert(0, 'Username')
    username_entry.bind('<FocusIn>', ram)
    username_entry.bind('<FocusOut>', ram)

    Frame(li, width=255, height=2, bg='firebrick1').place(x=120, y=295 + 100)

    password_entry = Entry(li, width=25, font=('AkayaTelivigala', 18), bg='white', fg='firebrick1', bd=0)
    password_entry.place(x=120, y=300 + 100)
    password_entry.insert(0, 'Password')
    password_entry.bind('<FocusIn>', ram1)
    password_entry.bind('<FocusOut>', ram1)

    Frame(li, width=255, height=2, bg='firebrick1').place(x=120, y=345 + 100)

    forgot_button = Button(li, width=11, text='Forgot Password?', bd=0, bg='white', activebackground='white',cursor='hand2', padx=20, font=('AkayaTelivigala', 11),command=fp)
    forgot_button.place(x=280, y=350 + 100)

    open_eye = PhotoImage(file='openeye.png')
    eye_button = Button(li, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
    eye_button.place(x=340, y=305 + 100)

    login_button = Button(li, width=11, text='Login', font=('Open Sans', 36, 'bold'), fg='white', bg='firebrick1',activebackground='white', cursor='hand2', bd=0 ,command=verify)
    login_button.place(x=100, y=380 + 125)

    signup_label = Label(li, text='Don\'t have an account?', font=('Open Sans', 15), fg='firebrick1', bg='white')
    signup_label.place(x=125, y=380 + 200 + 50)

    signup_button = Button(li, width=8, text='Create new one', font=('Open Sans', 15), fg='blue', bg='white',activebackground='blue', padx=25, cursor='hand2', bd=0, command=signup)
    signup_button.place(x=135, y=380 + 200 + 80)

    li.mainloop()


#customer portal
def customer_pp():
    cp=Toplevel()
    cp.iconbitmap("aa.ico")
    cp.title("Customer-order")
    cp.geometry("900x700")
    cp.resizable(0, 0)
    # define image
    my_image = Image.open('iio.png')
    resized_image = my_image.resize((900, 700))
    converted_img = ImageTk.PhotoImage(resized_image)
    mylabel=Label(cp,image=converted_img)
    mylabel.pack()

    # entry for Name
    a1 = Entry(cp, font=("bold", 15), width=20, bd=0, borderwidth=0)
    a1.place(x=170, y=225)

    # entry for Location
    a2 = Entry(cp, font=("bold", 15), width=20, borderwidth=0)
    a2.place(x=170, y=350)

    # entry for quantity
    a3 = Entry(cp, font=("bold", 15), width=10, borderwidth=0)
    a3.place(x=580, y=225)

    # entry for Contact number
    a4 = Entry(cp, font=("bold", 15), width=17, borderwidth=0)
    a4.place(x=685, y=350)

    # button
    a6 = Button(cp, text='Confirm', width=10, borderwidth=0, font=('bold', 15), fg='black', bg='gray')
    a6.place(x=365, y=535)


    # combobox
    options = ['1. Apple', '2. Mango', '3. Banana', '4. Litchi', '5. Watermelon', '6. Papaya', "7. Guava", "8. Jack fruit"]
    cb1 = ttk.Combobox(cp, values=options, width=17, font=("Arial", 15))
    cb1.place(x=550, y=450)



    #Edit option
    t_edit=Label(cp,text="To edit your order please Enter your order-id here and click the edit button.",font=('italic',10),fg='black')
    t_edit.place(x=50,y=650)
    e_entry=Entry(cp)
    e_entry.place(x=500,y=650)
    edit3=Button(cp,text="Edit")
    edit3.place(x=625,y=650)



    def edit():
        global name_edit1,location1,phonenumber1,item1,quantity1
        app=Toplevel()



        conn=sqlite3.connect("order_details.db")
        c=conn.cursor()
        record_id=e_entry.get()


        c.execute("SELECT *FROM orders WHERE oid="+ e_entry.get())
        records=c.fetchall()


        name_edit2=Label(app,text="name")
        name_edit2.grid(row=1,column=1)
        name_edit1=Entry(app)
        name_edit1.grid(row=1,column=2)


        # age_edit=Label(app,text="age")
        # age_edit.grid(row=2,column=1)
        # age_edit1=Entry(app)
        # age_edit1.grid(row=2,column=2)

        location2=Label(app,text="Location")
        location2.grid(row=3,column=1)
        location1=Entry(app)
        location1.grid(row=3,column=2)

        Phonenumber2=Label(app,text="Phonenumber")
        Phonenumber2.grid(row=4,column=1)
        phonenumber1=Entry(app)
        phonenumber1.grid(row=4,column=2)

        item2=Label(app,text="item")
        item2.grid(row=5,column=1)
        item1=Entry(app)
        item1.grid(row=5,column=2)

        quantity2=Label(app,text="quantity")
        quantity2.grid(row=6,column=1)
        quantity1=Entry(app)
        quantity1.grid(row=6,column=2)

        updt=Button(app,text="save",padx=20,command=update)
        updt.grid(row=9,column=1)

        for record in records:
            name_edit1.insert(0,record[0])
            location1.insert(0,record[1])
            phonenumber1.insert(0,record[2])
            item1.insert(0,record[3])
            quantity1.insert(0,record[4])


            conn.commit()
            conn.close()

    def update():
        conn=sqlite3.connect("order_details.db")
        c=conn.cursor()
        c.execute("""UPDATE orders SET
            Name=:name1,
            Location=:location1,
            Phonenumber=:phonenumber1,
            Item=:item1, 
            Quantity=:quantity1
            WHERE oid= :oid""",
            {
                'name1':name_edit1.get(),
                'location1':location1.get(),
                "phonenumber1":phonenumber1.get(),
                "item1":item1.get(),
                "quantity1":quantity1.get(),
                "oid":e_entry.get()





            })
        conn.commit()
        conn.close()
        messagebox.showinfo("sucessful","sucessfully updated your order")
        
    






    def confirm_order():
        if a1.get()=='' or a2.get()==''  or a3.get()==''  or a4.get()=='' :
            messagebox.showinfo("error","don't leave empty space ")
        elif a3.get().isalpha() or a4.get().isalpha():
                messagebox.showinfo("error","please enter numbers eg:12  ")
        else : 
                conn = sqlite3.connect("order_details.db")
                c = conn.cursor()
                c.execute("INSERT INTO orders VALUES (:Name, :Location, :Phonenumber ,:Item, :Quantity)",
                    {
                    "Name": a1.get(),
                    "Location": a2.get(),
                    "Item": cb1.get(),
                    "Quantity": a3.get(),
                    "Phonenumber": a4.get()
                })

                conn.commit()
                conn.close()

                conn = sqlite3.connect("order_details.db")
                c = conn.cursor()
                c.execute("SELECT *, oid FROM orders")
                records = c.fetchall()
                for record in records:
                    row_id = record[-1]

                a1.delete(0,END)
                a2.delete(0,END)
                a3.delete(0,END)
                a4.delete(0,END)
                cb1.set("")
                a5=Label(cp,text=f'your order id is {row_id}',font=('italic',10),fg='black')
                a5.place(x=365,y=590)
    a6.configure(command=confirm_order)
    edit3.configure(command=edit)
   


    cp.mainloop()





# Create the label inside the rounded frame
slogan_label =Label(root, text="HamroFruits: Nature's Harvest, Delivered fresh!", font=("bold", 20),bg="#FFDF64")
slogan_label.place(x=750,y=200)
#EMployee
Text_Employee=Label(root,text="Are you an Employee?",bg="#AFD485",font=("",25))
Text_Employee.place(x=685,y=350)
#login button
Login=Button(root,text="LOGIN",bg="black",fg="white",padx=90,pady=10,command=logeen,font=("",17),cursor="hand2")
Login.place(x=700,y=450)
#Customer
Text_Customer=Label(root,text="To order tasty and fresh fruits:",font=("",25),bg="#AFD485",)
Text_Customer.place(x=1050,y=350)
#button for customer portal
Customer_Portal=Button(root,text="Customer Portal",bg="black",fg="white",padx=70,pady=10,command=customer_pp,font=("",17),cursor="hand2")
Customer_Portal.place(x=1150,y=450)
#terms_and_conditions
terms=Button(root,text="terms and conditions",bg='white')
terms.place(x=650,y=680)
Text_condition1=Label(root,text="Acceptance of Terms: By accessing and using our services, you agree to comply with these",bg="#AFD485",font=("",15))
Text_condition1.place(x=650,y=650)
Text_condition2=Label(root,text=". If you do not agree with any part of these terms, please refrain from our page",bg="#AFD485",font=("",15))
Text_condition2.place(x=775,y=680)
root.mainloop()