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
    lista = [40, 6, 12, 24, 48, 96]
    menor = lista[0]
    for i in lista:
        if i<menor:
            menor = i
    print("El valor minimo es", menor)




if __name__ == '__main__':
    main()
