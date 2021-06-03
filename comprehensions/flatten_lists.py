line = input().split('|')[::-1]
result = [value.strip() for i in range(len(line)) for value in line[i].split()]
print(*result)