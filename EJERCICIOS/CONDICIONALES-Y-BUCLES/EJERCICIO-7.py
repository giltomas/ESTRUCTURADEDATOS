#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     08/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #Ejercicio numero 7 de condicionales y bucles, no utilizar max
    lista = [2, 6, 12, 24, 48, 96]
    mayor = 0
    for i in lista:
        if i>mayor:
            mayor = i
    print("El valor maximo es", mayor)




if __name__ == '__main__':
    main()
