# Tic Tac Toe Game | Houlaymatou B. | @code_techhb
from art import logo


# --------------------- functions -------------------------------
def display_grid(grid):
    rows = []
    for row in grid:
        rows.append("  |  ".join(row))
    print("\n--------------\n".join(rows))


def check_winner(grid):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combi in winning_combinations:
        marks = [grid[row][col] for row, col in combi]
        if marks[0] == marks[1] == marks[2] and marks[0] != " ":
            return marks[0]
    return None


def tic_tac_toe():
    grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    players = [("Player 1", "X"), ("Player 2", "T")]
    display_grid(grid)

    for turn in range(9):
        player, mark = players[turn % 2]

        while True:
            choice = input(f"{player}, choose a cell (1-9): ")
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    row, col = divmod(choice - 1, 3)
                    if grid[row][col] not in "XT":
                        grid[row][col] = mark
                        break
                    else:
                        print("🥲Cell is already taken. Try again.")
                else:
                    print("🚨Invalid choice. Please select a number between 1 and 9.")
            except ValueError:
                print("❌Invalid input! Please enter a number between 1 and 9.")

        display_grid(grid)
        winner = check_winner(grid)
        if winner:
            print(f"\n🥳Congratulations! {player} wins!")
            return

    print("☹️It's a draw!")


# -------------------- main -------------------------------
should_continue = True
while should_continue:
    print(logo)
    tic_tac_toe()
    go_again = input("\nWould you like to play again? Type Y for yes or any other key to exit: ").lower()
    if go_again != "y":
        should_continue = False
        print("\nSee you next time 🤓!\n")
