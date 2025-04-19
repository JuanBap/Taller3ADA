from fuerza_bruta import max_const_var_brute_force
from bottom_up import max_const_var_bottom_up
from memoizado import max_const_var_memoized

def main():
    P = [15, 14, 16, 18, 17, 5]
    
    print("Resultados para P =", P)
    print("Fuerza Bruta:", max_const_var_brute_force(P))
    print("Bottom-Up:", max_const_var_bottom_up(P))
    print("Memoizado:", max_const_var_memoized(P))

if __name__ == "__main__":
    main()
