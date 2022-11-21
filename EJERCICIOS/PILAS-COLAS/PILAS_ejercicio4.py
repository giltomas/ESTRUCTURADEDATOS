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
    # Ejercicio 4
    # Determinar si una cadena de caracteres es un palíndromo.
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
                print(nro)
                paux.apilar(nro)
            while (not paux.pila_vacia()):
                nro = paux.desapilar()
                self.apilar(nro)

        def invertir(self):
            paux=Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()
                paux.apilar(nro)
            return paux

        def esPalindromo(self):
            paux=Pila()
            paux2=Pila()
            paux3=Pila()
            palindromo=True
            while (not self.pila_vacia()):
                nodo = self.desapilar()
                paux.apilar(nodo)
                paux2.apilar(nodo)
            while (not paux2.pila_vacia()):
                nodo = paux2.desapilar()
                paux3.apilar(nodo)
            while (not paux3.pila_vacia()):
                elemento1=paux.en_cima()
                paux.desapilar()
                elemento2=paux3.en_cima()
                paux3.desapilar()
                if (elemento1 != elemento2):
                    palindromo=False
            if (palindromo):
                print("Es palíndromo")
            else:
                print("No es palíndromo")

    caracteres=input('Ingrese una cadena de caracteres: ')

    cadena=Pila()

    for letra in caracteres:
        cadena.apilar(letra)


    cadena.esPalindromo()


if __name__ == '__main__':
    main()
