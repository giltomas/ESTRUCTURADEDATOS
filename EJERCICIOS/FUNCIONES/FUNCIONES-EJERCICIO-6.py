#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     10/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def separar(listanum):
        par = []
        impar = []
        for i in listanum:
            if i % 2 == 0:
                par.append(i)
            if i % 2 == 1:
                impar.append(i)
        return par, impar

    ordenada = separar(lista)
    print(ordenada)



if __name__ == '__main__':
    main()
