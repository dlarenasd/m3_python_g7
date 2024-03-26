from string import ascii_lowercase
import getpass



password = getpass.getpass("Ingresa tu mejor contraseña con solo minúsculas, sin ñ, sin símbolos y sin espacio: ").lower()
letras= ascii_lowercase
print("Veamos cuántos intentos le toma al programa descifrarla")
contador = 0

for caracter in password:
    for letra in letras:
        contador +=1
        if letra == caracter:
            break
print(f"La contraseña fue forzada en {contador} intentos")