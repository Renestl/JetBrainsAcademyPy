def init_matrix(rows):
    matrix = []

    for row in range(rows):
        temp = list(map(int, input().split(' ')))
        matrix.append(temp)

    return matrix


a_rows, a_cols = input().split()
matrix_a = init_matrix(int(a_rows))

b_rows, b_cols = input().split()
matrix_b = init_matrix(int(b_rows))

if a_rows == b_rows and a_cols == b_cols:
    result = [[matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[0]))] for row in range(len(matrix_a))]
    [print(' '.join(map(str, result[row]))) for row in range(len(result))]
else:
    print('ERROR')
