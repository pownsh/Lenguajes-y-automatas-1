import random

def GeneradorLenguaje (n,alfabeto):
    lenguaje = []
    palabra=""
    control = 0
    while control != n:
        longitud=random.randint(1, 6)
        palabra=palabra.join(random.choice(alfabeto) for _ in range(longitud))
        if palabra not in lenguaje:
            lenguaje.append(palabra)
            control = control +1
            palabra = ""
        else:
            palabra = ""
    return(lenguaje)

def GenerardorAlfabeto(lenguaje):
    alfabeto = []
    frase = "".join(lenguaje)
    for i in frase:
        if i not in alfabeto:
            alfabeto.append(i)
    
    alfabeto.sort()
    return (alfabeto)

def ingresarDatos():
    
    prueba = input(" Ingresa (a) si deseas ontener un alfabeto a partir de un lenguaje \n Ingresa (l) si deseas obtener un lenguaje a partir de un alfabeto")
    if prueba == "l":
        alfabeto = input("Ingresa las letras del alfabeto a utilizar.")
        n = int(input("Ingresa la cantidad de palabras que generara el lenguaje."))
        print(GeneradorLenguaje(n,alfabeto))
    if prueba == "a":
        lenguaje = input("Ingresa las palabras que deseas utilizar separadas por esacios.")
        lenguaje = lenguaje.split()
        print(GenerardorAlfabeto(lenguaje))

from time import time
start = time()   
ingresarDatos()
end = time()- start
print(end)