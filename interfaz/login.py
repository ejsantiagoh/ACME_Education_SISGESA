import json
import hashlib

# Definimos un usuario y una contraseña predeterminada
USERNAME = 'usuario'
PASSWORD = 'SISGESA'

# Función para encriptar la contraseña con SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Guardamos el usuario y la contraseña en un archivo JSON
def guardarCredenciales():
    credentials = {
        'username': USERNAME,
        'password': hash_password(PASSWORD)
    }
    with open('passwords.json', 'w') as f:
        json.dump(credentials, f)


# Función para validar el login
def login(username, password): 
    try:
        with open('passwords.json', 'r') as f:
            credentials = json.load(f)
        
        if username == credentials['username'] and hash_password(password) == credentials['password']:
            print("Login exitoso.")
            cambiarPassword(credentials['username'])  # Llama a la función para cambiar la contraseña
        else:
            print("Usuario o contraseña incorrectos.")
        
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Función para cambiar la contraseña
def cambiarPassword(username):
    try:
        new_password = input("Ingrese su nueva contraseña: ")
        new_hashed_password = hash_password(new_password)

        # Actualizamos el archivo JSON con la nueva contraseña
        credentials = {
            'username': username,
            'password': new_hashed_password
        }
        with open('passwords.json', 'w') as f:
            json.dump(credentials, f)

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

