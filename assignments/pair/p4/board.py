import graphics as g
# Create a graphics window
WIDTH = 400
HEIGHT = 400
WHITE = 1
BLACK = -1

class Board:
    def __init__(self) -> None:
        self.board=[[0 for _ in range(8)]for _ in range(8)]
        self.win = g.GraphWin("board", WIDTH, HEIGHT)
        self.win.setBackground('#5F0000') 
        self.win.setCoords(0.0,0.0,8.0,8.0)

    def colors(self):
        for i in range(1,7):
            self.board[0][i]=WHITE #green
            self.board[i][0]=BLACK
            self.board[7][i]=WHITE
            self.board[i][7]=BLACK

    def pieces_board(self):
        for x in range(8):
            for y in range(8):
                r = g.Rectangle(g.Point(x,y),g.Point(x+1,y+1))
                r.setOutline("white")
                r.draw(self.win)
                if self.board[x][y]==WHITE:
                    c = g.Circle(g.Point(x+.5, y+.5), .4)
                    c.setFill("white")
                    c.draw(self.win)
                elif self.board[x][y]==BLACK:
                    c = g.Circle(g.Point(x+.5, y+.5), .4)
                    c.setFill("black")
                    c.draw(self.win)
        self.win.getMouse()


def main():
    b = Board()
    b.colors()
    b.pieces_board()

if __name__ == '__main__':
    main()
