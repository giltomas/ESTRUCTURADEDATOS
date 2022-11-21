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
    # Ejercicio 2
    # Reemplazar todas las ocurrencias de un determinado elemento en una pila.

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

        def reemplazar(self, elegido, reemplazo):
            pdatosreemplazo = Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()

                if (nro == elegido):
                    nro = reemplazo
                    pdatosreemplazo.apilar(nro)

                else:
                    pdatosreemplazo.apilar(nro)

            while (not pdatosreemplazo.pila_vacia()):
                nro = pdatosreemplazo.desapilar()
                print(nro)


        def contenido(self):
            paux = Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()
                print(nro)
                paux.apilar(nro)

            while (not paux.pila_vacia()):
                nro = paux.desapilar()
                self.apilar(nro)

    # Creo una pila
    pdatos = Pila()

    # Creo una lista de elementos
    elementos = [9,8,2,6,5,0,9,2,1,8,3,4,9,8,3,2,7]

    # Ingreso los elemento en la pila
    for nro in elementos:
        pdatos.apilar(nro)

    # Me fijo que haya ingresado los elementos en la pila viendo el contenido
    pdatos.contenido()

    # Le pido al usuario un numero para reemplazar y el numero de reemplazo
    elegido = int(input("Dime el numero que quieres reemplazar: "))
    reemplazo = int(input("Dime un numero para reemplazar: "))

    pdatos.reemplazar(elegido, reemplazo)

    pdatos.contenido()






if __name__ == '__main__':
    main()
