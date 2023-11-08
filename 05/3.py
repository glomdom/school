"""
3rd problem from 05_stack_deque.
"""

from collections import deque

amt_food = int(input("enter amount of food$ "))
orders = deque(map(int, input("enter orders$ ").strip().split()))

print(max(orders))

while orders:
    curr = orders[0]

    if curr <= amt_food:
        amt_food -= curr
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    rem = ", ".join(map(str, orders))

    print(f"Orders remaining: {rem}")
