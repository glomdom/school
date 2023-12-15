row, col = map(int, input("enter rows and cols> ").split(","))
mat = []

for _ in range(row):
    mat.append([x for x in input("enter values> ").split()])

def find_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    count = 0

    for i in range(rows - 1):
        for j in range(cols - 1):
            square = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]

            if all(element == square[0] for element in square):
                count += 1

    return count

print(find_square(mat))
