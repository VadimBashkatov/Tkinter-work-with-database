from tkinter import *
import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                         database="tkinterdata",
                                         user="vadim",
                                         password="vadim")
root = Tk()
Label(root, text = "Enter name: ").grid(row = 0, sticky = W)
Label(root, text = "Enter password: ").grid(row = 1, sticky = W)
Label(root, text = "Enter your city: ").grid(row = 2, sticky = W)

Fname = Entry(root)
Sname = Entry(root)
x = Entry(root)


Fname.grid(row = 0, column = 1)
Sname.grid(row = 1, column = 1)
x.grid(row = 2, column = 1)
def getInput():

    a = Fname.get()
    b = Sname.get()
    c = x.get()
    root.destroy()

    global params
    params = [a,b,c]

Button(root, text = "Зберегти",command = getInput).grid(row = 5, sticky = W)

mainloop()
if params[0] == '':
    print("Zapownit vsi radki")
    exit()
if params[1] == '':
    print("Zapownit vsi radki")
    exit()
if params[2] == '':
    print("Zapownit vsi radki")
    exit()
cursor = connection.cursor()
cursor.execute("insert into customers(name, password, city) values(%s, %s, %s)" ,(params[0], params[1], params[2]))
connection.commit()
cursor.execute("SELECT * FROM customers")
data = cursor.fetchall()
print(data)

