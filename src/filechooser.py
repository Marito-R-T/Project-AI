from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def openFile():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/Users/mario/OneDrive/Documentos/Universidad/Inteligencia Artificial/Project-AI/archivos_prueba',
        filetypes=filetypes
    )
    return list(filenames)
    #C:\Users\mario\OneDrive\Documentos\Universidad\Inteligencia Artificial\Project-AI\archivos_prueba