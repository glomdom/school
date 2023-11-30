first_len, second_len = list(map(int, input("enter length of 2 sets> ").split()))

set1 = set()
set2 = set()

for _ in range(first_len):
    set1.add(input("enter number for 1st set> "))

for _ in range(second_len):
    set2.add(input("enter number for 2nd set> "))

print("\n".join(set1.intersection(set2)))
