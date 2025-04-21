# bottom_up.py

def max_variacion_constante_bottom_up(P):
    """
    Encuentra el máximo número de periodos contiguos durante los cuales
    la acción incrementó o decrementó exactamente en el mismo valor.
    Versión Iterativa (Bottom-Up) con Tabulación.
    """
    m = len(P)
    if m < 2:
        return m

    # Crear la memoria. Tamaño m+1 para manejar fácilmente el caso base M[m]
    # Inicializar con -inf.
    M = [float('-inf')] * (m + 1)

    # Establecer casos base explícitamente en M
    # M[m] ya es -inf (representa longitud para subproblema vacío)
    M[m] = 0  # Establecer caso base explícitamente
    if m > 0:
        M[m-1] = 1 # La máxima longitud en el último elemento es 1

    # Llenar la tabla M desde el final hacia el principio
    # k va desde m-2 hasta 0
    for k in range(m - 2, -1, -1):
        # Calcular la longitud de la racha que comienza en k
        # Siempre hay al menos P[k] y P[k+1] porque k <= m-2
        longitud_actual = 2 # Al menos P[k] y P[k+1]
        diferencia = P[k+1] - P[k]
        for j in range(k + 2, m):
            if P[j] - P[j-1] == diferencia:
                longitud_actual += 1
            else:
                break

        # La solución en k depende de la racha que empieza en k
        # y la solución ya calculada para k+1 (almacenada en M[k+1])
        # M[k+1] contiene la máxima longitud encontrada a partir del índice k+1
        M[k] = max(longitud_actual, M[k+1])

    # El resultado final está en M[0], que considera todo el arreglo P[0:]
    return M[0]
