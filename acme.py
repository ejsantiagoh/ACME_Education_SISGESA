from interfaz.login import cambiarPassword
from interfaz.menu import menu
from modelo.mRegistroGrupo import registrarGrupo
from modelo.mRegistrarModulo import registrarModulo
from modelo.mRegistroEstudiantes import registrarEstudiante
from modelo.mRegistrarDocentes import registrarDocente
from persistencia.persistencia import *


# Programa principal
print("-" * 64)
print("----- Sistema de Gestión de Asistencia Académica (SISGESA) -----\n")

while True: # Entramos al menú
        dDataAll = cargarDatos(pathData)
        menu()
        opcion = input("Introduce tu opción (A, B, C, D, etc): ").strip().upper() # quita espacios y pasa a mayusculas
        if opcion == 'A':
            registrarGrupo(dDataAll,pathData)
        elif opcion == 'B':
            registrarModulo(dDataAll,pathData)
        elif opcion == 'C':
            registrarEstudiante(dDataAll,pathData)
        elif opcion == 'D':
            registrarDocente(dDataAll,pathData)
        elif opcion == 'E':
            pass
            # registrarAsistencia()
        elif opcion == 'F':
            pass
        elif opcion == 'G':
            pass
        elif opcion == 'H':
            pass
        elif opcion == 'I':
            pass
        elif opcion == 'J':
            cambiarPassword()
        elif opcion == 'K':
            print("Saliendo del programa...\n")
            print("Gracias por usar el software.\n")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.\n")
            input("Presione cualquier tecla para volver al menú...")

