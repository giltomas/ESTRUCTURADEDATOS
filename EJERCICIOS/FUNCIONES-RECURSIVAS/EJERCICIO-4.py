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
    def mostrar(lista, ind):
        lista.reverse()
        if ind != len(lista):
            print(lista[ind])
            mostrar(lista, ind+1)

    lista = [1, 2, 3, 4, 5]
    mostrar(lista, 0)

if __name__ == '__main__':
    main()
