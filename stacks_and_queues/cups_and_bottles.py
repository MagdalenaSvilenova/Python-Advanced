from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = list(map(int, input().split()))
wasted_liters = 0

while cups_capacity and filled_bottles:
    bottle = filled_bottles.pop()
    cups_capacity[0] -= bottle

    if cups_capacity[0] <= 0:
        wasted_liters -= cups_capacity.popleft()

if not cups_capacity:
    print("Bottles: ", end="")
    while filled_bottles:
        print(filled_bottles.pop(), end=" ")
else:
    print("Cups: ", end="")
    while cups_capacity:
        print(cups_capacity.popleft(), end=" ")

print(f"\nWasted litters of water: {wasted_liters}")