def even_numbers(iters):
    return list(filter(lambda x: x % 2 == 0, iters))


numbers = map(int, input().split())
print(even_numbers(numbers))