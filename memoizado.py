# memoizado.py

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
