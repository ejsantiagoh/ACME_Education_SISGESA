from persistencia.persistencia import guardarRegistroModulo 

def leerCodigo():
    try:
        while True:
            codigo = input("Ingresar Código del módulo:  \n").strip()
            if len(codigo.strip()) == 0:
                print("Error. Código incorrecto.")
                continue
            return codigo
        
    except Exception as e:
        print("Error al ingresar el Código \n" , e)


def leerNombre():
    try:
        while True:
            nombre = input("Ingresar Nombre del módulo: \n").strip()
            if len(nombre.strip()) == 0:
                print("Error. Nombre invalido")
                continue
            return nombre
        
    except Exception as e:
        print("Error al ingresar el nombre \n" , e)

def leerSemanas():
    
    while True:
        try:
            semanas = input("Ingresar la cantidad de semanas: \n")
            if len(semanas.strip()) == 0 :
                print("Error. El valor ingresado en semanas es incorrecto")
                continue
            return int(semanas)
        
        except Exception as e:
            print("Error al ingresar la cantidad del modulo. \n" , e)



def validarCodigo(dData):
    while True:
        try:
            codigo = leerCodigo()
            if codigo == "-1":
                print(f"No se puede almacenar el siguiente código {codigo} \n")
                continue
            if(recorrerCodigo(codigo,dData)):
                print(f"El codigo {codigo} ya existe en la base de datos.\n")
                continue
            return codigo
        except Exception as e :
            print("Error. Verificar el código.\n", e)   


def validarNombre(dData):
    while True:
        try:
            nombre = leerNombre()
            if(recorrerNombre(nombre,dData)):
                print(f"El nombre {nombre} ya existe en la base de datos. \n")
                continue
            return nombre
        except Exception as e :
            print("Error. Verificar el nombre.\n", e)   


def recorrerCodigo(codigo, dData):
    for m in dData['modulo']:
        if  m['codigo'] == codigo:
            return True
    return False

def recorrerNombre(nombre, dData):
    for m in dData['modulo']:
        if  m['nombre'] == nombre:
            return True
    return False

def registrarModulo(dData,pathData):

    if "modulo" not in dData:
            dData["modulo"] = []

    codigo = validarCodigo(dData)
    nombre = validarNombre(dData)
    semanas = leerSemanas()

    dData['modulo'].append(
        { "codigo" : codigo.upper(),
        "nombre" : nombre.title(),
        "semana" : semanas}
    )

    guardarRegistroModulo (dData,pathData)