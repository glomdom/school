n = int(input("enter number> "))
parking = set()

for _ in range(n):
    cmd = input("enter command> ").strip().split()

    if cmd[0].lower() == "in,":
        parking.add(cmd[1])
    elif cmd[0].lower() == "out,":
        parking.remove(cmd[1])

if len(parking) == 0:
    print("Parking lot is empty")
    exit(0)

while parking:
    print(parking.pop())
