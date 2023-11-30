def calc(names):
    even_set = set()
    odd_set = set()

    for index, name in enumerate(names, start=1):
        name_score = sum(ord(char) for char in name) // index

        if name_score % 2 == 0:
            even_set.add(name_score)
        else:
            odd_set.add(name_score)

    even_sum = sum(even_set)
    odd_sum = sum(odd_set)

    if even_sum > odd_sum:
        result = "-".join(map(str, even_set.symmetric_difference(odd_set)))
    elif odd_sum > even_sum:
        result = "-".join(map(str, odd_set.difference(even_set)))
    else:
        result = "-".join(map(str, even_set.union(odd_set)))

    return result

n = int(input("enter amount of names> "))
names = []

for _ in range(n):
    names.append(input("enter name> "))

print(calc(names))
