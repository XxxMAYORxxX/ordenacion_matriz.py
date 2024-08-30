def bubble_sort(fila):
    """
    Ordena una lista usando el algoritmo de Bubble Sort.

    :param fila: Lista de valores a ordenar.
    :return: Lista ordenada.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


def mostrar_matriz(matriz):
    """
    Muestra una matriz en formato legible.

    :param matriz: Lista de listas (matriz) a mostrar.
    """
    for fila in matriz:
        print(fila)


def ordenar_fila_matriz(matriz, fila_index):
    """
    Ordena una fila específica de la matriz usando Bubble Sort.

    :param matriz: Lista de listas (matriz) que contiene las filas.
    :param fila_index: Índice de la fila a ordenar.
    """
    if fila_index < 0 or fila_index >= len(matriz):
        print("Índice de fila fuera de rango.")
        return

    # Ordenar la fila especificada
    matriz[fila_index] = bubble_sort(matriz[fila_index])


def main():
    # Definición de la matriz bidimensional 3x3
    matriz = [
        [9, 2, 7],
        [3, 5, 1],
        [8, 4, 6]
    ]

    # Mostrar la matriz original
    print("Matriz Original:")
    mostrar_matriz(matriz)

    # Índice de la fila que se va a ordenar
    fila_a_ordenar = 1

    # Ordenar la fila especificada
    ordenar_fila_matriz(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
    mostrar_matriz(matriz)


if __name__ == "__main__":
    main()
