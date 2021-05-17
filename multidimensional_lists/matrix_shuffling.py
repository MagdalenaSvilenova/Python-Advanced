rows, cols = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    matrix.append(input().split())


def print_matrix(matrix):
    for row in matrix:
        row_str = [str(x) for x in row]
        print(' '.join(row_str))


inp = input()
while inp != "END":
    swap, *args = inp.split()
    if swap == 'swap' and len(args) == 4:
        row1, col1, row2, col2 = [int(x) for x in args]
    if swap != 'swap' or row1 >= rows or row2 >= rows or col1 >= cols or col2 >= cols or \
            any(int(i) < 0 for i in args):
        print("Invalid input!")
    else:
        tmp = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = tmp
        print_matrix(matrix)

    inp = input()