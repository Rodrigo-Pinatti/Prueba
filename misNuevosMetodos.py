def crear_matriz(filas, columnas):
    import random
    matriz = []  # Crear una lista vacía para almacenar la matriz
    for i in range(filas):  # Iterar a través de las filas
        fila = []  # Crear una lista vacía para cada fila
        for j in range(columnas):  # Iterar a través de las columnas
           ## valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))  # Solicitar al usuario que ingrese el valor para la posición [i][j]
            numeroAlea= random.randint(0,100)
            fila.append(numeroAlea)  # Agregar el valor a la fila actual
        matriz.append(fila)  # Agregar la fila a la matriz
    return matriz  # Devolver la matriz creada
"""
matriz = crear_matriz(filas, columnas)

filas = int(input("Ingrese el número de filas de la matriz: "))  # Solicitar al usuario que ingrese el número de filas
columnas = int(input("Ingrese el número de columnas de la matriz: "))  # Solicitar al usuario que ingrese el número de columnas

matriz = crear_matriz(filas, columnas)  # Llamar a la función crear_matriz para generar la matriz
print("La matriz generada es:")
for fila in matriz:  # Iterar a través de cada fila en la matriz
    print(fila)  # Imprimir la fila en la salida
"""


import numpy as np

def generar_matriz_tridimensional(dim1, dim2, dim3):
    matriz_3d = np.random.rand(dim1, dim2, dim3)
    return matriz_3d
"""
# Ejemplo de uso
dimension_1 = 2
dimension_2 = 3
dimension_3 = 4

matriz_generada = generar_matriz_tridimensional(dimension_1, dimension_2, dimension_3)
print(matriz_generada)
"""
def sum_divisores(num):
    return sum([i for i in range(1, num) if num % i == 0])

def cargar_amigos_matriz(limit):
    numeros_amigos = []
    for i in range(1, limit):
        sum_i = sum_divisores(i)
        sum_sum_i = sum_divisores(sum_i)
        if i == sum_divisores(sum_i) and i != sum_i and i not in numeros_amigos:
            numeros_amigos.append([i, sum_i])
    
    matriz_amigos = np.array(numeros_amigos)
    return matriz_amigos





def esPrimo(numero):
    booleano=True
    for x in range(2,numero):
        if(numero%x==0):
            booleano=False
            ##print(numero," es divisible por ",x)
    if (booleano):
        print(numero," es primo ",booleano)
    return(booleano)


def arrayPrimo(tope):
    vectorPrimo=[1,2,3]
    for x in range(4,tope):
        if(esPrimo(x)):
            vectorPrimo.append(x)
    return(vectorPrimo)





def fiboo(cant_nro):
    a = 0
    b = 1
    c = a + b
    fibonacci_matrix = [[a], [b]]  # Matriz para almacenar los números de Fibonacci

    for _ in range(1, cant_nro):
        a = b
        b = c
        c = a + b
        fibonacci_matrix.append([c])  # Agregar el número a la matriz

    return fibonacci_matrix






def imprimirMatriz(matriz):
    for fila in matriz:  # Iterar a través de cada fila de la matriz
        for elemento in fila:  # Iterar a través de cada elemento de la fila
            print(elemento, end=" ")  # Imprimir el elemento seguido de un espacio
        print()  # Imprimir un salto de línea después de cada fila




def guardarMatriztxt(matriz):
    mi_path="contenidoMatriz.txt"
    with open(mi_path, 'a+') as archivo:
        for fila in matriz:
            linea = ' '.join(map(str, fila))  # Convertir los elementos de la fila en una cadena separada por espacios
            archivo.write(linea + '\n')  # Escribir la línea en el archivo y agregar un salto de línea




def cargarMatrizDetxt(mi_path):
    matriz = []
    with open(mi_path, 'r') as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split()))  # Convertir la línea en una lista de enteros
            matriz.append(fila)
    return matriz






def cargarMatrizRandom(matriz,filas,columnas):
    import random
    for x in range (filas):
        for y in range (columnas):
            matriz[x][y]=random.randint(0,1000)
            
    return (matriz)



def generarMatriz(filas, columnas):
    matriz = []
    for x in range(filas):
        fila = []
        for y in range(columnas):
            fila.append(0)  
        matriz.append(fila)
    return matriz

def valorFrecuente(matriz):
    contador = {}
    max_frecuencia = 0
    valorMasFrecuente = (0)

    # Recorrer la matriz y contar la frecuencia de cada valor
    for fila in matriz:
        for elemento in fila:
            if elemento in contador:
                contador[elemento] += 1
            else:
                contador[elemento] = 1

            # Actualizar el valor más frecuente si corresponde
            if contador[elemento] > max_frecuencia:
                max_frecuencia = contador[elemento]
                valorMasFrecuente = elemento

    return valorMasFrecuente


def son_amigos(numero1, numero2):
    suma_divisores_numero1 = sum(divisor for divisor in range(1, numero1) if numero1 % divisor == 0)
    suma_divisores_numero2 = sum(divisor for divisor in range(1, numero2) if numero2 % divisor == 0)

    if suma_divisores_numero1 == numero2 and suma_divisores_numero2 == numero1:
        return True
    else:
        return False


def buscarAmigos(matriz):
    numerosAmigos = []   
    for fila in matriz:
        for elemento in fila:
            for otro_elemento in fila:
                if elemento != otro_elemento and son_amigos(elemento, otro_elemento):
                    numerosAmigos.append((elemento, otro_elemento))

    return numerosAmigos


def matriz_int64(filas,columnas):
    matriz_aleatoria = np.random.randint(low=0, high=100, size=(filas, columnas), dtype=np.int64)

    return(matriz_aleatoria)









