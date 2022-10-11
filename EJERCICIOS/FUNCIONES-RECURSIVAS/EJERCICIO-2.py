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
    diccionarios = {}
    total = {"Monto total": 0, "Stock": 0}
    def datos(diccionarios):
        isbn = input("Ingrese el ISBN del libro: ")
        if (isbn != "0"):
            nombre = input("Ingrese el nombre del libro: ")
            stock = int(input("Ingrese el stock: "))
            precio = int(input("Ingrese el precio: "))
            diccionario = {"ISBN": isbn, "Nombre del libro": nombre, "Stock": stock, "Precio": precio}
            total["Stock"] = stock
            total["Monto total"] = precio * stock
            diccionarios[isbn] = diccionario
            datos(diccionarios)
        else:
            return

    datos(diccionarios)
    if diccionarios != {}:
        print(diccionarios)
        print("La cantidad total de libros es", total["Stock"])
        print("El monto total de los libros es $", total["Monto total"])
        print("El valor promedio de los libros es $", total["Monto total"] // total["Stock"])

if __name__ == '__main__':
    main()
