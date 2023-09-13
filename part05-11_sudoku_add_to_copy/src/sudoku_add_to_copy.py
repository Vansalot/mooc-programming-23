def print_sudoku(sudoku: list):
    rowcounter = 0
    for row in sudoku:
        boxspace = 0
        if rowcounter == 3:
            print()
            rowcounter = 0
        rowcounter += 1
        for square in row:
            if boxspace == 3:
                print(" ", end="")
                boxspace = 0
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            boxspace += 1
            
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for row in sudoku:
        sudoku_copy.append(row[:])
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__=='__main__':
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)