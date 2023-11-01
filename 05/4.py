"""
4st problem from 05_stack_deque.
"""

clothes = list(map(int, input("enter clothes$ ").strip().split()))
cap = int(input("enter capacity$ "))

n_shelves = 0
curr_cap = cap

for cloth in clothes:
    if cloth <= curr_cap:
        curr_cap -= cloth
    else:
        n_shelves += 1
        curr_cap = cap - cloth

if curr_cap < cap:
    n_shelves += 1

print(n_shelves)
