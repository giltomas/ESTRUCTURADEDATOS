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
    ##    Ejercicio 5 Implementar los algoritmos necesarios para resolver las siguientes tareas:
    ##    a). concatenar dos listas, una atrás de la otra;
    ##    b). concatenar dos listas en una sola omitiendo los datos repetidos y
    ##    manteniendo su orden;
    ##    c). contar cuántos elementos repetidos hay entre dos listas;
    ##    d). eliminar todos los nodos de una lista de a uno a la vez mostrando su
    ##    contenido.


    class nodoLista(object) :
        """Clase nodo lista"""
        posicion, sig, valor = None, None, None

    class Lista(object) :
        """Clase Lista enlazada simple"""
        def __init__(self) :
            """Crea una lista vacía"""
            self.inicio = None
            self.tamanio = 0

        def insertar(self, posicion, valor) :
            """Inserta un elemento segun la posición"""
            nodo = nodoLista()
            nodo.posicion = posicion
            nodo.valor = valor

            if (self.inicio is None) or (self.inicio.posicion > posicion) :
                nodo.sig = self.inicio
                self.inicio = nodo
            else :
                ant = self.inicio # anterior
                act = self.inicio.sig # actual

                while (act is not None and act.posicion < posicion) :
                    ant = ant.sig
                    act = act.sig

                nodo.sig = act
                ant.sig = nodo

            self.tamanio += 1

        def insertar_al_final(self, valor) :
            """Inserta un elemento en la última posición"""
            nodo = nodoLista()
            nodo.posicion = self.tamanio
            nodo.valor = valor

            if (self.inicio is None) or (self.inicio.posicion > nodo.posicion) :
                nodo.sig = self.inicio
                self.inicio = nodo
            else :
                ant = self.inicio # anterior
                act = self.inicio.sig # actual

                while (act is not None and act.posicion < nodo.posicion) :
                    ant = ant.sig
                    act = act.sig

                nodo.sig = act
                ant.sig = nodo

            self.tamanio += 1

        def eliminar(self, clave) :
            """Elimina un elemento segun su posición y lo devuelve si lo encuentra"""
            dato = None


            if (self.inicio.posicion == clave) :
                dato = self.inicio.valor
                self.inicio = self.inicio.sig
                self.tamanio -= 1
            else :
                ant = self.inicio
                act = self.inicio.sig

                while (act is not None and act.posicion != clave) :
                    ant = ant.sig
                    act = act.sig

                if (act is not None) :
                    dato = act.valor
                    ant.sig = act.sig
                    self.tamanio -= 1

            return dato

        def buscar(self, buscado) :
            """Devuelve valor del elemento buscado por su posición"""
            aux = self.inicio

            while (aux is not None and aux.posicion != buscado) :
                aux = aux.sig

            return aux.valor

        def buscar_repetido(self, buscado) :
            """Devuelve la dirección del elemento buscado"""
            aux = self.inicio
            resultado=0
            while (aux is not None):
                if (aux.valor == buscado) :
                    resultado+=1
                aux = aux.sig

            return resultado-1

        def lista_vacia(self) :
            """Devuelve true si la lista está vacía"""
            return self.inicio is None

        def que_tamanio(self) :
            """Devuelve el número de elementos en la lista"""
            return self.tamanio

        def barrido(self) :
            """Realiza un barrido de la lista mostrando los valores"""
            aux = self.inicio

            while (aux is not None) :
                print(aux.valor)
                aux = aux.sig

        def concatenar(self, lista_elegida):
            nodo = lista_elegida.inicio
            while (nodo is not None) :
                self.insertar_al_final(nodo.valor)

                nodo = nodo.sig

        def concatenar_sin_repetir(self, lista_elegida):
            nodo = lista_elegida.inicio

            while (nodo is not None):
                if (self.buscar_repetido(nodo.valor) == -1):
                    self.insertar_al_final(nodo.valor)
                nodo = nodo.sig

    nueva_lista=Lista()

    frase="ALEGRIA"

    i=0
    for letra in frase:
        nueva_lista.insertar(i,letra)
        i+=1


    nueva_lista.insertar_al_final('z')


    ## a). concatenar dos listas, una atrás de la otra
    print('a. Concatenar dos listas, una atrás de la otra:')
    print('Creé método concatenar\n')
    #doslistas
    unalista=Lista()
    doslista=Lista()

    frase='corazón'

    for letra in frase:
        unalista.insertar_al_final(letra)

    frase2='melon'

    for letra in frase2:
        doslista.insertar_al_final(letra)

    unalista.concatenar(doslista)


    ##b). concatenar dos listas en una sola omitiendo los datos repetidos y
    ##    manteniendo su orden;

    print('b. Concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden')
    blista=Lista()
    frase='paraguas'

    for letra in frase:
        blista.insertar_al_final(letra)

    b2lista=Lista()
    frase='helado'

    for letra in frase:
        b2lista.insertar_al_final(letra)

    granlista=Lista()


    granlista.concatenar_sin_repetir(blista)
    granlista.concatenar_sin_repetir(b2lista)
    granlista.barrido()


    ##    c). contar cuántos elementos repetidos hay entre dos listas;
    print('\nc.Contar cuántos elementos repetidos hay entre dos listas;')
    print('Listas contadas: blista y b2lista, creadas en punto anterior, unidas en una gran lista')
    print('elementos sin repetir de la gran lista:', granlista.que_tamanio())
    granlista1=Lista()
    granlista1.concatenar(blista)
    granlista1.concatenar(b2lista)
    print('elementos totales de las listas concatenadas:', granlista1.que_tamanio())
    print('elementos repetidos entre las dos listas:', granlista1.que_tamanio()-granlista.que_tamanio())

    ##    d). eliminar todos los nodos de una lista de a uno a la vez mostrando su
    ##    contenido.

    print('\nd. Eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido')
    granlista.barrido()

if __name__ == '__main__':
    main()
