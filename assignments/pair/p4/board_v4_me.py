import board_v3
#from board_v2 import Board
from vector import Vector

def main():
    board = board_v3.Board()
    board.colors()
    board.pieces_board()

    print('hello')

    player_choice = 2  # 1 for white, 2 for black
    victory = False

    while not victory:
        #print(board)

        if player_choice == 2:
            print("Black player, please move\nTo move enter the position of a piece and the direction you want it to move.\nFor example, '7 1 se' will move the black piece at 7,1 down-right.")
            player_choice = 1
        else:
            print("White player, please move\nTo move enter the position of a piece and the direction you want it to move.\nFor example, '7 1 se' will move the white piece at 7,1 down-right.")
            player_choice = 2

        # Get input from the user
        x = int(input('x: '))
        y = int(input('y: '))
        move = Vector(x, y)
        #move = Vector(input("Enter the location of the piece you want to move").strip().split())

        if board.board[x][y] == 1 or board.board[x][y] == -1:
            leagal_moves = board.find_legal_moves(move)

            print("here is a list of legal moves")

            for i in range (len(leagal_moves)):
                print(str(i) + ': ' + str(leagal_moves[i]))
        
        
            board.set_highlight(leagal_moves , x , y)
            board.pieces_board()

            choice = int(input('which option do you want to use?\n list the number you want to move to'))

            board.move(x, y, leagal_moves[choice][0], leagal_moves[choice][1])
            # board[leagal_moves[choice][1] , leagal_moves[choice][2]] = board[move[1]],board[move[2]]

            # board[move[1]],board[move[2]] = hold[1],hold[2]

            board.clear_highlights()


            if board.check_win(player_choice) == True:
                victory = True
                if player_choice == 1: print('black wins')
                else: print("white wins")
        else:
            print ("not legal piece, please try again")


if __name__ == "__main__":
    main()