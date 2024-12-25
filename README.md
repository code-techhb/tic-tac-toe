# Tic Tac Toe Game 🕹️

This is a console-based implementation of the classic two-player Tic Tac Toe game. This game allows two players to take 
turns in 
placing their marks (`X` and `T`) on a 3x3 grid, with the goal of getting three of their marks in a row, column, or diagonal. If neither player achieves this after 9 moves, the game ends in a draw.

---
## **How to Play ▶️**

1. **Game Setup**:
   - The game is initialized with an empty 3x3 grid, numbered from 1 to 9, representing the positions where players can place their marks.
   
2. **Making a Move**:
   - On each turn, players are prompted to choose a number (1-9) corresponding to an empty cell on the grid.
   - Player 1 uses the mark `X` and Player 2 uses the mark `T`.

3. **Winning**:
   - The game checks for a win after every move. A player wins if they place their marks in a horizontal, vertical, or diagonal line.
   
4. **Draw**:
   - If all cells are filled and no player wins, the game results in a draw.

5. **Rematch**:
   - After the game ends, players are prompted if they want to play again. Type `Y` for yes, or any other key to exit.

---

## **Game Flow Example 🧩**

```
Player 1, choose a cell (1-9): 1
X | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Player 2, choose a cell (1-9): 5
X | 2 | T
---------
4 | X | 6
---------
7 | 8 | 9

Player 1, choose a cell (1-9): 9
X | 2 | T
---------
4 | X | T
---------
7 | 8 | X

Congratulations! Player 1 wins!
```

---

## **Code Overview 👩🏽‍💻**
### Functions:
- **`display_grid(grid)`**: Displays the current state of the game grid.
- **`check_winner(grid)`**: Checks if there is a winner by evaluating the rows, columns, and diagonals.
- **`tic_tac_toe()`**: Contains Game logic.
  
The game continues until either a player wins or the game ends in a draw.

---

## **Customization 🎨**
- You can modify the **player marks** in the `players` list.
- If you prefer a different game logo or art, you can update the `logo` variable imported from the `art` module.


