Author="Adriana Jergusova and James Cunningham"

import board_v3
from vector import Vector

WHITE = 1
BLACK = -1

def main():
    board = board_v3.Board()
    board.colors()
    board.pieces_board()

    player_choice = 2  # 1 = white, 2 = black
    victory = False

    while not victory:
        if player_choice == 2:
            print("Black player, please move (e.g., x=1 y=7):")
            color = BLACK
            player_choice = 1
        else:
            print("White player, please move (e.g., x=0 y=1):")
            color = WHITE
            player_choice = 2

        try:
            x = int(input('x: '))
            y = int(input('y: '))

            if not (0 <= x < 8 and 0 <= y < 8):
                print("Invalid board position.")
                continue

            if board.board[x][y] != color:
                print("You must select your own piece.")
                continue

            piece = Vector(x, y)
            legal_moves = board.find_legal_moves(piece)

            if not legal_moves:
                print("No legal moves for this piece.")
                continue

            print("\nLegal moves:")
            for i, move in enumerate(legal_moves):
                print(f"{i}: Move to ({move[0]}, {move[1]})")

            board.set_highlight(legal_moves, x, y)
            board.pieces_board()

            choice = int(input('Select a move by number: '))
            if not (0 <= choice < len(legal_moves)):
                print("Invalid move choice.")
                continue

            dest_x, dest_y = legal_moves[choice][0], legal_moves[choice][1]
            board.move(x, y, dest_x, dest_y)
            board.clear_highlights()

            if board.check_win(color):
                board.pieces_board()
                winner = "Black" if color == BLACK else "White"
                print(f"{winner} wins!")
                victory = True

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()