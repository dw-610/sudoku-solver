# Python Sudoku Solver

Objective: write a program that takes in any unsolved Sudoku board and returns
the solution.

Going to try and do this without any imports.

## Design

### Data Structures

Will use a `dict` object to handle the board.

```
board[(i,j)] = n
```

Where `i,j` is a tuple denoting the position and `n` is the value at that position.

### Algorithm

- Select row/columns with the largest number of known elements.
- For each unknown element in the row/column, get the possible values.
- If any element has only one possible value, assign it, clear memory and repeat.

*Note*: this is not the most efficient way to do it; would be better to update known possible values instead of clearing.

*Note*: this will not always work; on harder boards, will need to make decisions and try out paths to determine what value is correct.
