
def verificarCorreo(correo):
    if correo.islower():
        if "@" in correo:
            usuario,dominio = correo.split("@")
            if "." in dominio:
                print ("Correo valido")
            else:
                print ("Correo falso")
        else:
            print("correo falso")
    else:
        print("correo falso")
        
def IngresarDatos():
    correo = input("Inserta la direccion de correo electronico")
    verificarCorreo(correo)
    
from time import time
start = time()   
IngresarDatos()
end = time()- start
print(end)