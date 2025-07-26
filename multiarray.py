n = int(input("Enter the size of the matrix: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        mat = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(mat)
    matrix.append(row)

print("The matrix is:")
for row in matrix:
    for value in row:
        print(value, end=' ')
    print()

