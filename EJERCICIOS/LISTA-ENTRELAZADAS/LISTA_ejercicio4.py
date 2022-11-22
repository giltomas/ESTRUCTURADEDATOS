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
    ## Ejercicio 4 Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

    class nodoLista(object) :
        """Clase nodo lista"""
        info, sig, valor  = None, None, None

    class Lista(object) :
        """Clase Lista enlazada simple"""
        def __init__(self) :
            """Crea una lista vacía"""
            self.inicio = None
            self.tamanio = 0

        def insertar(self, posicion, valor) :
            """Inserta el dato a la lista"""
            nodo = nodoLista()
            nodo.info = posicion
            nodo.valor=valor

            if (self.inicio is None) or (self.inicio.info > posicion) :
                nodo.sig = self.inicio
                self.inicio = nodo
            else :
                ant = self.inicio # anterior
                act = self.inicio.sig # actual

                while (act is not None and act.info < posicion) :
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

        def tamanio(self) :
            """Devuelve el número de elementos en la lista"""
            return self.tamanio

        def barrido(self) :
            """Realiza un barrido de la lista mostrando los valores"""
            aux = self.inicio

            while (aux is not None) :
                print(aux.info, aux.valor)
                aux = aux.sig



    unaLista=Lista()

    unaLista.insertar(1,'Lionel')
    unaLista.insertar(5,'El Mejor de la Historia')
    unaLista.insertar(2,'Andrés')
    unaLista.insertar(3, 'Messi')


    unaLista.barrido()

    print('Insertamos un elemento en la lista')
    unaLista.insertar(4, 'Cuccitini')
    unaLista.barrido()

    print('Devuelvo valor eliminado')
    print(unaLista.eliminar(3))

if __name__ == '__main__':
    main()
