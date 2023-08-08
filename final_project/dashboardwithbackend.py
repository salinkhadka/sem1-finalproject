from tkinter import *
from PIL import Image, ImageTk
import sqlite3

dash = Tk()
dash.title('Login')
dash.resizable(0, 0)
dash.geometry("1435x850")

def checkout(row_id):
    # Function to handle the "Checkout" button click
    conn = sqlite3.connect("order_details.db")
    c = conn.cursor()

    c.execute("DELETE FROM orders WHERE oid=?", (row_id,))
    conn.commit()
    conn.close()
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
            ,bg='gray' , fg='firebrick1')
Name.grid(row=0,column=0,pady=25)
    
quantity=Label(frame,text='Location',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
quantity.grid(row=0,column=1,padx=25)

Location=Label(frame,text='Contact Details',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
Location.grid(row=0,column=2,padx=25)

contact_number=Label(frame,text='Items',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
contact_number.grid(row=0,column=3,padx=25)








Items=Label(frame,text='Quantity',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
Items.grid(row=0,column=4,padx=25)

oid=Label(frame,text='OID',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
oid.grid(padx=25,row=0,column=5)


button=Label(frame,text='button',font=('AkayaTelivigala',20)
            ,bg='gray' , fg='firebrick1')
button.grid(row=0,column=6)
show_records=Button(frame,text="Show Records",command=query)
show_records.grid(row=1,column=6)


dash.mainloop()