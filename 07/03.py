n = int(input("enter number> "))
invited = set()     # set for people invited
came = set()        # set for people that showed invite

students = set()    # set for students
teachers = set()    # set for teachers

for _ in range(n):
    is_teacher = False
    invite = input("enter invite code> ")

    if invite[0].isdigit():
        is_teacher = True

    teachers.add(invite) if is_teacher else students.add(invite)
    invited.add(invite)

while True:
    confirmed = input("enter invite which came> ")

    if confirmed.lower() == "end":
        break

    came.add(confirmed)

t = teachers.difference(came)
s = students.difference(came)

print(f"{len(t) + len(s)}")
print("\n".join(t))
print("\n".join(s))
