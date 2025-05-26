def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontais
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticais
        (0, 4, 8), (2, 4, 6)               # diagonais
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    
    return None

def is_board_full(board):
    return ' ' not in board

def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == 'X':
            choice = int(input("Jogador X, escolha um espaço (1-9): ")) - 1
        else:
            choice = int(input("Jogador O, escolha um espaço (1-9): ")) - 1

        if board[choice] == ' ':
            board[choice] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Jogador {winner} venceu!")
                break
            if is_board_full(board):
                print_board(board)
                print("Empate!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Espaço já ocupado, tente novamente.")

if __name__ == "__main__":
    play_game()
