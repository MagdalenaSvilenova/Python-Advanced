n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for index in range(n):
    primary_diagonal_sum += matrix[index][index]
    secondary_diagonal_sum += matrix[index][n - index - 1]

diagonal_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(diagonal_difference)