"""
1st problem from 05_stack_deque.
"""

inp = input("enter nums$ ")
nums = [x.strip() for x in reversed(inp.strip().split(","))]

print(", ".join(nums))
