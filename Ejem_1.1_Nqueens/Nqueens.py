def n_queens_solve(n):
    #iniciamos el tablero
    tablero = [[0 for _ in range(n)] for _ in range(n)]

    #llamamos la funcion backtracking
    if backtracking(tablero, 0, n):
        imp_solucion(tablero)
    else:
        print("No hay solución")

#creamos la funcion backtracking
def backtracking(tablero, col, n):
    pass

def is_save(tablero, fila, col, n):
    
    pass

def imp_solucion(tablero):
    pass

n = 8
n_queens_solve(n)


