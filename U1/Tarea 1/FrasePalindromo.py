
frase = input("Ingresa la frase a analizar ::> ")

# Quitar acentos y signos de puntuaci�n
traduccion = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ.,;!¡¿?", "aeiouunAEIOUUN       ")
frase = frase.translate(traduccion)

# Quitar espacios
frase = "".join(frase.split())

# Pasar todo a min�sculas
frase =frase.lower()

# Comprobar resultado palindr�mico
if frase == frase[::-1]:
    print ("Es Palindromo")
else:
    print ("No es palindromo")