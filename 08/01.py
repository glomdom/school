n = int(input("enter amt of names> "))
names = set()

for _ in range(n):
    names.add(input("enter name> "))

print("\n".join(names))
