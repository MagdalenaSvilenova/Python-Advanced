n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

data = input()

while not data == 'END':
    command, row, col, value = data.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if 0 <= row < n and 0 <= col < n:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    data = input()

if data == 'END':
    [print(' '.join([str(x) for x in row])) for row in matrix]