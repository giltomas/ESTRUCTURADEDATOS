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
    ##    Ejercicio 7
    ##    Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por
    ##    ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de
    ##    acuerdo a su peso –del objeto más liviano al más pesado–. Solo pueden utilizar pilas
    ##    auxiliares como estructuras extras, no se pueden utilizar métodos de ordenamiento.


    class nodoPila(object) :
        """Clase nodo pila"""
        nombre, peso, sig = None, None, None

    class Pila(object) :
        """Clase Pila"""
        def __init__(self) :
            self.cima = None
            self.tamanio = 0

        def apilar(self, nombre, peso) :
            """Apila el elemento sobre la cima de la pila"""
            nodo = nodoPila()
            nodo.nombre = nombre
            nodo.peso = peso
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
                return self.cima.nombre, self.cima.peso
            else :
                return None

        def tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio

        def ordenar_por_peso(self) :
            mazo_ordenado = Pila()

            # Ordeno el mazo hasta vaciarlo
            while (not self.pila_vacia()) :
                # Obtengo el primer elemento
                nodo = self.desapilar()
                print('DEBUG: nodo peso: ', nodo.peso)

                # Mientras que el mazo ordenado no esté vacío
                # y la cima del mazo ordenado sea mayor a la cima del mazo desordenado
                while (not mazo_ordenado.pila_vacia() and mazo_ordenado.cima.peso > nodo.peso):
                    # Quito el nodo de la cima
                    mayor = mazo_ordenado.desapilar()
                    print('DEBUG: Apilo mayor: ', mayor.peso)

                    # Apilo la cima del mazo ordenado en la cima del mazo desordenado
                    self.apilar(mayor.nombre, mayor.peso)

                # Apilo la carta en el mazo ordenado
                mazo_ordenado.apilar(nodo.nombre, nodo.peso)
                print('DEBUG: apilar elemento \n')

            # Pasar del mazo ordenado DESC al mazo vacío
            while (not mazo_ordenado.pila_vacia()) :
                nodo = mazo_ordenado.desapilar()
                self.apilar(nodo.nombre, nodo.peso)


    ##    Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por
    ##    ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.)

    piladeobjetos=Pila()

    piladeobjetos.apilar("mochila", 1)
    piladeobjetos.apilar("teclado", 0.25)
    piladeobjetos.apilar("silla", 7)

    ##  Ordenar dicha pila de acuerdo a su peso –del objeto más liviano al más pesado–.
    piladeobjetos.ordenar_por_peso()
    print(f'El objeto más liviano es {piladeobjetos.en_cima()}')

if __name__ == '__main__':
    main()
