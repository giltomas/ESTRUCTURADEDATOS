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
    ##    Ejercicio 9
    ##    Utilizando operaciones de cola y pila, invertir el contenido de una cola.


    class nodoCola(object) :
        """Clase nodo cola"""
        info, sig = None, None

    class Cola(object) :
        """Clase Cola"""
        def __init__(self) :
            """Crea una cola vacía"""
            self.frente, self.final = None, None
            self.tamanio = 0

        def arribo(self, dato) :
            """Arriba el elemento al final de la cola"""
            nodo = nodoCola()
            nodo.info = dato

            if self.frente is None :
                self.frente = nodo
            else :
                self.final.sig = nodo

            self.final = nodo
            self.tamanio += 1

        def atencion(self) :
            """Atiende el elemento en el frente de la cola y lo devuelve"""
            dato = self.frente.info
            self.frente = self.frente.sig
            if self.frente is None :
                self.final = None

            self.tamanio -= 1

            return dato

        def cola_vacia(self) :
            """Devuelve true si la cola está vacía"""
            return self.frente is None

        def en_frente(self) :
            """Devuelve el valor almacenado en el frente de la cola"""
            if self.frente is not None :
                return self.frente.info

        def tamanio(self) :
            """Devuelve el nro de elementos en la cola"""
            return self.tamanio

        def mover_al_final(self) :
            """Mueve el elemento del frente al final de la cola"""
            dato = atencion(self)
            arribo(self, dato)

            return dato


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

        def buscar_tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio


    datos=["a","d","j","k",'h','l','k','j','d','f','g','k','l','a','j','d','k','g','l','j','f','d','z']

    unacola=Cola()
    unapila=Pila()
    otrapila=Pila()

    for elemento in datos:
        unacola.arribo(elemento)

    while (not unacola.cola_vacia()):
        elemento=unacola.atencion()
        unapila.apilar(elemento)

    print(unapila.en_cima())

    while (not unapila.pila_vacia()):
        elemento=unapila.desapilar()
        otrapila.apilar(elemento)

    while (not otrapila.pila_vacia()):
        elemento=otrapila.desapilar()
        unacola.arribo(elemento)

if __name__ == '__main__':
    main()
