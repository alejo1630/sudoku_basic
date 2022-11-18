# Sudoku (Basic Version)

This Python code solves easy-normal sudoku using brute force based on the general rules of this game

## 🔰 How does it work?

- The User has to input the initial state of the sudoku in a excel file such as the files inside sudoku_examples
- The code is designed to show the sudoku matrix in the console
- The code uses the basic rules of the sudoku game to solve it
  - Numbers 1-9 inside each 3x3 square
  - Numbers 1-9 in each row
  - Numbers 1-9 in each column
  - A number can be repeated in a square, row or column
 - The numbers (1-9) are sorted based on their frequency in the initial state
 - With the most frequent number the code starts to move for each empty cell and defines wether the number is located there using the above rules and taking into account there would not be any other possible number that could be insert in tha position
 - The above step repeats for all the numbers and all the empty cells until all the sudoku is solved
 - If the code is not be able to solve the initial sudoku after 100 iterations, the following message will be displayed on the console *"Solution needs backtracking"*
 - **Backtracking** is an advanced strategy where the solution code is able to get back if there is a dead end and try other guesses.
 - Additional information is showed in each iteration:
    - Number of steps/iterations
    - % Progress based on the initial number of empty cell
    - The input value (1-9)
    - The input coordinate 
 
 
## 🔶 What is next?
- Implement backtracking strategy for hard sudokus
- Creat an interface or app
