from persistencia.persistencia import guardarAsistencia
from datetime import datetime, timedelta
import random


def validarCodEstudiante(dData):
    while True:
        try:
            codigo = validarEstudiante(dData)
            if(not recorrerCodEstudiante(codigo,dData)):
                print(f"El codigo {codigo} del estudiante no está asignado aun módulo")
                continue
            return codigo
        except Exception as e :
            print("Error al ingresar el codigo.\n", e)   


# Función para validar si el código de módulo pertenece al estudiante
def validar_modulo_por_estudiante(dData):
    codigo_estudiante = validarCodEstudiante(dData)
    # Buscar el estudiante en la lista
    for est in dData["asignarestudinatemodulo"]:
        if est['codigoestudiante'] == codigo_estudiante:
            return est, codigo_estudiante
    return False


def validarEstudianteModulo(dData):
    codigoModulo = validarModulo(dData)
    estudiante, codigo_estudiante = validar_modulo_por_estudiante(dData)

    if estudiante == False:
        print("El estudiante no se encuentra asignado a un modulo")
    else:
        if (codigoModulo not in estudiante['codigomodulo']):
            print(F"El modulo {codigoModulo} ingresado no se encuentra asignado al estudiante")
        else:
            return codigoModulo,codigo_estudiante


def traerFechaInicioModulo(dData, codigo):
    for m in dData['modulo']:
        if  m['codigo'] == codigo:
            return m["fechaInicio"]
    return False

def registrarAsistencia(dData):
    codModulo, codEstudiante = validarEstudianteModulo(dData)
    fechaInico, fechaFin = generar_asistencia(dData,codModulo)

    print(codModulo, "  " ,codEstudiante , "\n",  fechaInico, "   ",fechaFin)
    
def generar_asistencia(fecha_inicio_str):
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d %H:%M:%S")
    fecha_final = fecha_inicio + timedelta(weeks=2)

    # Genera una fecha de inicio aleatoria
    dias_inicio = random.randint(0, 14)
    fecha_inicio_aleatoria = fecha_inicio + timedelta(days=dias_inicio)
    
    # Genera una hora de inicio aleatoria (de 00:00 a 23:59)
    hora_inicio = random.randint(14, 16)
    minuto_inicio = random.randint(0, 59)
    fecha_inicio_aleatoria = fecha_inicio_aleatoria.replace(hour=hora_inicio, minute=minuto_inicio)

    # Genera una hora de finalización aleatoria dentro del mismo día (1 a 4 horas después)
    duracion_sesion = random.randint(1, 2)  # Duración en horas
    fecha_fin_aleatoria = fecha_inicio_aleatoria + timedelta(hours=duracion_sesion)

    # Asegurarse de que la fecha de finalización no exceda la fecha final
    if fecha_fin_aleatoria > fecha_final:
        fecha_fin_aleatoria = fecha_final  # Ajustar a la fecha final

    print(fecha_inicio_aleatoria, fecha_fin_aleatoria)