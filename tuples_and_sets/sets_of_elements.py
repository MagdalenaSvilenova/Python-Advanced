lengths = input().split()
n = int(lengths[0])
m = int(lengths[1])

n_set = set()
m_set = set()

counter = 0

for _ in range(n+m):
    number = input()
    counter += 1
    if counter <= n:
        n_set.add(number)
    else:
        m_set.add(number)

unique_elements = n_set.intersection(m_set)
for el in unique_elements:
    print(el)