"""Two-player Tic-Tac-Toe in the terminal."""
WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]

def show_board(board):
    for row in range(0, 9, 3):
        print(" | ".join(board[row:row+3]))
        if row < 6: print("---------")

def winner(board, symbol):
    return any(all(board[index] == symbol for index in line) for line in WIN_LINES)

def main():
    board = [str(i) for i in range(1, 10)]
    for turn in range(9):
        player = "X" if turn % 2 == 0 else "O"
        show_board(board)
        while True:
            try:
                position = int(input(f"Player {player}, choose 1-9: ")) - 1
            except ValueError:
                print("Enter a number from 1 to 9")
                continue
            if 0 <= position < 9 and board[position] not in ("X", "O"):
                break
            print("Invalid or occupied position")
        board[position] = player
        if winner(board, player):
            show_board(board)
            print(f"Player {player} wins!")
            return
    show_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
