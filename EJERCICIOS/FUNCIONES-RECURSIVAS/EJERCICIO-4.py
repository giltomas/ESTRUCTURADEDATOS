#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Tomas
#
# Created:     11/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.
    def mostrar(lista):
        lista.reverse()
        for i in lista:
            if lista != []:
                print(i)
            else:
                return mostrar(lista)

    lista1 = [1, 2, 3, 4, 5]
    mostrar(lista1)

if __name__ == '__main__':
    main()
