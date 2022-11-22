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
    ## Ejercicio 7 Se tiene una lista de los alumnos de un curso, de los que se sabe nombre,
    ## apellido y legajo. Por otro lado se tienen las notas de los diferentes parciales que
    ## rindió cada uno de ellos con la siguiente información: materia que rindió, nota
    ## obtenida y fecha de parcial. Desarrollar un algoritmo que permita realizar la
    ## siguientes actividades:

    # Importar fechas
    from datetime import date

    class Parcial(object) :
        """Clase Parcial"""
        materia, nota, fecha = None, None, None

        def __init__(self, materia, nota, fecha) :
            self.materia = materia
            self.nota = nota
            self.fecha = fecha

    class nodoLista(object) :
        """Clase nodo lista"""
        nombre, apellido, legajo, parciales, sig = None, None, None, [], None

    class Lista(object) :
        """Clase Lista enlazada simple"""
        def __init__(self) :
            """Crea una lista vacía"""
            self.inicio = None
            self.tamanio = 0

        def insertar(self, nombre, apellido, legajo, parciales) :
            """Inserta el dato a la lista"""
            nodo = nodoLista()
            nodo.nombre = nombre
            nodo.apellido = apellido
            nodo.legajo = legajo
            nodo.parciales = parciales

            if (self.inicio is None) or (self.inicio.apellido > apellido) :
                nodo.sig = self.inicio
                self.inicio = nodo
            else :
                ant = self.inicio # anterior
                act = self.inicio.sig # actual

                while (act is not None and act.apellido < apellido) :
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

        def tamanio(self) :
            """Devuelve el número de elementos en la lista"""
            return self.tamanio

        def contenido(self, solo_aprobados=False) :
            """Realiza un barrido de la lista mostrando los valores"""
            aux = self.inicio

            while (aux is not None) :
                if (solo_aprobados) :
                    aprobado = True

                    for parcial in aux.parciales :
                        if ( parcial.nota < 4 ) :
                            aprobado = False

                    if (aprobado) :
                        print(aux.apellido, aux.nombre)
                else :
                    print(aux.apellido, aux.nombre)

                aux = aux.sig

        def mostrar_promedios(self, minimo=0) :
            aux = self.inicio

            while (aux is not None) :
                cantidad = 0
                total = 0

                for parcial in aux.parciales :
                    total += parcial.nota
                    cantidad += 1

                promedio = total / cantidad

                if (promedio > minimo) :
                    print(aux.apellido, aux.nombre, 'promedio:', promedio)

                aux = aux.sig

        def buscar_apellido(self, apellido_a, inicial=False) :
            aux = self.inicio
            apellido_a = apellido_a.upper()

            while (aux is not None) :
                apellido_b = aux.apellido[0] if inicial else aux.apellido
                apellido_b = apellido_b.upper()

                if (apellido_a == apellido_b) :
                    print(aux.apellido, aux.nombre, aux.legajo)

                    for parcial in aux.parciales :
                        print(parcial.fecha, parcial.materia, parcial.nota)

                aux = aux.sig

        def buscar_materia(self, materia_a) :
            aux = self.inicio
            materia_a = materia_a.upper()

            while (aux is not None) :

                for parcial in aux.parciales :
                    materia_b = parcial.materia.upper()

                    if (materia_a == materia_b) :
                        print(aux.apellido, aux.nombre, aux.legajo)

                aux = aux.sig

        def porcentaje_aprobados(self, apellido_a) :
            aux = self.inicio
            apellido_a = apellido_a.upper()

            while (aux is not None) :
                apellido_b = aux.apellido.upper()

                if (apellido_a == apellido_b) :
                    aprobados = 0
                    total = 0

                    for parcial in aux.parciales :
                        total += 1
                        aprobados = aprobados + 1 if parcial.nota >= 4 else aprobados

                    porcentaje = aprobados * 100 / total
                    print(aux.apellido, aux.nombre, 'aprobó el', porcentaje, '% de los parciales')

                aux = aux.sig

        def buscar_anio(self, anio_a) :
            aux = self.inicio

            while (aux is not None) :

                for parcial in aux.parciales :
                    anio_b = parcial.fecha.year

                    if (anio_a == anio_b) :
                        print(aux.apellido, aux.nombre, aux.legajo)
                        print(parcial.fecha, parcial.materia, parcial.nota)

                aux = aux.sig

    lista = Lista()
    lista.insertar('Tomás', 'Langoni', 1, [Parcial("filosofia", 9, date(2020, 12, 3)), Parcial("sociologia", 10, date(2020, 11, 5)), Parcial("matematicas",8, date(2022, 9, 22))])
    lista.insertar('Cintia', 'Gil', 2, [Parcial("Teoría de la investigación", 4, date(2021, 10, 4)), Parcial("Base de Datos", 3, date(2022, 10, 5)), Parcial("Estructuras de Datos", 8, date(2020, 12, 3))])
    lista.insertar("Fernando", "Gil", 3,[Parcial("Álgebra lineal", 8, date(2021, 12, 3)), Parcial("Contabilidad", 8, date(2021, 12, 3)), Parcial("Práctica Profesional", 8, date(2022, 12, 3))])

    ## a). mostrar los alumnos ordenados alfabéticamente por apellido;
    print('Alumnos ordenados por apellido')
    lista.contenido()
    print('\n')

    ## b). indicar los alumnos que no desaprobaron ningún parcial
    print('Alumnos que no desaprobaron ningún parcial')
    lista.contenido(True)
    print('\n')

    ## c). determinar los alumnos que tienen promedio mayor a 8
    print('Mostrar promedios mayor 8')
    lista.mostrar_promedios(8)
    print('\n')

    ## d). mostrar toda la información de los alumnos cuyos apellidos comienzan con L
    print('Mostrar alumnos con apellido que empiece con L')
    lista.buscar_apellido('L', True)
    print('\n')

    ## e). mostrar el promedio de cada uno de los alumnos
    print('Mostrar todos los promedios')
    lista.mostrar_promedios()
    print('\n')

    ## f). mostrar todos los alumnos que rindieron la materia "Estructuras de datos";
    print('Mostrar todos los alumnos que rindieron Estructuras de datos')
    lista.buscar_materia('Estructuras de datos')
    print('\n')

    ## g). indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
    print('Porcentaje de parciales aprobados de un alumno')
    lista.porcentaje_aprobados('Gimenez')
    print('\n')

    ## h). indicar cuantos alumnos aprobaron y desaprobaron parciales de la materia "Base de datos";
    print('Mostrar todos los alumnos que aprobaron y desaprobaron Base de Datos')
    lista.buscar_materia('Base de Datos')
    print('\n')

    ## i). mostrar todos los alumnos que rindieron en el año 2020;
    print('Mostrar todos los alumnos que rindieron en el 2020')
    lista.buscar_anio(2020)
    print('\n')

if __name__ == '__main__':
    main()
