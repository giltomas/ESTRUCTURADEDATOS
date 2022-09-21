#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     17/09/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("FACEBOOK")
    contraseña = "python01"
    contador = 1
    while True:
        clave = input("Ingrese la contraseña: ")
        contador = contador + 1
        if clave == contraseña:
            print("Contraseña correcta")
            break
        if clave != contraseña and contador==4:
            print("Contraseña incorrecta")
            print("¿Se ha olvidado la contraseña?")
        if clave != contraseña and contador>6:
            print("Contraseña incorrecta")
            print("Vuelva a intentarlo nuevamente dentro de 5 minutos")
            break
    print("Siguiente")



if __name__ == '__main__':
    main()
