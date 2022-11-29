##        Ejercicio 1
##        Para probar los distintos algoritmos de ordenamiento vistos (Burbuja, Selección,
##        Inserción, Rápido y Mezcla):
##        a) Generar una lista de elementos aleatorios de distintos tamaños (100.000,
##        1.000.000, 10.000.000)
##        b) Medir y mostrar su tiempo de ejecución
##        c) Medir y mostrar la cantidad de comparaciones realizadas
##        d) Deberá indicar nombre y tiempo del método más rápido
##        e) Deberá indicar nombre y cantidad del método que realiza menos comparaciones


cien =[]
mil =[]
diezmil =[]

import random
import time

for i in range(100):
    aux=random.randint(0,1000)
    cien.append(aux)


for i in range(1000):
    aux=random.randint(0,1000)
    mil.append(aux)

for i in range(10000):
    aux=random.randint(0,10000)
    diezmil.append(aux)


def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]


def seleccion(lista) :
    """Método de ordenamiento selección"""
    for i in range(0, len(lista)-1) :
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j] < lista[minimo]) :
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]


def insercion(lista) :
    """Método de ordenamiento inserción"""
    for i in range(1, len(lista)+1) :
        k = i-1
        while (k > 0) and (lista[k] < lista[k-1]) :
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1


def quicksort(lista, primero, ultimo) :
    """Metodo de ordenamiento quicksort"""
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo

    while (izquierda < derecha) :
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
            izquierda += 1

        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
            derecha -= 1

        if (izquierda < derecha) :
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    if (lista[pivote] < lista[izquierda]) :
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    if (primero < izquierda) :
        quicksort(lista, primero, izquierda-1)

    if (ultimo > izquierda) :
        quicksort(lista, izquierda+1, ultimo)

def mergesort(lista) :
    """Metodo de ordenamiento mergesort"""
    if (len(lista) <= 1) :
        return lista
    else :
        medio = len(lista) // 2
        izquierda = []

        for i in range(0, medio) :
            izquierda.append(lista[i])

        derecha = []

        for i in range(medio, len(lista)) :
            derecha.append(lista[i])

        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)

        if (izquierda[medio-1] <= derecha[0]) :
            izquierda += derecha

            return izquierda

        resultado = merge(izquierda, derecha)

        return resultado

def contarTiempo(funcion, lista):
    tiempoinicial=time.time()
    funcion(lista)
    tiempofinal=time.time()
    diferencia=tiempofinal-tiempoinicial
    return diferencia

def crearTotales(funcion):
    tiempofuncion={}
    tiempo=contarTiempo(funcion, cien)
    tiempofuncion['cien']=tiempo
    tiempo=contarTiempo(funcion, mil)
    tiempofuncion['mil']=tiempo
    tiempo=contarTiempo(funcion, diezmil)
    tiempofuncion['diezmil']=tiempo
    return tiempofuncion

totales={}
totales['Burbuja']=crearTotales(burbuja)
totales['Seleccion']=crearTotales(seleccion)
totales['Insercion']=crearTotales(insercion)
totales['Mezcla']=crearTotales(mergesort)
print(totales)