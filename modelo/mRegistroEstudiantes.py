from  persistencia.persistencia import guardarRegistroEstudiante 

def leerCodigo():
    while True:
        try:
            codigo = input("Ingresar el Código del estudiante: \n").strip()
            if len(codigo.strip()) == 0:
                print("Error. Código incorrecto")
                continue
            return codigo
        except Exception as e:
            print("Error al ingresar el Código \n" , e)

def leerNombre():
    while True:
        try:
            nombre = input("Ingresar el nombre del estudiante: \n").strip()
            if len(nombre.strip()) == 0:
                print("Error. Nombre incorrecto")
                continue
            return nombre
        except Exception as e:
            print("Error al ingresar el Nombre \n" , e)

def leerSexo():
    while True:
        try:
            sexo = input("Ingresar el Sexo (M/F) :").strip().upper()
            if len(sexo.strip()) == 0:
                print("Error. Ha ingresado una letra que NO corresponde.")
                continue
            return sexo
        except Exception as e:
            print("Error al ingresar  el sexo. \n", e)


def leerEdad():
    while True:
        try:
            edad = input("Ingresar la Edad: \n")
            if len(edad.strip()) == 0:
                print("Error. Valor incorrecto.")
                continue
            return int(edad)
        except Exception as e:
            print("Error al ingresar la edad \n", e)


def validarCodigo(dData):
    while True:
        try:
            codigo = leerCodigo()
            if(recorrerCodigo(codigo,dData)):
                print(f"El codigo {codigo} ya existe en la base de datos. \n")
                continue
            return codigo
        except Exception as e :
            print("Error al ingresar el codigo.\n", e)   


def validarNombre(dData):
    while True:
        try:
            nombre = leerNombre()
            if(nombre.isalpha()):
                if(recorrerNombre(nombre,dData)):
                    print(f"El nombre {nombre} ya existe en la base de datos. \n")
                    continue
                return nombre.title()
            else:
                print("Ingresar solo letras.")
        except Exception as e :
            print("Error al ingresar el nombre.\n", e)   


def validarSexo():
    while True:
        try:
            sexo = leerSexo().upper()
            print(sexo)
            if(sexo != "M") and (sexo != "F"):
                print("Error.  Ingrese un valor valido. ")
                continue
            return sexo
        except Exception as e :
            print("Error al ingresar el sexo. ", e)   

def validarEdad():
    while True:
        try:
            edad = leerEdad()
            if(edad >= 62 and edad<=16):
                print(f"La edad ingresada no es permitida. \n")
                continue
            return edad
        except Exception as e :
            print("Error. Verificar la edad ingresada. ", e)   


def recorrerCodigo(codigo, dData):
    for e in dData['estudiante']:
        if  e['codigo'] == codigo:
            return True
    return False


def recorrerNombre(nombre, dData):
    for e in dData['estudiante']:
        if  e['nombre'] == nombre:
            return True
    return False


def registrarEstudiante(dData,pathData):
    if "estudiante" not in dData:
        dData["estudiante"] = []

    codigo =validarCodigo(dData)
    nombre =validarNombre(dData)
    edad =validarEdad()
    sexo =validarSexo()


    dData['estudiante'].append(
            { "codigo" : codigo.upper(),
            "nombre" : nombre,
            "edad" :  edad,
            "sexo": sexo
            }
    )

    guardarRegistroEstudiante(dData,pathData)