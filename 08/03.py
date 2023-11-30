n = int(input("enter amount of baby voice lines> "))
voice_lines = set()

for _ in range(n):
    voice_lines |= set(input("enter baby voice line> ").split())

print(voice_lines)
