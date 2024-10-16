def convert_to_xo(row):
    """Converts the numeric values in a row to 'X', 'O', or ' '."""
    converted_row = []
    for value in row:
        if value == 1:
            converted_row.append('X')
        elif value == -1:
            converted_row.append('O')
        else:
            converted_row.append(' ')
    return converted_row

def display_row_data(row, isCovert):
    """Displays a single row of data, converting it if isCovert is True."""
    if isCovert:
        row = convert_to_xo(row)
    print(" | ".join(map(str, row)))

def display_line():
    """Displays a line between rows."""
    print("-" * 9)

def display(board, isCovert):
    """Displays the entire board, converting data if isCovert is True."""
    display_row_data(board[0], isCovert)
    display_line()
    display_row_data(board[1], isCovert)
    display_line()
    display_row_data(board[2], isCovert)

# Example usage
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
display(board, False)
print()
board = [
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]
]
display(board, False)
print()
display(board, True)