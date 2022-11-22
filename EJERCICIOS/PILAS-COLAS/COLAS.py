#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     22/11/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
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
            """Atiende el elemento en el frente de la cola y
            lo devuelve"""
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

    cdatos = Cola()
    cvocales = Cola()

    letra = input("Ingrese un caracter: ")

    while (letra != ""):
        cdatos.arribo(letra)
        letra = input("Ingrese un caracter: ")

    while (not cdatos.cola_vacia()):
        letra = cdatos.atencion()
        if (letra.upper() in ["A", "E", "I", "O", "U"]):
            cvocales.arribo(letra)

    print("\nDatos cola vocales:")
    while (not cvocales.cola_vacia()):
        dato = cvocales.atencion()
        print(dato)









if __name__ == '__main__':
    main()
