from cgitb import text
from msilib.schema import File
from tkinter import ttk
from tkinter import *
from turtle import width
from database import cursor
from filechooser import openFile
import pandas as pd

from functions import leer_plantilla

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')
        # Creating a Frame Container
        #frame = LabelFrame(self.wind, text='Agregar Plantilla')
        #frame.grid(row= 0 , column= 0, columnspan=4, pady=20, padx=5)

        # Name Input
        #Label(frame, text='Name: ').grid(row=1, column=0)
        #self.name = Entry(frame)
        #self.name.grid(row=1, column=1)
        #self.name.focus()

        # Price Input
        #Label(frame, text='Price: ').grid(row=2, column=0)
        #self.price = Entry(frame)
        #self.price.grid(row=2, column=1)

        # Button Add Product
        self.addFile = ttk.Button(self.wind, text='Save Product', command=self.get_csv).grid(row=3, columnspan=2, column=0, sticky=W + E)
        # Create Table
        col = self.get_columns()
        self.tree = ttk.Treeview(height= 10, columns=col)
        self.tree.grid(row=4, column=0, columnspan= 2)
        self.set_headings()
        #db
        #self.get_products()
    
    def get_columns(self):
        tuple = ("codE", "nombreE", "salario", "dpi", "fName", "fApellido")
        return tuple

    def set_headings(self):
        self.tree.heading('#0', text='Id', anchor= CENTER)
        self.tree.heading("codE", text='Nombre', anchor= CENTER)
        self.tree.heading('nombreE', text='Otro', anchor= CENTER)
        self.tree.heading('salario', text='Otro', anchor= CENTER)
        self.tree.heading('dpi', text='Otro', anchor= CENTER)
        self.tree.heading('fName', text='Otro', anchor= CENTER)
        self.tree.heading('fApellido', text='Otro', anchor= CENTER)

    def get_csv(self):
        files = openFile()
        for str in files:
            df = pd.read_csv(str, sep=',')
            self.add_csv(df)


    def add_csv(self, df:pd.DataFrame):
        leer_plantilla(df)
        #self.tree.insert('',0, values=list(df.Action))

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

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()