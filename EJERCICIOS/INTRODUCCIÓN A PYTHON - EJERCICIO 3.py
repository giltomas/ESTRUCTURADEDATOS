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
    #Ejercicio 1 de condicionales y bucles
    numeroimpar = (int(input("Ingrese un numero impar: ")))
    while numeroimpar % 2 == 0:
        numeroimpar = (int(input("Error, ingrese un numero impar: ")))
    print(f"El numero ingresado es impar: {numeroimpar}")




if __name__ == '__main__':
    main()
