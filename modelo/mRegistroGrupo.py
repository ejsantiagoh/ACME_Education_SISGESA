from persistencia.persistencia import guardarRegistroGrupo


def leerCodigo():
    while True:
        try:
            codigo = input("Ingresar el Código del grupo: \n").strip()
            if len(codigo.strip()) == 0:
                print("Error. Código incorrecto.")
                continue
            return codigo
        except Exception as e:
            print("Error. Revisar que código ingresado sea el correcto. \n" , e)

def leerNombre():
    while True:
        try:
            nombre = input("Ingresar Nombre del grupo: \n").strip()
            if len(nombre.strip()) == 0:
                print("Error. Nombre incorrecto")
                continue
            return nombre
        except Exception as e:
            print("Error. Revisar que el nombre ingresado sea el correcto. \n" , e)

def leerSigla():
    while True:
        try:
            sigla = input("Ingresar Sigla del grupo: \n").strip()
            if len(sigla.strip()) == 0:
                print("Error. Sigla incorrecta.")
                continue
            return sigla
        except Exception as e:
            print("Error al ingresar la Sigla \n", e)

def validarCodigo(pathData):
    while True:
        try:
            codigo = leerCodigo()
            if(recorrerCodigo(codigo,pathData)):
                print(f"El codigo {codigo} ya existe en la base de datos. \n")
                continue
            return codigo
        except Exception as e :
            print("Error al ingresar el codigo.\n", e)   


def validarNombre(pathData):
    while True:
        try:
            nombre = leerNombre()
            if(recorrerNombre(nombre,pathData)):
                print(f"El nombre {nombre} ya existe en la basse de datos \n")
                continue
            return nombre
        except Exception as e :
            print("Error. ingresar el nombre correctamente.\n", e)   

def validarSigla(pathData):

    while True:
        try:
            sigla = leerSigla()
            if(recorrerSigla(sigla,pathData)):
                print(f"La sigla {sigla} ya existe en la base de datos")
                continue
            return sigla
        except Exception as e :
            print("Error al ingresar la sigla.\n", e) 

def recorrerCodigo(codigo, pathData):
    for c in pathData['grupo']:
        if  c['codigo'] == codigo:
            return True
    return False

def recorrerNombre(nombre, pathData):
    for n in pathData['grupo']:
        if n['nombre'] == nombre:
            return True
    return False

def recorrerSigla(sigla, pathData):
    for n in pathData['grupo']:
        if n['sigla'] == sigla:
            return True
    return False

def registrarGrupo(dGrupo, arch):

    if "grupo" not in dGrupo:
        dGrupo["grupo"] = []

    Codigo = validarCodigo(dGrupo)
    Nombre = validarNombre(dGrupo)
    Sigla = validarSigla(dGrupo)

    dGrupo['grupo'].append(
            { "codigo" : Codigo,
            "nombre" : Nombre.title(),
            "sigla" :  Sigla.upper()}
            )

    guardarRegistroGrupo(dGrupo,arch)