#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     11/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def suma (numero):
        sumados = 0
        for i in range(numero):
            sumados += i
        print("El total de la suma es", sumados)

    suma(11)




if __name__ == '__main__':
    main()
