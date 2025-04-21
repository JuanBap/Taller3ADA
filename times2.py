# times2.py
import time
import random
import csv
from exhaustivo import max_variacion_constante_rec
from memoizado import max_variacion_constante_memo
from bottom_up import max_variacion_constante_bottom_up

def medir_tiempo(algoritmo, P):
    inicio = time.time()
    resultado = algoritmo(P)
    fin = time.time()
    return resultado, fin - inicio

# Tamaños de entrada crecientes para pruebas
# Crear 100 casos de prueba desde 1 hasta 100, evenly spaced
tamaños = [i for i in range(1, 101)]  # 1, 2, 3, ..., 100

print(f"Midiendo tiempos de ejecución para {len(tamaños)} tamaños de entrada:")
print("Tamaño | Recursivo | Memoizado | Bottom-Up")
print("-" * 50)

# Preparar archivo CSV
with open('resultados_tiempos_small.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Tamaño', 'Recursivo', 'Memoizado', 'Bottom-Up'])
    
    for n in tamaños:
        # Generar una secuencia aleatoria de precios
        P = [random.randint(1, 100) for _ in range(n)]
        
        # Ejecutar todos los algoritmos para todos los tamaños
        resultado_rec, tiempo_rec = medir_tiempo(max_variacion_constante_rec, P)
            
        # Medir tiempos para los otros algoritmos
        resultado_memo, tiempo_memo = medir_tiempo(max_variacion_constante_memo, P)
        resultado_bu, tiempo_bu = medir_tiempo(max_variacion_constante_bottom_up, P)
        
        # Formatear y mostrar los resultados en consola
        print(f"{n:5d} | {tiempo_rec:.6f}s | {tiempo_memo:.6f}s | {tiempo_bu:.6f}s")
        
        # Guardar en CSV (sin el "s" del tiempo)
        csv_writer.writerow([n, tiempo_rec, tiempo_memo, tiempo_bu])

print(f"\nResultados guardados en 'resultados_tiempos_small.csv' para {len(tamaños)} tamaños diferentes") 