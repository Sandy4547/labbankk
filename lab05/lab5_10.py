import random

# Function to convert numeric board values to 'X', 'O', or ' '
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

# Function to display a single row of data
def display_row_data(row, isCovert):
    """Displays a single row of data, converting it if isCovert is True."""
    if isCovert:
        row = convert_to_xo(row)
    print(" | ".join(map(str, row)))

# Function to display a line between rows
def display_line():
    """Displays a line between rows."""
    print("-" * 9)

# Function to display the entire board
def display(board, isCovert):
    """Displays the entire board, converting data if isCovert is True."""
    display_row_data(board[0], isCovert)
    display_line()
    display_row_data(board[1], isCovert)
    display_line()
    display_row_data(board[2], isCovert)

# Possible directions for winning (rows, columns, diagonals)
directions = [
    [(0, 0), (1, 0), (2, 0)],  # Column 1
    [(0, 1), (1, 1), (2, 1)],  # Column 2
    [(0, 2), (1, 2), (2, 2)],  # Column 3
    [(0, 0), (0, 1), (0, 2)],  # Row 1
    [(1, 0), (1, 1), (1, 2)],  # Row 2
    [(2, 0), (2, 1), (2, 2)],  # Row 3
    [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
    [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
]

# Function to sum the values in a given direction
def sum_board(board, direction):
    total = 0
    for i in range(3):
        row = direction[i][0]
        col = direction[i][1]
        total += board[row][col]
    return abs(total)

# Function to check if there is a winning condition on the board
def check_win(board):
    for direction in directions:
        if sum_board(board, direction) == 3:
            return True
    return False

# Randomly select the first player
def random_player():
    value = random.random()
    if value < 0.5:
        return "O"
    else:
        return "X"

# Switch to the next player
def next_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

# Update the board with the player's move
def play_board(player, board, pos):
    value = 0
    if player == "X":
        value = 1
    elif player == "O":
        value = -1
    pos_row = (pos - 1) // 3
    pos_col = (pos - 1) % 3
    board[pos_row][pos_col] = value

# Main game loop for playing Tic-Tac-Toe
def play_game_tictactoa():
    print("--------------- Game OX ---------------")
    player = random_player()
    print(f"First player is {player}.")
    print("Guide board input")
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display(board, False)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    turn = 0
    while True:
        pos = input(f"Player {player} selected position board[1-9]:")
        pos = int(pos)
        play_board(player, board, pos)
        display(board, True)
        turn += 1
        is_win = check_win(board)
        if is_win or turn == 9:
            break
        player = next_player(player)
    if is_win:
        print(f"Player {player} is win!")
    else:
        print("Draw")
    print("End Program")

# Start the game
play_game_tictactoa()