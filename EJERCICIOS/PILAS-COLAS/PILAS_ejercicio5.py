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
    # Ejercicio 5
    # Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de cartas de baraja española–,resolver las siguientes actividades:
    # a) generar las cartas del mazo de forma aleatoria;
    # b) separar la pila mazo en cuatro pilas una por cada palo;
    # c) ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
    import random
    class nodoPila(object) :
        """Clase nodo pila"""
        nro, palo, sig = None, None, None

    class Pila(object) :
        """Clase Pila"""
        def __init__(self) :
            self.cima = None
            self.tamanio = 0

        def apilar(self, nro, palo) :
            """Apila el elemento sobre la cima de la pila"""
            nodo = nodoPila()
            nodo.nro = nro
            nodo.palo = palo
            nodo.sig = self.cima

            self.cima = nodo
            self.tamanio += 1

        def desapilar(self) :
            """Desapila el elemento de la cima de la pila y lo devuelve"""
            x = self.cima
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

        def contenido(self) :
            paux = Pila()

            while (not self.pila_vacia()) :
                carta = self.desapilar()
                print(carta.nro, 'de', palos[carta.palo])
                paux.apilar(carta.nro, carta.palo)

            while (not paux.pila_vacia()) :
                carta = paux.desapilar()
                self.apilar(carta.nro, carta.palo)

        def ordenar(self) :
            mazo_ordenado = Pila()

            # Ordeno el mazo hasta vaciarlo
            while (not self.pila_vacia()) :
                # Obtengo el primer elemento
                nodo = self.desapilar()
                print('DEBUG: nodo nro: ', nodo.nro)

                # Mientras que el mazo ordenado no esté vacío
                # y la cima del mazo ordenado sea mayor a la cima del mazo desordenado
                while (not mazo_ordenado.pila_vacia() and mazo_ordenado.cima.nro > nodo.nro) :
                    # Quito el nodo de la cima
                    mayor = mazo_ordenado.desapilar()
                    print('DEBUG: Apilo mayor: ', mayor.nro)

                    # Apilo la cima del mazo ordenado en la cima del mazo desordenado
                    self.apilar(mayor.nro, mayor.palo)

                # Apilo la carta en el mazo ordenado
                mazo_ordenado.apilar(nodo.nro, nodo.palo)
                print('DEBUG: apilar carta \n')

            # Pasar del mazo ordenado DESC al mazo vacío
            while (not mazo_ordenado.pila_vacia()) :
                nodo = mazo_ordenado.desapilar()
                self.apilar(nodo.nro, nodo.palo)


    mazo = Pila()
    palos = ['espada', 'basto', 'copa', 'oro']
    cartas = []

    ## a) generar las cartas del mazo de forma aleatoria
    while (len(cartas) != 40) :
        palo = random.randint(0, 3)
        nro = random.randint(1, 10)
        carta = [nro, palo]

        if (carta not in cartas) :
            cartas.append(carta)
            mazo.apilar(nro, palo)

    ## b) separar la pila mazo en cuatro pilas una por cada palo

    pespada = Pila()
    pbasto = Pila()
    pcopa = Pila()
    poro = Pila()

    while (not mazo.pila_vacia()) :
        carta = mazo.desapilar()

        if (carta.palo == 0) :
            pespada.apilar(carta.nro, carta.palo)
        elif (carta.palo == 1) :
            pbasto.apilar(carta.nro, carta.palo)
        elif (carta.palo == 2) :
            pcopa.apilar(carta.nro, carta.palo)
        else :
            poro.apilar(carta.nro, carta.palo)

    ## c) ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente
    seleccion = int(input("Ingrese un nro: \n 1 - Espada \n 2 - Basto \n 3 - Copa \n 4 - Oro"))

    while (seleccion not in [1,2,3,4] ):
        seleccion = int(input("Ingrese un nro: \n 1 - Espada \n 2 - Basto \n 3 - Copa \n 4 - Oro"))

    if (seleccion-1 == 0) :
        pila = pespada
    elif (seleccion-1 == 1) :
        pila = pbasto
    elif (seleccion-1 == 2) :
        pila = pcopa
    else :
        pila = poro


    print('\nMazo desordenado')
    pila.contenido()
    pila.ordenar()
    print('\nMazo ordenado')
    pila.contenido()


if __name__ == '__main__':
    main()
