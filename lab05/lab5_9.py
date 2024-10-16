directions = [ [(0, 0) , (1, 0) , (2, 0)],
               [(0, 1) , (1, 1) , (2, 1)],
               [(0, 2) , (1, 2) , (2, 2)],
               [(0, 0) , (0, 1) , (0, 2)],
               [(1, 0) , (1, 1) , (1, 2)],
               [(2, 0) , (2, 1) , (2, 2)],
               [(0, 0) , (1, 1) , (2, 2)],
               [(0, 2) , (1, 1) , (2, 0)] ]

def sum_board(board, direction):
    total = 0
    for i in range(3):
        row = direction[i][0]
        col = direction[i][1]

        total += board[row][col]
    return abs(total)

def check_win(board):
    for direction in directions:
        if sum_board(board, direction) == 3:
            return True
    return False

broad = [[-1, 1, 1],
         [-1, -1, 0],
         [-1, 1, -1]]

print("table column 1 sum:", sum_board(broad, directions[0]))
print("table row 1 sum:", sum_board(broad, directions[3]))
print("table diagonal 1 sum:", sum_board(broad, directions[6]))

broad = [[1, 0, -1],
         [1, 1, 1],
         [0, 0, 1]]
is_win = check_win(broad)
print(f"Board is win: {is_win}")
broad = [[1, 1, -1],
         [1, 1, -1],
         [0, 0, 0]]
is_win = check_win(broad)
print(f"Board is win: {is_win}")