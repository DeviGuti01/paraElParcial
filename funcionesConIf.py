# Condiciones Anidadas

usuario = input("¿Eres admin o invitado?: ").lower() # El lower es para reconocer mayusculas o minusculas
clave = "admin123"

if usuario == "admin":
    contrasena = input("Introduce la clave: ")
    if contrasena == clave:
        print("Acceso permitido")
    else: 
        print("clave incorrecta")
    if usuario == "invitado":
        print("Bienvenido como invitado")
    else:
        print("Usuario no reconocido")
