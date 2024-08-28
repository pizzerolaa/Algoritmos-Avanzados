board = [['' for _ in range(3)] for _ in range(3)]  # tablero

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

def winCheck(board, player):
    # Verificamos filas, columnas y diagonales
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    
    return False

def drawCheck(board):
    return all(all(cell for cell in row) for row in board)

def minimax(board, depth, is_maximizing, alpha, beta):
    if winCheck(board, 'X'):
        return 1
    elif winCheck(board, 'O'):
        return -1
    elif drawCheck(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval
    
def bestMovement(board):
    best_value = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'
                move_value = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ''
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

def play():
    board = [['' for _ in range(3)] for _ in range(3)]
    currentPlayer = 'O'

    while True:
        printBoard(board)

        if currentPlayer == 'O':
            row, column = playerMovement(board)
            board[row][column] = 'O'
            if winCheck(board, 'O'):
                printBoard(board)
                print("¡Felicidades! Ganaste")
                break
        else:
            print("Turno de la IA")
            row, column = bestMovement(board)
            board[row][column] = 'X'
            if winCheck(board, 'X'):
                printBoard(board)
                print("La IA ha ganado")
                break
        
        if drawCheck(board):
            printBoard(board)
            print("Es un empate.")
            break

        currentPlayer = 'X' if currentPlayer == 'O' else 'O'

if __name__ == "__main__":
    play()