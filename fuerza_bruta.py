# fuerza_bruta.py

# === Fuerza Bruta ===
def max_const_var_brute_force(P):
    return max_const_var_brute_aux(P, 1, 1, 0, 0)

def max_const_var_brute_aux(P, i, curr_len, max_len, diff):
    if i >= len(P):
        return max(curr_len, max_len)
    elif i == 1:
        return max_const_var_brute_aux(P, i + 1, 2, max_len, P[1] - P[0])
    elif P[i] - P[i - 1] == diff:
        return max_const_var_brute_aux(P, i + 1, curr_len + 1, max_len, diff)
    else:
        return max_const_var_brute_aux(P, i + 1, 2, max(curr_len, max_len), P[i] - P[i - 1])

# Ejemplo
P = [15, 14, 16, 18, 17, 5]
print("Fuerza Bruta:", max_const_var_brute_force(P))


