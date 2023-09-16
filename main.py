import game_logic as ttt

def load_scores(filename="scores.txt"):
    try:
        with open(filename, "r") as file:
            scores = file.readline().strip().split(",")
            if len(scores) != 2:
                return {"X": 0, "O": 0}
            return {"X": int(scores[0]), "O": int(scores[1])}
    except FileNotFoundError:
        return {"X": 0, "O": 0}

def save_scores(scores, filename="scores.txt"):
    with open(filename, "w") as file:
        file.write(f"{scores['X']},{scores['O']}")

def main():
    scores = load_scores()

    while True:
        board = ttt.create_board()
        current_player = "X"

        print(f"Player X: {scores['X']}  Player O: {scores['O']}")
        print("Welcome to Tic Tac Toe!")

        while True:
            ttt.print_board(board)

            row, col = -1, -1
            while True:
                try:
                    row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
                    col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if ttt.make_move(board, row, col, current_player):
                    break
                else:
                    print("Invalid move. Try again.")

            if ttt.check_winner(board, current_player):
                ttt.print_board(board)
                print(f"Player {current_player} wins! Congratulations!")
                scores[current_player] += 1
                save_scores(scores)
                break

            if ttt.is_board_full(board):
                ttt.print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
