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
    impar = int(input("Ingrese un numero impar: "))
    while impar % 2 == 0:
        impar = int(input("Ingrese un numero impar: "))
    print("Ingreso un numero impar", impar)





if __name__ == '__main__':
    main()
