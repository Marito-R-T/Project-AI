import pandas as pd
import database_functions as dbf
from querys import querys
import columns as columns

def insertar_persona(persona:tuple, querys:dict):
    if(not dbf.existePersona(persona[0])):
        row = dbf.create_persona_planilla(persona, querys["persona"])
        print(row, "creadas")

def insertar_empresa(empresa:tuple, querys:dict):
    if(not dbf.existeEmpresa(empresa[0])):
        row = dbf.create_empresa_planilla(empresa, querys["empresa"])
        print(row, "creadas")

def insertar_tupla(trabajo:tuple, querys:dict):
    trabajo = dbf.create_trabajo_planilla(trabajo, querys["trabajo"])
    print(trabajo, "creadas")


def primer_plantilla(df:pd.DataFrame):
    nombres = df.nombres.str.split(' ', 1, expand=True)
    apellidos = df.apellidos.str.split(' ', 1, expand=True)
    df['nombreF'] = nombres[0]
    df['nombreS'] = nombres[1]
    df['apellidoF'] = apellidos[0]
    df['apellidoS'] = apellidos[1]
    df.genero = df.genero.replace({'masculino':'M', 'femenino':'F'}, regex=True)
    df.loc[(df.genero != 'M') & (df.genero != 'F'), 'genero'] = 'O'
    for linea in df.itertuples():
        trabajador = (linea.dpi, linea.nombreF, linea.nombreS, linea.apellidoF, linea.apellidoS, 
            linea.direccion, linea.nit, linea.genero, linea.correo)
        insertar_persona(trabajador, querys["plantilla1"])
        empresa = (linea.codigo, linea.nombreEmpresa, linea.nitEmpresa, linea.dirEmpresa, linea.telEmpresa)
        insertar_empresa(empresa, querys["plantilla1"])
        trabajo = (dbf.getPersona(trabajador[0]), linea.fechaI, linea.fechaF, dbf.getEmpresa(empresa[0]), linea.salario)
        insertar_tupla(trabajo, querys["plantilla1"])

def segunda_plantilla(df:pd.DataFrame):
    for linea in df.itertuples():
        trabajador = (linea.dpi, linea.nombre_empleado, linea.apellido_empleado,
        linea.residencia, linea.nit, linea.genero, linea.telefono, linea.correo)
        insertar_persona(trabajador, querys["plantilla2"])
        empresa = (linea.codigo, linea.nombre_empresa, linea.empresa_nit)
        insertar_empresa(empresa, querys["plantilla2"])
        trabajo = (dbf.getPersona(trabajador[0]), linea.fecha_i, linea.fecha_f, dbf.getEmpresa(empresa[0]), linea.salario)
        insertar_tupla(trabajo, querys["plantilla2"])

def tercera_plantilla(df:pd.DataFrame):
    for linea in df.itertuples():
        trabajador = (linea.dpi, linea.primer_nombre, linea.segundo_nombre, linea.primer_apellido,
        linea.dir_e, linea.nit_e)
        insertar_persona(trabajador, querys["plantilla3"])
        empresa = (linea.codigo, linea.empresa, linea.nit, linea.dir)
        insertar_empresa(empresa, querys["plantilla3"])
        trabajo = (dbf.getPersona(trabajador[0]), linea.fecha_i, linea.fecha_f, dbf.getEmpresa(empresa[0]), linea.salario, linea.puesto)
        insertar_tupla(trabajo, querys["plantilla3"])

def cuarta_plantilla(df:pd.DataFrame):
    nombres = df.nombres.str.split(' ', 1, expand=True)
    apellidos = df.apellidos.str.split(' ', 1, expand=True)
    df['nombre_f'] = nombres[0]
    df['nombre_s'] = nombres[1]
    df['apellido_f'] = apellidos[0]
    df['apellido_s'] = apellidos[1]
    df.genero = df.genero.replace({'hombre':'M', 'mujer':'F'}, regex=True)
    df.loc[(df.genero != 'M') & (df.genero != 'F'), 'genero'] = 'O'
    for linea in df.itertuples():
        trabajador = (linea.dpi, linea.nombre_f, linea.nombre_s, linea.apellido_f, linea.apellido_s,
        linea.residencia, linea.nit, linea.genero)
        insertar_persona(trabajador, querys["plantilla4"])
        empresa = (linea.codigo, linea.empresa, linea.nit_empresa, linea.tel_empresa)
        insertar_empresa(empresa, querys["plantilla4"])
        trabajo = (dbf.getPersona(trabajador[0]), linea.inicio, linea.fin, dbf.getEmpresa(empresa[0]), linea.puesto)
        insertar_tupla(trabajo, querys["plantilla4"])

def leer_plantilla(df:pd.DataFrame):
    if (list(df.columns) == columns.columns_primer_plantilla) :
        primer_plantilla(df)
    elif (list(df.columns) == columns.columns_segunda_plantilla):
        segunda_plantilla(df)
    elif (list(df.columns) == columns.columns_tercera_plantilla):
        tercera_plantilla(df)
    elif (list(df.columns) == columns.columns_cuarta_plantilla):
        cuarta_plantilla(df)
