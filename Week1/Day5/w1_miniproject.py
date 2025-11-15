def clear_screen():
    print("\n" * 50)
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("TIC TAC TOE")
    print('*' * 15)
    for r in range(3):
        row_cells = []
        for c in range(3):
            row_cells.append(f' {board[r][c]} ')
        print('* ' + '|'.join(row_cells) + ' *')
        if r < 2:
         print('* ' + '---+---+---' + ' *')
    print('*' * 15)
#print_board(board=())
#plateau de jeu fait 
def is_winner(board, symbol):
    for r in range(3):
        if all(board[r][c] == symbol for c in range(3)):
            return True
    for c in range(3):
        if all(board[r][c] == symbol for r in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False
def board_full(board):
    return all(board[r][c] != ' ' for r in range(3) for c in range(3)) 
#verifie si la grille est pleine ok
def get_move(player, board):
    while True:
        try:
            row = input(f"Player {player}'s turn. Enter row (1-3): ").strip()
            col = input(f"Enter column (1-3): ").strip()
            r = int(row) - 1
            c = int(col) - 1
            if r not in (0,1,2) or c not in (0,1,2):
                print("Invalid data - data between 1 and 3.")
                continue
            if board[r][c] != ' ':
                print("position already taken - choose another.")
                continue
            return r, c
        except ValueError:
            print("Invalid data - data between 1 and 3.")
            continue
#regles du jeu definies
def play_game():
    board = create_board()
    current = 'X' 
    clear_screen()
    print("Welcome to TIC TAC TOE!\n")
    while True:
        print_board(board)
        r, c = get_move(current, board)
        board[r][c] = current
        clear_screen()
        print_board(board)
        if is_winner(board, current):
            print(f"\nPlayer {current} wins!")
            break
        if board_full(board):
            print("\nDraw!")
            break
        current = 'O' if current == 'X' else 'X'
    while True:
        replay = input("\nReplay ? (y/n) : ").strip().lower()
        if replay in ('y'):
            clear_screen()
            return True
        if replay in ('n'):
            print("Thanks, Bye !")
            return False
        print("Answer not understood — tape 'y' for YES o 'n' for NO.") 

def main(): 
    while True:
        if not play_game():
            break
if __name__ == "__main__":
    main()
