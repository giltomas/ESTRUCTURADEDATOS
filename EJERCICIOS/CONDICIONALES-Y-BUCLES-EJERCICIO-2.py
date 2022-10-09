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
    numero1 = int(input("Ingrese su primer numero: "))
    numero2 = int(input("Ingrese su segundo numero: "))
    print("Elija una de las 3 opciones")
    opcion = int(input("1. Sumar, 2. Restar, 3. Multiplicar: "))
    while opcion<1 or opcion>3:
        print("opción incorrecta, vuelva a ingresar una opción")
        opcion = int(input("1. Sumar, 2. Restar, 3. Multiplicar: "))
    if opcion==1:
        print("La opción elegida es suma", numero1, "+", numero2, "=", numero1 + numero2)
    if opcion==2:
        print("La opción elegida es resta", numero1, "-", numero2, "=", numero1 - numero2)
    if opcion==3:
        print("La opción elegida es multiplicación", numero1, "x", numero2, "=", numero1 * numero2)




if __name__ == '__main__':
    main()
