from database import cursor
from database import db

def existePersona(dpi:int):
    query = "SELECT id_persona FROM persona WHERE dpi = %s"
    values = tuple([dpi])
    cursor.execute(query, values)
    count = cursor.rowcount
    return count > 0

def getPersona(dpi:int):
    query = "SELECT id_persona FROM persona WHERE dpi = %s"
    values = tuple([dpi])
    cursor.execute(query, values)
    return cursor.fetchall()[0][0]

def existeEmpresa(id:int):
    query = "SELECT id_empresa FROM empresa WHERE codigo = %s"
    values = tuple([id])
    cursor.execute(query, values)
    count = cursor.rowcount
    return count > 0

def getEmpresa(id:int):
    query = "SELECT id_empresa FROM empresa WHERE codigo = %s"
    values = tuple([id])
    cursor.execute(query, values)
    return cursor.fetchall()[0][0]

def create_persona_planilla(obj:tuple, query:str):
    cursor.execute(query, obj)
    db.commit()
    return cursor.rowcount

def create_empresa_planilla(obj:tuple, query:str):
    cursor.execute(query, obj)
    db.commit()
    return cursor.rowcount

def create_trabajo_planilla(obj:tuple, query:str):
    cursor.execute(query, obj)
    db.commit()
    return cursor.rowcount