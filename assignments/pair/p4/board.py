import graphics as g
import os
# Create a graphics window
WIDTH = 400
HEIGHT = 400
WHITE = 1
BLACK = -1
EMPTY = 0

class Board:
    def __init__(self) -> None:
        self.board=[[0 for _ in range(8)]for _ in range(8)]
        self.win = g.GraphWin("board", WIDTH, HEIGHT)
        self.win.setBackground('#880808') 
        self.win.setCoords(0.0,0.0,8.0,8.0)

    def colors(self):
        for i in range(1,7):
            self.board[0][i]=WHITE
            self.board[i][0]=BLACK
            self.board[7][i]=WHITE
            self.board[i][7]=BLACK

    def draw_grid(self):
        x=0
        while x<8:
            y=0
            while y<8:
                r = g.Rectangle(g.Point(x,y),g.Point(x+1,y+1))
                r.draw(self.win)
                y+=1
            x+=1

    def draw_circle(self,x,y,color):
        c = g.Circle(g.Point(x+.5, y+.5), .4)
        c.setFill(color)
        c.draw(self.win)

    def highlight_square(self,dest_x, dest_y,color):
        r = g.Rectangle(g.Point(dest_x, dest_y), g.Point(dest_x + 1, dest_y + 1))
        r.setFill(color)
        r.draw(self.win)

    def pieces(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y]==WHITE:
                    self.draw_circle(x,y,"white")
                elif self.board[x][y]==BLACK:
                    self.draw_circle(x,y,"black")
    
    def count_direction(self, x, y, dir):
        """Counts total number of pieces along the line of action in both directions"""
        count = 1 
        dx, dy = dir[0], dir[1]

        # count forward
        for i in range(1, 8):
            nx = x + i * dx
            ny = y + i * dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[nx][ny] != EMPTY:
                    count += 1
            else:
                break

        # Backward
        for i in range(1, 8):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[nx][ny] != EMPTY:
                    count += 1
            else:
                break
        return count

    def legal_moves(self,x,y):
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1],[0, -1], [-1, -1], [-1, 0], [1, -1]]
        legal_moves = []

        for dir in directions:
            n = self.count_direction(x, y, dir)
            dest_x = x + n * dir[0]
            dest_y = y + n * dir[1]

            if 0 <= dest_x < 8 and 0 <= dest_y < 8:
                if self.board[dest_x][dest_y] != self.board[x][y]:
                    legal_moves.append([dest_x, dest_y, dir])
                    self.highlight_square(dest_x,dest_y, "blue")

    def select_move(self):
        m=(self.win.getMouse())
        x=int(m.getX())
        y=int(m.getY())
        
        if self.board[x][y]== 0:
            self.select_move()

        elif self.board[x][y]== WHITE or self.board[x][y]== BLACK:
            self.draw_circle(x,y,"grey")
            self.legal_moves(x,y)
        self.move(x,y)

    def move(self,x,y):
        m=(self.win.getMouse())
        nx=int(m.getX())
        ny=int(m.getY())
        if self.board[x][y]==1:
            self.board[nx][ny]=1
            self.board[x][y]=0
        if self.board[x][y]==-1:
            self.board[nx][ny]=-1
            self.board[x][y]=0
        self.draw_grid()
        self.pieces()
        self.win.getMouse()

        


def main():
    b = Board()
    b.colors()
    b.draw_grid()
    b.pieces()
    b.select_move()

if __name__ == '__main__':
    main()