querys = {
    "plantilla1": {
        "persona":"INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        "empresa":"INSERT INTO empresa (codigo, nombre_empresa, nit, direccion, telefono) values (%s, %s, %s, %s, %s)",
        "trabajo":"INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"
    },
    "plantilla2": {
        "persona":"INSERT INTO persona (dpi, primer_nombre, primer_apellido, direccion_residencia, nit, genero, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
        "empresa":"INSERT INTO empresa (codigo, nombre_empresa, nit) values (%s, %s, %s)",
        "trabajo":"INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"
    },
    "plantilla3": {
        "persona":"INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, direccion_residencia, nit) VALUES (%s, %s, %s, %s, %s, %s)", 
        "empresa":"INSERT INTO empresa (codigo, nombre_empresa, nit, direccion) values (%s, %s, %s, %s)",
        "trabajo":"INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario, nombre_puesto) values (%s, %s, %s, %s, %s, %s)"
    },
    "plantilla4": {
        "persona":"INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
        "empresa":"INSERT INTO empresa (codigo, nombre_empresa, nit, telefono) values (%s, %s, %s, %s)",
        "trabajo":"INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, nombre_puesto) values (%s, %s, %s, %s, %s)"
    }
}

#Querys para insertar empleados
INSERT_PERSONA_PLANILLA_1 = "INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_PERSONA_PLANILLA_2 = "INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_PERSONA_PLANILLA_3 = "INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_PERSONA_PLANILLA_4 = "INSERT INTO persona (dpi, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, direccion_residencia, nit, genero, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

#Querys para insertar empresas
INSERT_EMPRESA_PLANILLA_1 = "INSERT INTO empresa (nombre_empresa, nit, codigo, direccion, telefono) values (%s, %s, %s, %s, %s)"
INSERT_EMPRESA_PLANILLA_2 = "INSERT INTO empresa (nombre_empresa, nit, codigo, direccion, telefono) values (%s, %s, %s, %s, %s)"
INSERT_EMPRESA_PLANILLA_3 = "INSERT INTO empresa (nombre_empresa, nit, codigo, direccion, telefono) values (%s, %s, %s, %s, %s)"
INSERT_EMPRESA_PLANILLA_4 = "INSERT INTO empresa (nombre_empresa, nit, codigo, direccion, telefono) values (%s, %s, %s, %s, %s)"

#Querys para insertar trabajos
INSERT_TRABAJO_PLANILLA_1 = "INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"
INSERT_TRABAJO_PLANILLA_2 = "INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"
INSERT_TRABAJO_PLANILLA_3 = "INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"
INSERT_TRABAJO_PLANILLA_4 = "INSERT INTO trabajo (id_persona, fecha_inicial, fecha_final, id_empresa, salario) values (%s, %s, %s, %s, %s)"