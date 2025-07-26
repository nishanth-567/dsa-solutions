rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the elemnts of the matrix")

for i in range(rows):
    row = []
    for j in range(cols):
        mat = int(input(f"Element [{i+1}], [{j+1}]"))
        row.append(mat)
        matrix.append(row)

for row in matrix:
    print(row)

# for row in matrix:
#     for value in row:
#         print(value, end=' ')
#     print()