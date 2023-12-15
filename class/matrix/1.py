n = int(input("enter amt of cols and rows> "))
mat = []
left_diag = 0
right_diag = 0

for _ in range(n):
    mat.append([int(x) for x in input("enter numbers> ").split()])

# left_diag = sum([row[i] for i, row in enumerate(mat)])
# right_diag = sum([row[-i - 1] for i, row in enumerate(mat)])

left_diag = sum([mat[i][i] for i in range(len(mat))])
right_diag = sum([mat[i][~i] for i in range(len(mat))]) # flipvame bitovete na vtoriq `i`, koeto ni dava obratnoto -1 na nego (primer: 1 = ~0, 2 = ~1, ..)

print(left_diag, right_diag)
