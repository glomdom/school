n = int(input("enter amount of grades> "))
grades = {}

for _ in range(n):
    name, grade = input("enter name and grade> ").split()

    if name in grades:
        grades[name].append(float(grade))
    else:
        grades[name] = [float(grade)]

for name, grade in grades.items():
    avg = sum(grade) / len(grade)
    formatted = " ".join(["{:.2f}".format(x) for x in grade])

    print(f"{name} -> {formatted} (avg: {avg:.2f})")
