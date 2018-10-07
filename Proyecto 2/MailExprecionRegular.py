import re

def ValidarCorreo(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        print ("Correo correcto")
    else:
        print ("Correo incorrecto")
        
def IngresarDatos():
    correo = input("Inserta la direccion de correo electronico")
    ValidarCorreo(correo)
    
from time import time
start = time()   
IngresarDatos()
end = time()- start
print(end)