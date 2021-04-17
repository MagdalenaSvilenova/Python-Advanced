numbers = input().split()

result = []

while numbers:
    next_number = numbers.pop()
    result.append(next_number)

print(' '.join(result))