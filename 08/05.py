max_set = set()
max_len = 0
n = int(input())

for i in range(n):
    a, b = input().split("-")
    a, b = list(map(int, a.split(","))), list(map(int, b.split(",")))

    range1_start, range1_end = a[0], a[1]
    range2_start, range2_end = b[0], b[1]

    set1 = set(int(x) for x in range(range1_start, range1_end+1))
    set2 = set(int(x) for x in range(range2_start, range2_end+1))
    intersection = set2.intersection(set1)

    if len(intersection) >= max_len:
        max_len = len(intersection)
        max_set = intersection

print(f"Longest intersection is {list(max_set)} with length {max_len}")
