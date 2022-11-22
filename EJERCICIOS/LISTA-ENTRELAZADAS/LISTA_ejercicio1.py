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
    # Ejercicio 1
    # Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.


    class nodoLista(object) :
        """Clase nodo lista"""
        info, sig = None, None

    class Lista(object) :
        """Clase Lista enlazada simple"""
        def __init__(self) :
            """Crea una lista vacía"""
            self.inicio = None
            self.tamanio = 0

        def insertar(self, dato) :
            """Inserta el dato a la lista"""
            nodo = nodoLista()
            nodo.info = dato

            if (self.inicio is None) or (self.inicio.info > dato) :
                nodo.sig = self.inicio
                self.inicio = nodo
            else :
                ant = self.inicio # anterior
                act = self.inicio.sig # actual

                while (act is not None and act.info < dato) :
                    ant = ant.sig
                    act = act.sig

                nodo.sig = act
                ant.sig = nodo

            self.tamanio += 1

        def eliminar(self, clave) :
            """Elimina un elemento de la lista y lo devuelve si lo encuentra"""
            dato = None

            if (self.inicio.info == clave) :
                dato = self.inicio.info
                self.inicio = self.inicio.sig
                self.tamanio -= 1
            else :
                ant = self.inicio
                act = self.inicio.sig

                while (act is not None and act.info != clave) :
                    ant = ant.sig
                    act = act.sig

                if (act is not None) :
                    dato = act.info
                    ant.sig = act.sig
                    self.tamanio -= 1

            return dato

        def buscar(self, buscado) :
            """Devuelve la dirección del elemento buscado"""
            aux = self.inicio

            while (aux is not None and aux.info != buscado) :
                aux = aux.sig

            return aux

        def lista_vacia(self) :
            """Devuelve true si la lista está vacía"""
            return self.inicio is None

        def que_tamanio(self) :
            """Devuelve el número de elementos en la lista"""
            return self.tamanio

        def contenido(self) :
            """Realiza un contenido de la lista mostrando los valores"""
            aux = self.inicio

            while (aux is not None) :
                print(aux.info)
                aux = aux.sig


    miLista=Lista()

    elementos=[1,2,3,4,5,6,7,8,9]

    for elemento in elementos:
        miLista.insertar(elemento)

    print("La cantidad de elementos de esta lista es:")
    print(miLista.que_tamanio())

if __name__ == '__main__':
    main()
