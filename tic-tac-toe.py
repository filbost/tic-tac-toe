def print_board(board):
    print("   1   2   3")
    print("  --- --- ---")
    for i, row in enumerate(board):
        print(f"{i + 1} | {' | '.join(row)} |")
        print("  --- --- ---")


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
    all(board[i][len(board) - i - 1] == board[0][len(board) - 1] and board[i][len(board) - i - 1] != ' ' for i in range(len(board))):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(len(board)) for j in range(len(board[0])))


def get_player_move():
    while True:
        try:
            move = int(input("Введите номер строки (1-3): ")) - 1, int(input("Введите номер столбца (1-3): ")) - 1
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                return move
            else:
                print("Некорректный ввод. Введите значения от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Введите целые числа.")


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        move = get_player_move()

        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} выиграл!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта клетка уже занята. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
