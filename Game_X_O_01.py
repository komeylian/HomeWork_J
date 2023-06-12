def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')


def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ':
        return board[0][0]
    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != ' ':
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'

    while True:
        print_board(board)
        print("Player", current_player)
        move = input("Enter your move (1-9): ")

        if move.isdigit() and 1 <= int(move) <= 9:
            position = int(move) - 1
            row = position // 3
            col = position % 3

            if board[row][col] == ' ':
                board[row][col] = current_player

                winner = check_winner(board)
                if winner:
                    print("Player", winner, "wins!")
                    break
                elif is_board_full(board):
                    print("It's a tie!")
                    break

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move! Try again.")
        else:
            print("Invalid input! Enter a number between 1 and 9.")


play_game()
