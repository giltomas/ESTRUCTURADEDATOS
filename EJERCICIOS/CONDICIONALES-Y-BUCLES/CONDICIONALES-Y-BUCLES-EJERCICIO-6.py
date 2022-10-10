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
    lista = [2, 4, 6, 8, 10]
    contador = 0
    suma = 0
    for i in lista:
        suma=suma+i
        contador+=1
    promedio = suma/contador
    print("El promedio es", promedio)



if __name__ == '__main__':
    main()
