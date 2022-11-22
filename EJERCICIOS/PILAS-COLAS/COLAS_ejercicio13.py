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
    ##    Ejercicio 13
    ##    Dada una cola con los códigos de turnos de atención (con el formato #@@, donde # es
    ##    una letra de la A hasta la F y “@@” son dos dígitos desde el 01 al 20), desarrollar un
    ##    algoritmo que resuelva las siguientes situaciones:
    ##    a) cargar 20 turnos de manera aleatoria a la cola.
    ##    b) separar la cola con datos en dos colas, cola_1 con los turnos que empiezan
    ##    con la letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E).
    ##    c) determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál
    ##    de las letras tiene mayor cantidad.
    ##    d) mostrar los turnos de la cola con menor cantidad de elementos, cuyo número
    ##    de turno sea mayor que 506.


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

        def que_tamanio(self) :
            """Devuelve el nro de elementos en la cola"""
            return self.tamanio

        def mover_al_final(self) :
            """Mueve el elemento del frente al final de la cola"""
            dato = atencion(self)
            arribo(self, dato)

            return dato
        def cargar_turnos(self, cantidad):
            for i in range(cantidad):
                turno=letras[random.randint(0,5)]+str(random.randint(0, 20))
                unacola.arribo(turno)
                print(turno)

        def separar_en_dos(self):
            cAux=Cola()
            cola_1=Cola()
            cola_2=Cola()
            while (not self.cola_vacia()):
                elemento=self.atencion()
                cAux.arribo(elemento)
            while (not cAux.cola_vacia()):
                elemento=cAux.atencion()
                self.arribo(elemento)
                if (elemento[0] in ['A','C','F']):
                    cola_1.arribo(elemento)
                else:
                    cola_2.arribo(elemento)
            print('Separación exitosa')
            print('Cola 1:')
            cola_1.imprimir_valores()
            print('Cola 2:')
            cola_2.imprimir_valores()

        def imprimir_valores(self):
            cAux=Cola()
            while (not self.cola_vacia()):
                elemento=self.atencion()
                cAux.arribo(elemento)
            while (not cAux.cola_vacia()):
                elemento=cAux.atencion()
                print(elemento)
                self.arribo(elemento)

        def contar_letra(self, letra):
            cAux=Cola()
            contador=0
            while (not self.cola_vacia()):
                elemento=self.atencion()
                cAux.arribo(elemento)
            while (not cAux.cola_vacia()):
                elemento=cAux.atencion()
                self.arribo(elemento)
                if (elemento[0] == letra):
                    contador+=1
                else:
                    contador=contador
            return contador


    """ Generación de nros aleatorios """
    # Importa módulo random
    import random
    # Genera nro aleatorio
    random.randint(0, 100)
    """ Generación de letras aleatorias """
    # Importa módulos string y random
    import string
    import random
    # Elije aleatoriamente una letra de todas las ascii_letters
    randomLetter = random.choice(string.ascii_letters)


    letras=['A','B','C','D','E','F']

    unacola=Cola()

    #a) cargar 20 turnos de manera aleatoria a la cola.

    unacola.cargar_turnos(20)

    ##    b) separar la cola con datos en dos colas, cola_1 con los turnos que empiezan
    ##    con la letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E).

    cAux=Cola()
    cola_1=Cola()
    cola_2=Cola()
    while (not unacola.cola_vacia()):
        elemento=unacola.atencion()
        cAux.arribo(elemento)
    while (not cAux.cola_vacia()):
        elemento=cAux.atencion()
        unacola.arribo(elemento)
        if (elemento[0] in ['A','C','F']):
            cola_1.arribo(elemento)
        else:
            cola_2.arribo(elemento)
    print('Separación exitosa')
    print('Cola 1:')
    cola_1.imprimir_valores()
    print('Cola 2:')
    cola_2.imprimir_valores()

    ##    c) determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál
    ##    de las letras tiene mayor cantidad.

    tamaño1=cola_1.que_tamanio()
    tamaño2=cola_2.que_tamanio()

    if tamaño1 > tamaño2:
        print('La cola 1 tiene mayor cantidad de turnos')
        letraA=cola_1.contar_letra('A')
        letraC=cola_1.contar_letra('C')
        letraF=cola_1.contar_letra('F')
        if (letraA > letraC and letraA > letraF):
            print(f'La letra A tiene mayor cantidad de turnos, son {letraA}')
        elif (letraC > letraA and letraC > letraF):
            print(f'La letra C tiene mayor cantidad de turnos, son {letraC}')
        else:
            print(f'La letra F tiene mayor cantidad de turnos, son {letraF}')
    else:
        print('La cola 2 tiene mayor cantidad de turnos')
        letraB=cola_2.contar_letra('B')
        letraD=cola_2.contar_letra('D')
        if (letraB > letraD):
            print(f'La letra que se repite más es la B, con {letraB} turnos')
        else:
            print(f'La letra que se repite más es la D, con {letraD} turnos')

if __name__ == '__main__':
    main()
