# main.py
from exhaustivo import max_variacion_constante_rec
from memoizado import max_variacion_constante_memo
from bottom_up import max_variacion_constante_bottom_up

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