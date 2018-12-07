
def AbrirArchivoTxt():
    codigoJava = open(r"C:\Users\Angel\Desktop\java.txt",'r')#abre el archivo .txt y lo guarda en la variable
    listaDeLineas=codigoJava.readlines()#separa cada linea en una lista y lo guarda en una variable
    return listaDeLineas# regresa la lista 

def Traductor(listaDeLineas):
    bandera = False# bandera de control para identacion
    for i in listaDeLineas:
        linea = i
        linea = linea.replace('public static void main(String[] args) {', '')
        linea = linea.replace('public static void', 'def')
        linea = linea.replace('public class prueba{', '')
        linea = linea.replace('{', ':')
        linea = linea.replace('int ', '')
        linea = linea.replace('}', '')
        linea = linea.replace('System.out.println', 'print')
        linea = linea.replace('\n','')
        linea = linea.replace(';','')
        linea = linea.replace('\t','')
        if bandera == True:
            linea = '    ' + linea
            bandera = False
        elif ':' in linea:
            bandera = True
        print(linea)

def CombertidorDeCodigo():
    listaDeLineas = AbrirArchivoTxt()
    Traductor(listaDeLineas)

from time import time
start = time()    
CombertidorDeCodigo()
end = time()- start
print(end)