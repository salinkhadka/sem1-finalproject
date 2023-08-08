from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def ram(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)
    elif username_entry.get() == '':
        username_entry.insert(0, 'Username')

def ram1(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)
    elif password_entry.get() == '':
        password_entry.insert(0, 'Password')


def show():
    open_eye_image = ImageTk.PhotoImage(file='openeye.png')
    open_eye.configure(image=open_eye_image)
    open_eye.image = open_eye_image  # Store a reference to prevent image garbage collection
    password_entry.config(show='')
    eye_button.config(command=hide)
    print("apple")

def hide():
    closed_eye_image = ImageTk.PhotoImage(file='closeeye.png')
    open_eye.configure(image=closed_eye_image)
    open_eye.image = closed_eye_image  # Store a reference to prevent image garbage collection
    password_entry.config(show='*')
    eye_button.config(command=show)
    print("apple")






def signup():
    su = Toplevel()
    su.title("Signup")
    su.geometry("1435x850")
    su.resizable(0, 0)

    my_image = Image.open("login1.png")
    resized_image = my_image.resize((1435, 850))
    converted_image = ImageTk.PhotoImage(resized_image)
    my_label = Label(su, image=converted_image)
    my_label.pack()

    def confirm():
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()
    
        c.execute("INSERT INTO registration VALUES (:email, :username, :full_name, :dob, :password)",
              {
                  "email": email_entry.get(),
                  "username": username_entry.get(),
                  "full_name": fullname_entry.get(),
                  "dob": dob_entry.get(),
                  "password": password_entry.get()
              })

        conn.commit()
        conn.close()
    
        email_entry.delete(0, END)
        username_entry1.delete(0, END)
        fullname_entry.delete(0, END)
        dob_entry.delete(0, END)
        password_entry1.delete(0, END)


    email_label = Label(su, text='Email', font=('AkayaTelivigala', 16), bg='white', fg='firebrick1')
    email_label.place(x=120, y=370-60)

    email_entry = Entry(su, width=25, font=('AkayaTelivigala', 14), bg='firebrick1', fg='white')
    email_entry.place(x=122, y=400-60)

    username_label = Label(su, text='Username', font=('AkayaTelivigala', 16), bg='white', fg='firebrick1')
    username_label.place(x=120, y=430-60)

    username_entry1 = Entry(su, width=25, font=('AkayaTelivigala', 14), bg='firebrick1', fg='white')
    username_entry1.place(x=122, y=380+70+10-60)
    

    fullname_label = Label(su, text='Full Name', font=('AkayaTelivigala', 16), bg='white', fg='firebrick1')
    fullname_label.place(x=120, y=490-60)

    fullname_entry = Entry(su, width=25, font=('AkayaTelivigala', 14), bg='firebrick1', fg='white')
    fullname_entry.place(x=122, y=520-60)

    dob_label = Label(su, text='Date Of Birth', font=('AkayaTelivigala',16), bg='white', fg='firebrick1')
    dob_label.place(x=120, y=550-60)

    dob_entry = Entry(su, width=25, font=('AkayaTelivigala', 14), bg='firebrick1', fg='white')
    dob_entry.place(x=122, y=580-60)

    password_label = Label(su, text='Password', font=('AkayaTelivigala', 16), bg='white', fg='firebrick1')
    password_label.place(x=120, y=550)

    password_entry1 = Entry(su, width=25, font=('AkayaTelivigala', 14), bg='firebrick1', fg='white')
    password_entry1.place(x=122, y=580)
    
    

    terms = Checkbutton(su, text='I agree to the Terms & Conditions', font=('AkayaTelivigala', 12),
                        bg='white', fg='firebrick1')
    terms.place(x=120, y=620)

    signup_button = Button(su, width=11, text='Signup', font=('Open Sans', 25, 'bold'), fg='white',
                           bg='firebrick1', activebackground='white', cursor='hand2', bd=0, command=confirm)
    signup_button.place(x=110, y=650)

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

forgot_button = Button(li, width=11, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                       cursor='hand2', padx=20, font=('AkayaTelivigala', 11))
forgot_button.place(x=280, y=350 + 100)

open_eye = PhotoImage(file='openeye.png')
eye_button = Button(li, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eye_button.place(x=340, y=305 + 100)

login_button = Button(li, width=11, text='Login', font=('Open Sans', 36, 'bold'), fg='white', bg='firebrick1', activebackground='white', cursor='hand2', bd=0)
login_button.place(x=100, y=380 + 125)

signup_label = Label(li, text='Don\'t have an account?', font=('Open Sans', 15), fg='firebrick1', bg='white')
signup_label.place(x=125, y=380 + 200 + 50)

signup_button = Button(li, width=8, text='Create new one', font=('Open Sans', 15), fg='blue', bg='white',
                       activebackground='blue', padx=25, cursor='hand2', bd=0, command=signup)
signup_button.place(x=135, y=380 + 200 + 80)

li.mainloop()