#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     21/11/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    # Ejercicio 3
    #Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

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

        def contenido(self):
            paux=Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()
                paux.apilar(nro)
            while (not paux.pila_vacia()):
                nro = paux.desapilar()
                print(nro)
                self.apilar(nro)

        def invertir(self):
            paux = Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()
                print(nro)
                paux.apilar(nro)

            return paux

    # Creo una pila de datos
    pdatos = Pila()

    #Creo una lista de elementos
    elementos = [9,2,6,9,3,8,5,5,6,1,0,9,2,6,8,3,6,5,5,6]

    # Apilo los elementos
    for nro in elementos:
        pdatos.apilar(nro)

    print("Contenido de la pila")
    pdatos.contenido()
    print("\n")

    print("Contenido de la pila invertida")
    pdatos.invertir()






if __name__ == '__main__':
    main()
