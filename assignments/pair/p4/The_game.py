def board_initalize():
    board = [None] * 8
    for i in range(8):
        row = [0] * 8
        board[i] = row

    # 1 is a white piece, 2 is a black piece
    for i in range(1, 8):
        board[0][i] = 1  # white pieces on top row
        board[7][i] = 1  # white pieces on bottom row
        board[i][0] = 2  # black pieces on left column
        board[i][7] = 2  # black pieces on right column


def move_direction(x, y, direction, board, player):
    direction = direction.lower()
    dx = 0
    dy = 0

    # Determine direction
    if 'n' in direction:
        dx = -1
    elif 's' in direction:
        dx = 1

    if 'e' in direction:
        dy = 1
    elif 'w' in direction:
        dy = -1

    # Count pieces along the line (both directions)
    count = 0
    for i in range(-7, 8):
        nx = x + i * dx
        ny = y + i * dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            if board[nx][ny] != 0:
                count += 1

    # Get destination coordinates based on allowed distance traveled
    dest_x = x + dx * count
    dest_y = y + dy * count

    # Check bounds to ensure no crash
    if not (0 <= dest_x < 8 and 0 <= dest_y < 8):
        return None, None, "Destination is out of bounds."

    # Check path for enemy pieces being jumped
    for step in range(1, count):
        middle_x = x + dx * step
        middle_y = y + dy * step

        if board[middle_x][middle_y] != 0:
            if board[middle_x][middle_y] != player:
                return None, None, "You cannot jump over enemy pieces."

    # Check if destination is occupied by own piece
    if board[dest_x][dest_y] != 0:
        return None, None, "You cannot land on your own piece."

    return dest_x, dest_y, None  # no error

def connected(board):
    #a function that check if the peices are 'connected'
    #not finished

def print_board(board):
    #not finished

def main():
    board = board_initalize()
    player_choice = 2  # 1 for White, 2 for Black
    victory = False

    while not victory:
        print_board(board)

        if player_choice == 2:
            print("Black player, please move\nTo move enter the position of a piece and the direction you want it to move.\nFor example, '7 1 se' will move the black piece at 7,1 down-right.")
            player_choice = 1
        else:
            print("White player, please move\nTo move enter the position of a piece and the direction you want it to move.\nFor example, '7 1 se' will move the white piece at 7,1 down-right.")
            player_choice = 2

        # Get input from the user
        move = input("Enter your move").strip().split()
        
        x = int(move[0])
        y = int(move[1])
        direction = move[2].lower() #.lower make the string lowercase so we dont have to account for capitals
        
        # Ensure the move is in bounds
        if not (0 <= x < 8 and 0 <= y < 8):
            print("Invalid coordinates")
            continue

        # Call move_direction to calculate the new position
        new_x, new_y, error = move_direction(x, y, direction, board, player_choice)

        # Move the piece (if the move is valid)
        board[new_x][new_y] = board[x][y]
        board[x][y] = 0  # Clear the old position

        if connected(board) == True:
            victory = True


if __name__ == "__main__":
    main()
