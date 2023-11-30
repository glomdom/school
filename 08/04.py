from collections import Counter

s = input("enter string> ")
letters = Counter(s)

for char in sorted(letters):
    print(f"{char}: {letters[char]} time/s")
