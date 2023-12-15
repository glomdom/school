rows, cols = map(int, input().split(","))
matrix = []
max_sum = 0
max_square = None

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(rows - 2):
    for j in range(cols - 2):
        square = [matrix[i+k][j+l] for k in range(3) for l in range(3)]
        current_sum = sum(square)

        if current_sum > max_sum:
            max_sum = current_sum
            max_square = square

print(max_square)
