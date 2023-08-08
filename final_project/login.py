from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import ast




    

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
    openeeye.config(file='closeye.png')
    password.config(show='*')
    eyebuttin.config(command=show)
def show():
    openeeye.config(file='openeye.png')
    password.config(show='')
    eyebuttin.config(command=hide)
def verify():
    from tkinter import messagebox
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("datasheet.txt", "r") as file:
            data = file.read()
            login_data = ast.literal_eval(data)
    except (FileNotFoundError, ValueError, SyntaxError) as e:
        messagebox.showerror("Error", f"Error reading login data: {e}")
        return

    if username in login_data and password == login_data[username]:
        messagebox.showinfo("Log in", "Logged in successfully")
    else:
        messagebox.showerror("Log in", "Invalid username or password")




def signup():
    su = Toplevel()
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
        try:
        # Read existing user data from the "datasheet.txt" file
                with open("datasheet.txt", "r") as file:
                        data = file.read()
                        user_data = ast.literal_eval(data)
        except (FileNotFoundError, ValueError, SyntaxError):
        # If the file is not found or not a valid dictionary, start with an empty dictionary
                user_data = {}

        username = usernameentry.get()
        password = Passwordentry.get()

        # Update the user_data dictionary with the new username and password
        user_data[username] = password

        # Write the updated user_data dictionary to the "datasheet.txt" file
        with open("datasheet.txt", "w") as file:
                file.write(str(user_data))

        # Clear the input fields after successful registration
        emailentry.delete(0, END)
        usernameentry.delete(0, END)
        fullnameentry.delete(0, END)
        dobentry.delete(0, END)
        Passwordentry.delete(0, END)

        messagebox.showinfo("Sign in", "Signed up successfully")
        li.destroy()




    email=Label(su,text='Email',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
    email.place(x=120,y=370-60)

    emailentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
    emailentry.place(x=122,y=400-60)

    username=Label(su,text='Username',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
    username.place(x=120,y=430-60)

    usernameentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
    usernameentry.place(x=122,y=380+70+10-60)

    fullname=Label(su,text='Full Name',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
    fullname.place(x=120,y=490-60)

    fullnameentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
    fullnameentry.place(x=122,y=520-60)

    dob=Label(su,text='Date Of Dirth',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
    dob.place(x=120,y=550-60)

    dobentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
    dobentry.place(x=122,y=580-60)

    Password=Label(su,text='Password',font=('AkayaTelivigala',16)
            ,bg='white' , fg='firebrick1')
    Password.place(x=120,y=550)

    Passwordentry=Entry(su,width=25,font=('AkayaTelivigala',14)
            ,bg='firebrick1' , fg='white')
    Passwordentry.place(x=122,y=580)



    terms=Checkbutton(su,text='I agree to the Terms & Conditions',font=('AkayaTelivigala',12)
            ,bg='white' , fg='firebrick1') 
    terms.place(x=120,y=620)

    login=Button(su,width=11,text='Signup',font=('Open Sans',25,'bold')
             ,fg='white',bg='firebrick1',activebackground='white',cursor='hand2',bd=0,command=confirm)
    login.place(x=110,y=650)


    su.mainloop()

li = Tk()
li.title('Login')
li.resizable(0, 0)
li.geometry("1435x850")

my_image = Image.open("login1.png")
resized_image = my_image.resize((1435, 850))
converted_image = ImageTk.PhotoImage(resized_image)
my_label = Label(li, image=converted_image)
my_label.pack()

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

forgot_button = Button(li, width=11, text='Forgot Password?', bd=0, bg='white', activebackground='white',cursor='hand2', padx=20, font=('AkayaTelivigala', 11))
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
