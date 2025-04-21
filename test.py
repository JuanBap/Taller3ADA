# test.py
from exhaustivo import max_variacion_constante_rec
from memoizado import max_variacion_constante_memo
from bottom_up import max_variacion_constante_bottom_up

print("--- Otros Casos de Prueba ---")
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
