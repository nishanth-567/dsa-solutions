row = int(input("Enter the number pf rows: "))
col = int(input("Enter the numnber of columns: "))

mat = []
print("Enter the elements in the matrix: \n")


for i in range(row):
    rows = []
    for j in range(col):
        matrix = int(input(f"Enter the element [{i+1}] [{j+1}]: "))
        rows.append(matrix)
        mat.append(rows)

for rows in mat:
    print(rows)