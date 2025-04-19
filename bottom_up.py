#bottom_up.py

# === Bottom-Up ===
def max_const_var_bottom_up(P):
    n = len(P)
    if n < 2:
        return n
    max_len = 1

    for i in range(1, n):
        diff = P[i] - P[i - 1]
        length = 2
        for j in range(i + 1, n):
            if P[j] - P[j - 1] == diff:
                length += 1
                max_len = max(max_len, length)
            else:
                break
    return max_len

# Ejemplo
P = [15, 14, 16, 18, 17, 5]
print("Bottom-Up:", max_const_var_bottom_up(P))
