# memoizado.py

# === Memoización ===
def max_const_var_memoized(P):
    M = [-float('inf')] * len(P)
    return max_const_var_memo_aux(P, 1, P[1] - P[0], 2, M, 2)

def max_const_var_memo_aux(P, curr, diff, length, M, max_so_far):
    if curr >= len(P):
        return max(length, max_so_far)
    if P[curr] - P[curr - 1] == diff:
        return max_const_var_memo_aux(P, curr + 1, diff, length + 1, M, max(max_so_far, length + 1))
    else:
        return max_const_var_memo_aux(P, curr + 1, P[curr] - P[curr - 1], 2, M, max(max_so_far, length))

# Ejemplo
P = [15, 14, 16, 18, 17, 5]
print("Memoizado:", max_const_var_memoized(P))
