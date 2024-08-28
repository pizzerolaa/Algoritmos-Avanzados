board = [['' for _ in range(3)] for _ in range(3)] #tablero

def printBoard(board):
    for row in board:
        print("|".join(cell or " " for cell in row))
        print("-" * 5)

def playerMovement(board):
    while True:
        try:
            row = int(input("Ingrese el número de la fila (0, 1, 2): "))
            column = int(input("Ingrese el número de la columna (0, 1, 2): "))

            if board[row][column] == '':
                return row, column
            else:
                print("La celda ya está ocupada, intente de nuevo.")
        except (ValueError, IndexError):
            print("Entrada no válida. Asegurese que el número ingresado sea entre 0 y 2")

def play():
    board = [['' for _ in range(3)] for _ in range(3)]
    playerMovement(board)
    printBoard(board)

play()
