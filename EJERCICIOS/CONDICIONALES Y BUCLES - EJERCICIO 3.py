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
    while True:
        email = input("Ingrese su e-mail: ")
        if email == "@":
            print("E-mail correcto")
            break
        if email != "@":
            print("E-mail incorrecto")
            break
    print("Siguiente")



if __name__ == '__main__':
    main()
