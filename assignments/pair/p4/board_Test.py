Author="Adriana Jergusova and James Cunningham"

from board_v3 import Board, WHITE, BLACK, EMPTY
from vector import Vector

def empty_board():
    board = Board()
    board.board = [[EMPTY for _ in range(8)] for _ in range(8)]
    return board

def test_white_captures_black(empty_board):
    empty_board.board[2][2] = WHITE
    empty_board.board[4][4] = BLACK

    # Override count_direction to force 2-step move
    empty_board.count_direction = lambda p, d: 2

    piece = Vector(2, 2)
    legal_moves = empty_board.find_legal_moves(piece)
    assert [4, 4, [1, 1]] in legal_moves

    empty_board.move(2, 2, 4, 4)
    assert empty_board.board[4][4] == WHITE
    assert empty_board.board[2][2] == EMPTY

def test_cannot_capture_own_piece(empty_board):
    empty_board.board[3][3] = WHITE
    empty_board.board[5][5] = WHITE

    empty_board.count_direction = lambda p, d: 2

    piece = Vector(3, 3)
    legal_moves = empty_board.find_legal_moves(piece)
    assert [5, 5, [1, 1]] not in legal_moves

def test_win_detects_connected_group(empty_board):
    empty_board.board[0][0] = WHITE
    empty_board.board[0][1] = WHITE
    empty_board.board[1][1] = WHITE
    empty_board.board[1][0] = WHITE

    assert empty_board.check_win(WHITE)

def test_win_fails_on_disconnected_pieces(empty_board):
    empty_board.board[0][0] = WHITE
    empty_board.board[7][7] = WHITE

    assert not empty_board.check_win(WHITE)