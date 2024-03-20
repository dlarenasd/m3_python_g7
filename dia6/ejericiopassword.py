import getpass
#crear un script de ingreso de password
#donde el largo mínimo es de 6 caracteres
#password = input("Ingrese su contraseña: \n")
password = getpass.getpass ("Ingrese su contraseña: \n")

if password == 12345:
    print("Password incorrecto")

elif len(password)<6:
    print("Su contraseña es demasiado corta, debe tener mínimo 6 caracteres")
