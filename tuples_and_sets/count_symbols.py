text = input()

sorted_text = sorted(list(set(text)))

for ch in sorted_text:
    print(f"{ch}: {text.count(ch)} time/s")