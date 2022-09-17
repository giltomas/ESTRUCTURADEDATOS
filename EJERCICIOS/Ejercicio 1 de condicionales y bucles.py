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
    #Ejercicio 2 de condicionales y bucles
    print("OPERACIONES ARITMETICAS")
    numerouno = (int(input("Ingrese su primer numero: ")))
    numerodos = (int(input("Ingrese su segundo numero: ")))
    opcion = (int(input("Ingrese la opción que quiera, 1. Sumar, 2. Restar, 3. Multiplicar: ")))
    while opcion < 1 or opcion > 3:
        print("Error, vuelva a elegir una opción")
        opcion = (int(input("Ingrese la opción que quiera: 1. Sumar, 2. Restar, 3. Multiplicar")))
    if opcion == 1:
        print(f"La opción escogida es sumar: {numerouno} + {numerodos} = {numerouno + numerodos}")
    if opcion == 2:
        print(f"La opción escogida es restar: {numerouno} - {numerodos} = {numerouno - numerodos}")
    if opcion == 3:
        print(f"La opción escogida es multiplicar: {numerouno} * {numerodos} = {numerouno * numerodos}")
    print("Operación finalizada")




if __name__ == '__main__':
    main()
