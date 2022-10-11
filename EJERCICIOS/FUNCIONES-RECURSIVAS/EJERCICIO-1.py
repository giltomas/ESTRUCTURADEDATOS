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
    lista = []
    promedios = []
    totcadena = []
    def datos(lista):
        codsuc = input("Ingrese el codigo de la sucursal: ")
        while codsuc != "0":
            nomsuc = input("Ingrese el nombre de la sucursal: ")
            ventas = int(input("Ingrese las ventas de la sucursal: "))
            total = int(input("Ingrese el total de las ventas: "))
            promedio = total/ventas
            lista.append(codsuc)
            lista.append(nomsuc)
            lista.append(ventas)
            lista.append(total)
            promedios.append(promedio)
            totcadena.append(total)
            codsuc = input("Ingrese el codigo de la sucursal: ")
        else:
            return

    def imprimir_datos(lista):
        print("Su lista es", lista)

    print(datos(lista))
    if lista != []:
        imprimir_datos(lista)
        print("Sus promedios son", promedios)
        print("El total vendido por la cadena es", totcadena)




if __name__ == '__main__':
    main()
