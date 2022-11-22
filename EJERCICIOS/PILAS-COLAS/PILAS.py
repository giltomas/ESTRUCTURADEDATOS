#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Tomas
#
# Created:     19/11/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    class nodoPila(object) :
        """Clase nodo pila"""
        info, sig = None, None

    class Pila(object) :
        """Clase Pila"""
        def __init__(self) :
            self.cima = None
            self.tamanio = 0

        def apilar(self, dato) :
            """Apila el elemento sobre la cima de la pila"""
            nodo = nodoPila()
            nodo.info = dato
            nodo.sig = self.cima

            self.cima = nodo
            self.tamanio += 1

        def desapilar(self) :
            """Desapila el elemento de la cima de la pila y lo devuelve"""
            x = self.cima.info
            self.cima = self.cima.sig
            self.tamanio -= 1

            return x

        def pila_vacia(self) :
            """Devuelve true si la pila está vacía"""
            return self.cima is None

        def en_cima(self) :
            """Devuelve el valor almacenado en la cima de la pila"""
            if self.cima is not None :
                return self.cima.info
            else :
                return None

        def tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio



    pdatos = Pila()
    ppar = Pila()
    pimpar = Pila()

    dato = int(input("Ingrese un numero - 0 para salir: "))

    while (dato != 0):
        pdatos.apilar(dato)
        dato = int(input("Ingrese un numero - 0 para salir: "))

    while (not pdatos.pila_vacia()):
        dato = pdatos.desapilar()
        if (dato % 2 == 0):
            ppar.apilar(dato)

        else:
            pimpar.apilar(dato)

    while (not ppar.pila_vacia()):
        dato = ppar.desapilar()
        print(dato)

    while (not pimpar.pila_vacia()):
        dato = pimpar.desapilar()
        print(dato)








































if __name__ == '__main__':
    main()
