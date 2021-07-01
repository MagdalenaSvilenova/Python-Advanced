def odd_even_sum(nums):
    if command == 'Odd':
        return sum(filter(lambda x: x % 2 == 1, nums)) * len(nums)
    return sum(filter(lambda x: x % 2 == 0, nums)) * len(nums)


command = input()
numbers = list(map(int, input().split()))
print(odd_even_sum(numbers))