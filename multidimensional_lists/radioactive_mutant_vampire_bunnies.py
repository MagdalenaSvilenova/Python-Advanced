rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

commands = input()