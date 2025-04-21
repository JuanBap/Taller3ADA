# main.py

# --- 1. Solución Exhaustiva (Recursiva - Estilo LIS) ---

def max_variacion_constante_aux_rec(P, k):
    """
    Función auxiliar recursiva para calcular la máxima longitud
    de variación constante comenzando desde el índice k o después.
    """
    m = len(P)

    # Casos Base de la recursión
    if k >= m:
        return 0  # Fuera de los límites
    if k == m - 1:
        return 1  # Último elemento, longitud 1

    # Calcular la longitud de la racha con diferencia constante que comienza en k
    longitud_actual = 1
    if k + 1 < m:  # Se necesita al menos 2 elementos para tener una diferencia
        longitud_actual = 2
        diferencia = P[k+1] - P[k]
        # Iterar para extender la racha actual
        for j in range(k + 2, m):
            if P[j] - P[j-1] == diferencia:
                longitud_actual += 1
            else:
                break # La diferencia cambió, termina la racha
    else:
        # Si k es el penúltimo elemento, longitud_actual ya es 1 (solo ese elemento)
        # Si k es el último elemento, el caso base k == m - 1 lo maneja
        # Si k+1 no es menor que m, significa que solo hay un elemento (P[k])
        # o estamos fuera de los límites (ya manejado).
        # Si k == m-1, longitud_actual debe ser 1.
        longitud_actual = 1


    # Explorar la solución sin comenzar necesariamente en k (mirando desde k+1)
    longitud_resto = max_variacion_constante_aux_rec(P, k + 1)

    # La máxima longitud es la mayor entre la racha que empieza en k
    # y la máxima encontrada después de k
    return max(longitud_actual, longitud_resto)

def max_variacion_constante_rec(P):
    """
    Encuentra el máximo número de periodos contiguos durante los cuales
    la acción incrementó o decrementó exactamente en el mismo valor.
    Versión Recursiva Exhaustiva.
    """
    m = len(P)
    if m < 2:
        return m # Si hay 0 o 1 elemento, la longitud es m

    # Llama a la función auxiliar comenzando desde el índice 0
    return max_variacion_constante_aux_rec(P, 0)

# --- 2. Solución Memoizada (Top-Down con Memoria) ---

def max_variacion_constante_aux_memo(P, k, M):
    """
    Función auxiliar memoizada para calcular la máxima longitud
    de variación constante comenzando desde el índice k o después,
    usando la memoria M.
    """
    m = len(P)

    # Si el valor ya está calculado, retornarlo
    # Ahora verificamos si es diferente de -float('inf') en lugar de None
    if k < m and M[k] != float('-inf'):
        return M[k]

    # Casos Base (igual que en la recursiva)
    if k >= m:
        return 0
    if k == m - 1:
        # Almacenar antes de retornar para el caso base
        if k < m: M[k] = 1
        return 1

    # Calcular la longitud de la racha que comienza en k (igual que antes)
    longitud_actual = 1
    if k + 1 < m:
        longitud_actual = 2
        diferencia = P[k+1] - P[k]
        for j in range(k + 2, m):
            if P[j] - P[j-1] == diferencia:
                longitud_actual += 1
            else:
                break
    else:
         longitud_actual = 1 # Si solo queda el elemento k

    # Calcular recursivamente la solución para el resto (usando memoria)
    longitud_resto = max_variacion_constante_aux_memo(P, k + 1, M)

    # Determinar el resultado para el estado actual 'k'
    resultado = max(longitud_actual, longitud_resto)

    # Almacenar el resultado en la memoria antes de retornar
    # Solo almacenar si k es un índice válido de M
    if k < m:
        M[k] = resultado

    return resultado

def max_variacion_constante_memo(P):
    """
    Encuentra el máximo número de periodos contiguos durante los cuales
    la acción incrementó o decrementó exactamente en el mismo valor.
    Versión Memoizada (Top-Down).
    """
    m = len(P)
    if m < 2:
        return m

    # Crear e inicializar la memoria con -infinito para indicar "no calculado"
    M = [float('-inf')] * m 

    # Llama a la función auxiliar con la memoria
    return max_variacion_constante_aux_memo(P, 0, M)

# --- 3. Solución Bottom-Up (Iterativa con Tabulación) ---

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
    # Inicializar con 0.
    M = [0] * (m + 1)

    # Establecer casos base explícitamente en M
    # M[m] ya es 0 (representa longitud para subproblema vacío)
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

# --- Ejemplo de Uso ---
P = [15, 14, 16, 18, 17, 5] # El ejemplo dado
# La subsecuencia es [14, 16, 18] (índices 1, 2, 3), longitud 3, diferencia +2

print(f"Secuencia de precios: {P}")

# Prueba Recursiva
print(f"Solución Recursiva: {max_variacion_constante_rec(P)}")

# Prueba Memoizada
print(f"Solución Memoizada: {max_variacion_constante_memo(P)}")

# Prueba Bottom-Up
print(f"Solución Bottom-Up: {max_variacion_constante_bottom_up(P)}")

# --- Otros Casos de Prueba ---
print("\n--- Otros Casos de Prueba ---")
P_test1 = []
print(f"P={P_test1}: Rec={max_variacion_constante_rec(P_test1)}, Memo={max_variacion_constante_memo(P_test1)}, BU={max_variacion_constante_bottom_up(P_test1)}") # Esperado: 0

P_test2 = [10]
print(f"P={P_test2}: Rec={max_variacion_constante_rec(P_test2)}, Memo={max_variacion_constante_memo(P_test2)}, BU={max_variacion_constante_bottom_up(P_test2)}") # Esperado: 1

P_test3 = [10, 12]
print(f"P={P_test3}: Rec={max_variacion_constante_rec(P_test3)}, Memo={max_variacion_constante_memo(P_test3)}, BU={max_variacion_constante_bottom_up(P_test3)}") # Esperado: 2

P_test4 = [5, 5, 5, 5, 5]
print(f"P={P_test4}: Rec={max_variacion_constante_rec(P_test4)}, Memo={max_variacion_constante_memo(P_test4)}, BU={max_variacion_constante_bottom_up(P_test4)}") # Esperado: 5 (diferencia 0)

P_test5 = [10, 9, 8, 7, 6, 5]
print(f"P={P_test5}: Rec={max_variacion_constante_rec(P_test5)}, Memo={max_variacion_constante_memo(P_test5)}, BU={max_variacion_constante_bottom_up(P_test5)}") # Esperado: 6 (diferencia -1)

P_test6 = [1, 2, 4, 5, 6, 8, 10]
# Rachas: [1, 2] (len 2, diff 1), [2, 4] (len 2, diff 2), [4, 5, 6] (len 3, diff 1), [8, 10] (len 2, diff 2)
print(f"P={P_test6}: Rec={max_variacion_constante_rec(P_test6)}, Memo={max_variacion_constante_memo(P_test6)}, BU={max_variacion_constante_bottom_up(P_test6)}") # Esperado: 3

P_test7 = [3, 6, 9, 10, 13, 16, 19, 18]
# Rachas: [3, 6, 9] (len 3, diff 3), [10, 13, 16, 19] (len 4, diff 3)
print(f"P={P_test7}: Rec={max_variacion_constante_rec(P_test7)}, Memo={max_variacion_constante_memo(P_test7)}, BU={max_variacion_constante_bottom_up(P_test7)}") # Esperado: 4