def print_min_max_sum(nums):
    min_number = min(nums)
    max_number = max(nums)
    sum_numbers = sum(nums)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is {sum_numbers}")


nums = list(map(int, input().split()))
print_min_max_sum(nums)