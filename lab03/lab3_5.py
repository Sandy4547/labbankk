rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print(f"This block of {rows} rows x {columns} columns:")
for i in range(rows):
    print("O" * columns)