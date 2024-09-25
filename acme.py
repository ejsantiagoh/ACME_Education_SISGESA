from interfaz.login import cambiarPassword
from interfaz.menu import menu
from modelo.mRegistroGrupo import registrarGrupo
from modelo.mRegistrarModulo import registrarModulo
from modelo.mRegistroEstudiantes import registrarEstudiante
from modelo.mRegistrarDocentes import registrarDocente
# from modelo.mRegistroAsistencia import registrarAsistencia

# Programa principal
print("-" * 64)
print("----- Sistema de Gestión de Asistencia Académica (SISGESA) -----\n")

while True: # Entramos al menú
        menu()
        opcion = input("Introduce tu opción (A, B, C, D, etc): ").strip().upper() # quita espacios y pasa a mayusculas
        if opcion == 'A':
            registrarGrupo()
        elif opcion == 'B':
            registrarModulo()
        elif opcion == 'C':
            registrarEstudiante()
        elif opcion == 'D':
            registrarDocente()
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

