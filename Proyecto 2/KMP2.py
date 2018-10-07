#!/usr/bin/python
import sys

def kmp(P, T):
    m = 0 #salta dentro del texto y encuentra la posicion que se busca
    i = 0 #indice que recorre la palabra
    pos = 0 #es para saber cuando la palabra no existe
    l_p = len(P)#largo del patron
    l_t = len(T)#largo del texto
    if(l_t >= l_p):#tiene que ser mas grande el texto que el patron
        tabla = tabla_fallos(P)#se genera la tabla de fallos
        print ("La tabla de fallos es %s" %tabla)
        while((m<l_t) and (i<=l_p)):
            if(P[i] == T[m+i]):
                if(i == (l_p-1)):
                    pos = pos + 1 #regresa las posiciones donde se encuentre una coincidencia
                    print ("esta en la posicion %s" %m)
                    return
                i= i+1
            else:
                m = m + i - tabla[i]
                if(i>0):
                    i = tabla[i]
        if pos == 0:
            print ("no se encuentra")
    else:
        "no se puede"

def tabla_fallos(P):
    """recibe como parametro el patron y devuelve
    una tabla que contiene los saltos que se deben
    hacer
    """
    l_p = len(P)
    k = 0
    table = [0] * l_p
    for q in range(1, l_p):
        while P[k] != P[q] and k > 0:
            k = table[k - 1]
        if P[k] == P[q]:
            k += 1
        table[q] = k
    table.insert(0, -1)
    return table[:-1]

def main():
    """funcion principal
    """
    try:
        T = input("Inserta el texto.")
        P = input("Inserta el patron a buscar dentro del texto.")
    except:
        print ("No escribiste las frases")
        return
    print ("El texto es %s" %T)
    print ("La palabra a buscar es %s" %P)
    kmp(P, T)

from time import time
start = time()   
main()
end = time()- start
print(end)