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
    ##    Ejercicio 11
    ##    Dada una cola con las notificaciones de las aplicaciones de redes sociales de un
    ##    Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la
    ##    emitió y el mensaje, resolver las siguientes actividades:
    ##    a) escribir una función que elimine de la cola todas las notificaciones de
    ##    Facebook;
    ##    b) escribir una función que muestre todas las notificaciones de Twitter, cuyo
    ##    mensaje incluya la palabra 'Python', si perder datos en la cola;
    ##    c) utilizar una pila para almacenar temporáneamente las notificaciones
    ##    producidas entre las 11:43 y las 15:57, y determinar cuántas son.

    from datetime import time

    class nodoCola(object) :
        """Clase nodo cola"""
        hora, app, mensaje, sig = None, None, None, None

    class Cola(object) :
        """Clase Cola"""
        def __init__(self) :
            """Crea una cola vacía"""
            self.frente, self.final = None, None
            self.tamanio = 0

        def arribo(self, hora, app, mensaje) :
            """Arriba el elemento al final de la cola"""
            nodo = nodoCola()
            nodo.mensaje = mensaje
            nodo.app = app
            nodo.hora = hora

            if self.frente is None :
                self.frente = nodo
            else :
                self.final.sig = nodo

            self.final = nodo
            self.tamanio += 1

        def atencion(self) :
            """Atiende el elemento en el frente de la cola y lo devuelve"""
            dato = self.frente
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
                return self.frente.mensaje, self.frente.hora, self.frente.app


        def que_tamanio(self) :
            """Devuelve el nro de elementos en la cola"""
            return self.tamanio

        def mover_al_final(self) :
            """Mueve el elemento del frente al final de la cola"""
            dato = atencion(self)
            arribo(self, dato)

            return dato

        def eliminar_red(self, red):
            cAux=Cola()
            while (not self.cola_vacia()):
                nodo=self.atencion()
                cAux.arribo(nodo.hora, nodo.app, nodo.mensaje)
            while (not cAux.cola_vacia()):
                nodo = cAux.atencion()
                app = nodo.app
                if app != red:
                    self.arribo(nodo.hora, nodo.app, nodo.mensaje)


        def imprimir_valores(self):
            cAux=Cola()
            while (not self.cola_vacia()):
              nodo=self.atencion()
              cAux.arribo(nodo.hora, nodo.app, nodo.mensaje)
            while (not cAux.cola_vacia()):
                nodo = cAux.atencion()
                print(nodo.hora, nodo.app, nodo.mensaje)
                self.arribo(nodo.hora, nodo.app, nodo.mensaje)

        def buscar(self, appbuscada, palabra):
            cAux=Cola()
            cAux2=Cola()
            busqueda=Cola()
            while (not self.cola_vacia()):
                nodo=self.atencion()
                cAux.arribo(nodo.hora, nodo.app, nodo.mensaje)
                cAux2.arribo(nodo.hora, nodo.app, nodo.mensaje)
            while (not cAux.cola_vacia()):
                nodo=cAux.atencion()
                app1=nodo.app
                mensaje=nodo.mensaje
                if (app1 == appbuscada and palabra in mensaje):
                    busqueda.arribo(nodo.hora, nodo.app, nodo.mensaje)
            while (not cAux2.cola_vacia()):
                nodo=cAux2.atencion()
                self.arribo(nodo.hora, nodo.app, nodo.mensaje)
            if (not busqueda.cola_vacia()):
                busqueda.imprimir_valores()
            else:
                print('No se han encontrado valores')

        def contar_por_hora(self, desde, hasta):
            cAux1=Cola()
            cAux2=Cola()
            pila=Pila()
            while (not self.cola_vacia()):
                nodo=self.atencion()
                cAux1.arribo(nodo.hora, nodo.app, nodo.mensaje)
                cAux2.arribo(nodo.hora, nodo.app, nodo.mensaje)
            while (not cAux1.cola_vacia()):
                nodo=cAux1.atencion()
                if (nodo.hora >= desde and nodo.hora <= hasta):
                    pila.apilar(nodo.hora, nodo.app, nodo.mensaje)
            sabertamanio=pila.que_tamanio()
            print(f'Las notificaciones desde {desde} hasta {hasta} fueron {sabertamanio}')



    class nodoPila(object) :
        """Clase nodo pila"""
        info, sig = None, None

    class Pila(object) :
        """Clase Pila"""
        def __init__(self) :
            self.cima = None
            self.tamanio = 0

        def apilar(self, hora, app, mensaje) :
            """Apila el elemento sobre la cima de la pila"""
            nodo = nodoPila()
            nodo.app = app
            nodo.hora = hora
            nodo.mensaje = mensaje
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
                return self.cima.hora, self.cima.app, self.cima.mensaje
            else :
                return None

        def que_tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio


    ##    Dada una cola con las notificaciones de las aplicaciones de redes sociales de un
    ##    Smartphone, de las cuales se cuenta con la hora de la notificación, la aplicación que la
    ##    emitió y el mensaje

    notificaciones=Cola()

    app=['facebook', 'twitter', 'tiktok', 'instagram']

    print(time(13,30))

    notificaciones.arribo(time(13,30), 'twitter', 'hagan un gol por favor')
    notificaciones.arribo(time(12,45), 'instagram', 'arabia en el segundo tiempo')
    notificaciones.arribo(time(15,10), 'twitter', '¿Quieres aprender ingles online?')
    notificaciones.arribo(time(11,30), 'tik tok', 'Te amo Messi')
    notificaciones.arribo(time(4,30), 'facebook', 'hola precio')
    notificaciones.arribo(time(4,30), 'twitter', 'dos besito porque tres mucha plata')

    ##    a) escribir una función que elimine de la cola todas las notificaciones de
    ##    Facebook

    print('\nValores antes de la función:')
    notificaciones.imprimir_valores()
    notificaciones.eliminar_red('facebook')
    print('\nValores después de la función:')
    notificaciones.imprimir_valores()


    ##    b) escribir una función que muestre todas las notificaciones de Twitter, cuyo
    ##    mensaje incluya la palabra 'Python', si perder datos en la cola;
    print('\nEscribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra Python, sin perder datos en la cola')
    notificaciones.buscar('twitter', 'Python')

    ##    c) utilizar una pila para almacenar temporáneamente las notificaciones
    ##    producidas entre las 11:43 y las 15:57, y determinar cuántas son.
    print('Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.')
    notificaciones.contar_por_hora(time(11,43), time(15,57))

if __name__ == '__main__':
    main()
