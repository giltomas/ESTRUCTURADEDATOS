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
    # Ejercicio 6
    # Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales,
    # consonantes y otros caracteres que no sean letras (signos de puntuación números,
    # espacios, etc.). Luego utilizando las operaciones de pila resolver las siguientes consignas:
    # a) cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
    # b) cantidad de espacios en blanco;
    # c) porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo;
    # d) cantidad de números;
    # e) determinar si la cantidad de vocales y otros caracteres son iguales;
    # f) determinar si existe al menos una z en la pila de consonantes.
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

        def saber_tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio

        def contenido(self):
            paux=Pila()
            while (not self.pila_vacia()):
                nro = self.desapilar()
                paux.apilar(nro)
            while (not paux.pila_vacia()):
                nro = paux.desapilar()
                print(nro)
                self.apilar(nro)

        def buscar_caracter(self, caracter):
            paux=Pila()
            contador=0
            while (not self.pila_vacia()):
                nodo=self.desapilar()
                paux.apilar(nodo)
            while (not paux.pila_vacia()):
                letra1=paux.en_cima()
                nodo=paux.desapilar()
                if (letra1 == caracter):
                    contador+= 1
            return contador

        def contar_numeros(self):
            paux=Pila()
            contador=0
            while (not self.pila_vacia()):
                nodo=self.desapilar()
                paux.apilar(nodo)
            while (not paux.pila_vacia()):
                letra1=paux.en_cima()
                nodo=paux.desapilar()
                if (letra1 in ["0","1","2","3","4","5","6","7","8","9"]):
                    contador+= 1
            print(f'La pila tiene {contador} números\n')

    ##    Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales,
    ##    consonantes y otros caracteres que no sean letras (signos de puntuación números,
    ##    espacios, etc.).

    parrafo= "1Oid mortales, 2el grito sagrado, 3libertad, libertad, libertad. 4Oid el grito de rotas cadenas, 5ved el trono a la noble igualdad."
    parrafo=parrafo.lower()

    pilaparrafo=Pila()
    pilasinseparar=Pila()

    for letra in parrafo:
        pilaparrafo.apilar(letra)
        pilasinseparar.apilar(letra)

    vocales=Pila()
    consonantes=Pila()
    caracteresespeciales=Pila()



    while (not pilaparrafo.pila_vacia()):
        letra=pilaparrafo.en_cima()
        pilaparrafo.desapilar()
        if (letra in ["a","e","i","o","u"]):
            vocales.apilar(letra)
        elif (letra in ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]):
            consonantes.apilar(letra)
        else:
            caracteresespeciales.apilar(letra)



    ##    a) cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
    print(f'Cantidad de caracteres de cada tipo: \n {vocales.saber_tamanio()} vocales. \n {consonantes.saber_tamanio()} consonantes. \n {caracteresespeciales.saber_tamanio()} caracteres especiales. \n ')

    ##    b) cantidad de espacios en blanco;
    print(f'Buscar cantidad de espacios en blanco')
    print(f'Cantidad de espacios en blanco: {caracteresespeciales.buscar_caracter(" ")}')

    ##    c) porcentaje que representan las vocales respecto de las consonantes sobre el
    ##    total de caracteres del párrafo;
    print(f'\nPorcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo:')
    tamañovocales=vocales.saber_tamanio()
    tamañoconsonantes=consonantes.saber_tamanio()
    tamañocesp=caracteresespeciales.saber_tamanio()

    total=tamañovocales+tamañoconsonantes+tamañocesp
    print(f'El total es {total}')

    porcentaje=tamañovocales * 100 / total

    print(f'El porcentaje de vocales es {porcentaje:.2f} \n ')

    ##    d) cantidad de números;
    print(f'Contar números:')
    pilasinseparar.contar_numeros()

    ##    e) determinar si la cantidad de vocales y otros caracteres son iguales;
    print("Determinar si la cantidad de vocales y otros caracteres son iguales:")
    if (tamañovocales == tamañocesp+tamañoconsonantes):
        print("La cantidad de vocales y otros caracteres son iguales\n")
    else:
        print("La cantidad de vocales y otros caracteres NO son iguales \n")

    ##    f) determinar si existe al menos una z en la pila de consonantes.
    print("Determinar si existe al menos una z en la pila de consonantes:")
    if consonantes.buscar_caracter("z") > 0:
        print("La z existe al menos una vez")
    else:
        print("La z no existe al menos una vez")

if __name__ == '__main__':
    main()
