from cgitb import text
from tkinter import ttk
from tkinter import *

from database import cursor

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')
        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Register A new Product')
        frame.grid(row= 0 , column= 0, columnspan=3, pady=20, padx=5)

        # Name Input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)
        self.name.focus()

        # Price Input
        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Save Product').grid(row=3, columnspan=2, sticky=W+E)

        # Create Table
        self.tree = ttk.Treeview(height= 10, columns= 2)
        self.tree.grid(row=4, column=0, columnspan= 2)
        self.tree.heading('#0', text='Id', anchor= CENTER)
        self.tree.heading('#1', text='Nombre', anchor= CENTER)

        #db
        self.get_products()

    def run_query(self, query):
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_products(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = "SELECT id, nombre FROM departamento"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=row[1])
            print(row[1])

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()