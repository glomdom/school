n = int(input("enter num> "))
names = set()

for _ in range(n):
    name = input("enter name> ")
    names.add(name)

print("\n".join(names))
