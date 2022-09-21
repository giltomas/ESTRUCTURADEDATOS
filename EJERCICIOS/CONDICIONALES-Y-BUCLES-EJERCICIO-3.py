#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     18/09/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #Ejercicio 3 de condicionales y bucles
    contador = 1
    while True:
        email = input("Ingrese su e-mail: ")
        contador += 0
        if email == "@":
            print("E-mail correcto")
            break
        if email != "@":
            print("Error, lo recientemente ingresado no pertenece a una dirección e-mail")
            contador += 1
        if email != contador>3:
            print("Intentelo nuevamente dentro de 5 minutos")
            break
    print("Siguiente")



if __name__ == '__main__':
    main()
