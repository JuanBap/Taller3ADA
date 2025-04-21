# exhaustivo.py

def max_variacion_constante_rec(P):
    """
    Encuentra el máximo número de periodos contiguos durante los cuales
    la acción incrementó o decrementó exactamente en el mismo valor.
    Versión Recursiva de Fuerza Bruta.
    """
    if len(P) < 2:
        return len(P)  # Si hay 0 o 1 elemento, la longitud es len(P)
    return max_variacion_constante_aux_rec(P, 1, 1, 0, 0)

def max_variacion_constante_aux_rec(P, i, curr_len, max_len, diff):
    if i >= len(P):
        return max(curr_len, max_len)
    elif i == 1:
        return max_variacion_constante_aux_rec(P, i + 1, 2, max_len, P[1] - P[0])
    elif P[i] - P[i - 1] == diff:
        return max_variacion_constante_aux_rec(P, i + 1, curr_len + 1, max_len, diff)
    else:
        return max_variacion_constante_aux_rec(P, i + 1, 2, max(curr_len, max_len), P[i] - P[i - 1])
