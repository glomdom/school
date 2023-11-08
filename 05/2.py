"""
2nd problem from 05_stack_deque.
"""

n = int(input("enter amount of commands$ "))
stack = []

for _ in range(n):
    cmd = input("enter command$ ").split()

    match cmd[0]:
        case "1":
            stack.append(int(cmd[1]))
        case "2":
            stack.pop()
        case "3":
            print(max(stack))
        case "4":
            print(min(stack))
        case "5":
            print(len(stack))
        case _:
            print("stop right there you criminal scum!")
            exit(1)

print(", ".join([str(x) for x in reversed(stack)]))
