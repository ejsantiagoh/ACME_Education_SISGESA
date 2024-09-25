import json
from pathlib import Path

pathData = "data.json"

def guardarDatos():
    datos = {}
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo)


def cargarDatos(arch):
    archivo = Path(arch)
    grupo = {}
    if archivo.is_file(): #True si existe y es un archivo
        try:
            with open(arch, "r") as fd: #Abrir el archivo
                grupo = json.load(fd)
            if not fd.closed:
                fd.close()
        except Exception as e:
            print("Error al abrir el archivo data\n", e)
    else:
        print("Error el archivo no existe")
        input("Presione cualquier tecla para continuar...")    
    return grupo

def guardarRegistroGrupo(pathData, arch):
    archivo = Path(arch)
    try:
        if archivo.is_file(): #Si el archivo existe
            with open(archivo,"w") as fd:
                json.dump(pathData, fd)
            if not fd.closed:
                fd.close()
    except Exception as e:
        print("Error al guardar un grupo en el archivo ", e)
        
def guardarRegistroModulo(dData, pathData):
    archivo = Path(pathData)
    try:
        if archivo.is_file():
            with open(archivo,"w") as fd:
                json.dump(dData,fd)
            if not fd.closed:
                fd.close()
    except Exception as e:
        print("Error al guardar un modulo en el archivo ", e)
        
def guardarRegistroEstudiante(dData, pathData):
    archivo = Path(pathData)
    try:
        if archivo.is_file():
            with open(archivo,"w") as fd:
                json.dump(dData,fd)
            if not fd.closed:
                fd.close()
    except Exception as e:
        print("Error al guardar un estudiante en el archivo ", e)
        
def guardarDocentes(dData, pathData):
    archivo = Path(pathData)
    try:
        if archivo.is_file():
            with open(archivo,"w") as fd:
                json.dump(dData,fd)
            if not fd.closed:
                fd.close()
    except Exception as e:
        print("Error al guardar un docente en el archivo ", e)

