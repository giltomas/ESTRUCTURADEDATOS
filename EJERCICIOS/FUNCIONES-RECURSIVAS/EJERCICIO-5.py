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
    #Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
    def recorrer(lista):
        for i in lista:
            if lista != []:
                print(i)
            else:
                return recorrer(lista)

    lista1 =  [[23,45,63],[72,81,91],[56,64,37],[34,75,26]]
    recorrer(lista1)

if __name__ == '__main__':
    main()
