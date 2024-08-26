# Diccionario de usuarios y contraseñas
usuarios = {
    "admin": "123",
    "ivanna": "2002",
    "manu": "2505"
}

# Número máximo de intentos permitidos
intentos_restantes = 3

while intentos_restantes > 0:
    # Solicitar usuario y contraseña
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Validar usuario y contraseña
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Acceso correcto")
        break
    else:
        intentos_restantes -= 1
        print(f"Usuario o contraseña incorrectos. Te quedan {intentos_restantes} intentos.")
        
    if intentos_restantes == 0:
        print("Has agotado todos los intentos. Acceso denegado.")
