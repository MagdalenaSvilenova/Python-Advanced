rows, cols = [int(x) for x in input().split()]
matrix = []
max_sum = -9999999
best_submatrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for row in range(rows - 2):
    for col in range(cols - 2):
        submatrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row+3):
            submatrix.append([])
            for c in range(col, col+3):
                submatrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = submatrix

print(f"Sum = {max_sum}")
for row in best_submatrix:
    print(' '.join([str(x) for x in row]))



