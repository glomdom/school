inp = input("enter nums> ").strip().split()
inp = map(float, inp)
inp = tuple(inp)
non_repeating = set(inp)

for num in non_repeating:
    count = inp.count(num)

    print(f"{num:.1f} - {count} times")
