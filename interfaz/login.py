import json
import hashlib

# Definimos un usuario y una contraseña predeterminada
USUARIO = 'usuario'
CONTRASENA = 'SISGESA'

# Función para encriptar la contraseña con SHA-256
def encriptarContrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Guardamos el usuario y la contraseña en un archivo JSON
def guardarCredenciales():
    credenciales = {
        'usuario': USUARIO,
        'contrasena': encriptarContrasena(CONTRASENA)
    }
    with open('passwords.json', 'w') as archivo:
        json.dump(credenciales, archivo)

# Función para validar el inicio de sesión
def login(usuario, contrasena):
    try:
        with open('passwords.json', 'r') as archivo:
            credenciales = json.load(archivo)
            if usuario == credenciales['usuario'] and encriptarContrasena(contrasena) == credenciales['contrasena']:
                print("Inicio de sesión exitoso.")
                cambiarPassword(credenciales['usuario'])  # Llama a la función para cambiar la contraseña
            # else:
            #     print("Usuario o contraseña incorrectos.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Función para cambiar la contraseña
def cambiarPassword(usuario):
    try:
        nueva_contrasena = input("Ingrese su nueva contraseña: ")
        nueva_contrasena_encriptada = encriptarContrasena(nueva_contrasena)

        # Actualizamos el archivo JSON con la nueva contraseña
        credenciales = {
            'usuario': usuario,
            'contrasena': nueva_contrasena_encriptada
        }
        with open('passwords.json', 'w') as archivo:
            json.dump(credenciales, archivo)

        print("Contraseña cambiada exitosamente.")

    except Exception as e:
        print(f"Ocurrió un error al cambiar la contraseña: {e}")

# Guardamos las credenciales inicialmente
guardarCredenciales()

# Solicitar el inicio de sesión al usuario
print("*" * 64)
print("------------------------- S I S G E S A -----------------------")
user = input("Ingresar su usuario: ")
password = input("Ingresar su contraseña: ")
login(user, password)

