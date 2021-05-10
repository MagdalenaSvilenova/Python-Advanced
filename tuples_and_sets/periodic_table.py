n = int(input())
unique_elements = set()

for _ in range(n):
    chemical_compound = input().split()
    for i in chemical_compound:
        unique_elements.add(i)

for el in unique_elements:
    print(el)