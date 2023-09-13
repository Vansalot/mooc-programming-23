def row_correct(sudoku: list):
    for row in sudoku:
        checked_numbers = []
        for square in row: 
            if square == 0:
                continue
            elif square in checked_numbers:
                return False
            elif square not in checked_numbers:
                checked_numbers.append(square)
    return True

def column_correct(sudoku: list):
    for column_no in range(len(sudoku[0])):
        checked_numbers = []
        for row in sudoku:
            if row[column_no] == 0:
                continue
            elif row[column_no] in checked_numbers:
                return False
            elif row[column_no] not in checked_numbers:
                checked_numbers.append(row[column_no])
    return True

def block_correct(sudoku: list):
    blocklocations = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3] ,[6, 6]]

    for block in blocklocations:
        column_no = block[1]
        row_no = block[0]
        checked_numbers = []
        for row in range(row_no, row_no + 3):
            for column in range(column_no, column_no + 3):
                if sudoku[row][column] == 0:
                    pass
                elif sudoku[row][column] in checked_numbers:
                    return False
                elif sudoku[row][column] not in checked_numbers:
                    checked_numbers.append(sudoku[row][column])
    return True

def sudoku_grid_correct(sudoku: list):
        
    if not row_correct(sudoku) or not column_correct(sudoku) or not block_correct(sudoku):
        return False
    else:
        return True


if __name__=="__main__":   
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

