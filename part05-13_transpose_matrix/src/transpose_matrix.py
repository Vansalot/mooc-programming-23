def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])

    for row in range(len(matrix_copy)):
        for column in range(len(matrix_copy[0])):
            matrix[column][row] = matrix_copy[row][column]
    
    return matrix

if __name__=='__main__':
    numberlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(numberlist))