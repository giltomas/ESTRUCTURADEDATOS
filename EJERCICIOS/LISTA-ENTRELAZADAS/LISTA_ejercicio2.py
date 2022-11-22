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
    ##    Ejercicio 2 Diseñar un algoritmo que elimine todas las vocales que se encuentren en
    ##    una lista de caracteres.


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

        def eliminar_vocales(self):
    ##        while
    ##        lAux=Lista()
    ##        elemento=self.eliminar()
    ##        lAux.insertar(elemento)
            pass


    lista='aaadeeeshrrfladjehrikuoooioioioioldkjflsjdflksdklfjsdkoioioiilf'
    miListaenlazada=Lista()
    miListavocales=Lista()
    miListaconsonantes=Lista()

    for letra in lista:
        miListaenlazada.insertar(letra)




    # Separar vocales de consonantes
    nodo = miListaenlazada.inicio

    while (nodo is not None) :

        if (nodo.info in ['a','e','i','o']) :
            miListavocales.insertar(nodo.info)
        else :
            miListaconsonantes.insertar(nodo.info)

        nodo = nodo.sig

    # Imprimo vocales
    print('Imprimo vocales')
    miListavocales.contenido()
    print('\n')

    # Imprimo consonants
    print('Imprimo consonantes')
    miListaconsonantes.contenido()

if __name__ == '__main__':
    main()
