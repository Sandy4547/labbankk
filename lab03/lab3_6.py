rows = int(input("Enter number of rows: "))

columns = 9

print(f"This block of {rows} rows x {columns} columns:")
for i in range(rows):
    num_hashes = 2 * i + 1
    num_Os_each_side = (columns - num_hashes) // 2
    
    row_pattern = "O" * num_Os_each_side + "#" * num_hashes + "O" * num_Os_each_side
    print(row_pattern)