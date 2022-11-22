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
    ## Ejercicio 12
    ## Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el
    ## siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:

    class nodoCola(object) :
        """Clase nodo cola"""
        nombre, prioridad, sig = None, None, None

    class Cola(object) :
        """Clase Cola"""
        def __init__(self) :
            """Crea una cola vacía"""
            self.frente, self.final = None, None
            self.tamanio = 0

        def arribo(self, nombre, prioridad) :
            """Arriba el elemento al final de la cola"""
            nodo = nodoCola()
            nodo.nombre = nombre
            nodo.prioridad = prioridad

            if self.frente is None :
                self.frente = nodo
            else :
                self.final.sig = nodo

            self.final = nodo
            self.tamanio += 1

        def arriboPrioritario(self, nombre, prioridad) :
            i = 0

            # Si el doc en_frente tiene mayor prioridad lo muevo al final
            while (not self.cola_vacia() and prioridad <= self.frente.prioridad) :
                self.mover_al_final()
                i += 1

            # Ingreso el documento
            self.arribo(nombre, prioridad)
            i += 1

            # Si me quedan documentos menos prioritarios para mover al final
            # los envío al final de la cola
            if (i != self.tamanio) :
                for j in range(i, self.tamanio) :
                    self.mover_al_final()
                    i += 1

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
                return self.frente.info

        def tamanio(self) :
            """Devuelve el nro de elementos en la cola"""
            return self.tamanio

        def mover_al_final(self) :
            """Mueve el elemento del frente al final de la cola"""
            nodo = self.atencion()
            self.arribo(nodo.nombre, nodo.prioridad)

            return nodo

        def imprimir(self, cantidad=False) :
            if (not cantidad) :
                cantidad = self.tamanio

            for i in range(0, cantidad) :
                doc = self.atencion()
                print(doc.nombre)

    prioridades = { 'Empleados': 1, 'Staff IT': 2, 'Gerente': 3 }
    impresora = Cola()

    ## a) cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
    impresora.arribo('DocEmp 1', prioridades['Empleados'])
    impresora.arribo('DocEmp 2', prioridades['Empleados'])
    impresora.arribo('DocEmp 3', prioridades['Empleados'])

    ## b) imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
    impresora.imprimir(1)

    ## c) cargue dos documentos del staff de TI.
    impresora.arriboPrioritario('DocIT 1', prioridades['Staff IT'])
    impresora.arriboPrioritario('DocIT 2', prioridades['Staff IT'])

    ## d) cargue un documento del gerente.
    impresora.arriboPrioritario('DocGerente 1', prioridades['Gerente'])

    ## e) imprima los dos primeros documentos de la cola.
    impresora.imprimir(2)

    ## f) cargue dos documentos de empleados y uno de gerente.
    impresora.arribo('DocEmp 4', prioridades['Empleados'])
    impresora.arribo('DocEmp 5', prioridades['Empleados'])
    impresora.arriboPrioritario('DocGerente 2', prioridades['Gerente'])

    ## g) imprima todos los documentos de la cola de impresión.
    impresora.imprimir()

if __name__ == '__main__':
    main()
