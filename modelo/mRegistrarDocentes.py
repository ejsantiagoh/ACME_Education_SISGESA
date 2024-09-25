from persistencia.persistencia import guardarDocentes


def leerCedula():
    while True:
        try:
            cedula = input("Ingresar la cédula del Docente: \n").strip()
            if len(cedula.strip()) == 0:
                print("Error. cédula invalida")
                continue
            return cedula
        except Exception as e:
            print("Error al ingresar la cédula \n" , e)
            
            
def leerNombre():
    while True:
        try:
            nombre = input("Ingresar nombre del docente: ").strip()
            if len(nombre.strip()) == 0:
                print("Error. nombre incorrecto")
                continue
            return nombre
        except Exception as e:
            print("Error al ingresar la nombre \n" , e)
            
def validarNombre(pathData):
    while True:
        try:
            nombre = leerNombre()
            if(recorrerNombre(nombre,pathData)):
                print(f"El nombre {nombre} ya existe en la base de datos")
                continue
            return nombre
        except Exception as e :
            print("Error al ingresar el nombre.\n", e)   


def validarCedula(pathData):
    while True:
        try:
            cedula = leerCedula()
            print(recorrerCedula(cedula,pathData))
            if(recorrerCedula(cedula,pathData)):
                print(f"La cedula {cedula} ya existe en la base de datos")
                continue
            return cedula
        except Exception as e :
            print("Error al ingresar el código.\n", e)   

def recorrerCedula(cedula, pathData):
    for n in pathData['docente']:
        if n['cedula'] == cedula:
            return True
    return False

def recorrerNombre(nombre, pathData):
    for n in pathData['docente']:
        if n['nombre'] == nombre:
            return True
    return False

def registrarDocente(dData,pathData):
    if "docente" not in dData:
        dData["docente"] = []

    cedula = validarCedula(dData)
    nombre = validarNombre(dData)

    dData['docente'].append({    
                             "cedula" : cedula,
                            "nombre" : nombre.title(),
                        })

    guardarDocentes(dData,pathData)