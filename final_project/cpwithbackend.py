from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

cp = Tk()
cp.title("Customer-order")
cp.geometry("900x700")
cp.resizable(0, 0)

# define image
my_image = Image.open('iio.png')
resized_image = my_image.resize((900, 700))
converted_image = ImageTk.PhotoImage(resized_image)
mylabel = Label(cp, image=converted_image)
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
    app=Tk()



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
    






def confirm_order():
    if a1.get()=='' or a2.get()==''  or a3.get()==''  or a4.get()=='' :
        messagebox.showinfo("error","don't leave empty space ")
    else :
        if a3.get().isalpha() or a4.get().isalpha():
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