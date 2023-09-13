def transpose(matrix: list):
    new_matrix = []
    for row in matrix:
        new_matrix.append([])

    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            new_matrix[row].append(matrix[column][row])

    print(new_matrix)


if __name__=='__main__':
    numberlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(numberlist)