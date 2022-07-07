import b as ModuleB
import CRUD as crud

ModuleB.greeting("Jonathan")

a = ModuleB.person1["age"]
print(a)

columnas = """
        CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)"""

crud.CrearTabla("BaseRegistros","TablaDias",columnas)


def today():
    import datetime
    return datetime.datetime.now()



def get_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

print(get_days_in_month(2020, 1))















'''
columnas = """
        CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)"""

CrearTabla("BaseProductos","TablaProductos",columnas)
InsertarRegistro("BaseProductos","INSERT INTO TablaProductos VALUES (NULL,'BALON',10,'DEPORTE')")
InsertarVariosRegistros("BaseProductos",[
    "INSERT INTO TablaProductos VALUES (NULL,'BALON',10,'DEPORTE')",
    "INSERT INTO TablaProductos VALUES (NULL,'JARRON',20,'CERAMICA')",
    "INSERT INTO TablaProductos VALUES (NULL,'PELOTA',5,'DEPORTE')"
])
print(LeerRegistros("BaseProductos","TablaProductos"))
ActualizarRegistro("BaseProductos","UPDATE TablaProductos SET NOMBRE_ARTICULO='PELO8TA' WHERE CODIGO_ARTICULO=3")
EliminarRegistro("BaseProductos","DELETE FROM TablaProductos WHERE CODIGO_ARTICULO=3")
'''