# todos_juntos.py

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


# === Main Execution ===
if __name__ == "__main__":
    P = [5, 7, 9, 11, 13, 8, 3]

    print("Fuerza Bruta:", max_const_var_brute_force(P))     # ✅ Output: 3
    print("Memoizado:", max_const_var_memoized(P))           # ✅ Output: 3
    print("Bottom-Up:", max_const_var_bottom_up(P))          # ✅ Output: 3
