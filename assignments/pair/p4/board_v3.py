Author="Adriana Jergusova and James Cunningham"

import graphics as g
import vector  # Assuming this is your own module

WIDTH = 400
HEIGHT = 400
EMPTY = 0
WHITE = 1
BLACK = -1
GREEN = 1
BLUE = 4

class Piece:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

class Board:
    def __init__(self):
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.highlight = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.win = g.GraphWin("Lines of Action", WIDTH, HEIGHT)
        self.win.setBackground('#5F0000')
        self.win.setCoords(0.0, 0.0, 8.0, 8.0)
        self.drawn_objects = []  # Store all drawn shapes

    def colors(self):
        for i in range(1, 7):
            self.board[0][i] = WHITE
            self.board[7][i] = WHITE
            self.board[i][0] = BLACK
            self.board[i][7] = BLACK

    def move(self, start_x, start_y, end_x, end_y):
        moving_piece = self.board[start_x][start_y]
        self.board[end_x][end_y] = moving_piece
        self.board[start_x][start_y] = EMPTY

    def clear_drawn_objects(self):
        for obj in self.drawn_objects:
            obj.undraw()
        self.drawn_objects = []

    def pieces_board(self):
        self.clear_drawn_objects()  # Clear before redrawing

        for x in range(8):
            for y in range(8):
                if self.highlight[x][y] == GREEN:
                    r = g.Rectangle(g.Point(x, y), g.Point(x + 1, y + 1))
                    r.setFill('green')
                    r.draw(self.win)
                    self.drawn_objects.append(r)
                elif self.highlight[x][y] == BLUE:
                    r = g.Rectangle(g.Point(x, y), g.Point(x + 1, y + 1))
                    r.setFill('blue')
                    r.draw(self.win)
                    self.drawn_objects.append(r)

                r = g.Rectangle(g.Point(x, y), g.Point(x + 1, y + 1))
                r.setOutline("white")
                r.draw(self.win)
                self.drawn_objects.append(r)

                if self.board[x][y] == WHITE:
                    c = g.Circle(g.Point(x + 0.5, y + 0.5), 0.4)
                    c.setFill("white")
                    c.draw(self.win)
                    self.drawn_objects.append(c)
                elif self.board[x][y] == BLACK:
                    c = g.Circle(g.Point(x + 0.5, y + 0.5), 0.4)
                    c.setFill("black")
                    c.draw(self.win)
                    self.drawn_objects.append(c)

    def clear_highlights(self):
        self.highlight = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.clear_drawn_objects()
        self.pieces_board()

    def set_highlight(self, legal_moves , x , y):
        self.highlight[x][y] = BLUE
        for l in legal_moves:
            self.highlight[l[0]][l[1]] = GREEN

    def count_direction(self, p, direction):
        """Counts total number of pieces along the line of action in both directions"""
        count = 1 
        x = p.get_x()
        y = p.get_y()
        dx, dy = direction[0], direction[1]

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

    def find_legal_moves(self, p):
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1],[0, -1], [-1, -1], [-1, 0], [1, -1]]
        legal_moves = []

        for dir in directions:
            n = self.count_direction(p, dir)
            dest_x = p.get_x() + n * dir[0]
            dest_y = p.get_y() + n * dir[1]
            

            if 0 <= dest_x < 8 and 0 <= dest_y < 8:
                if self.board[dest_x][dest_y] != self.board[p.get_x()][p.get_y()]:
                    legal_moves.append([dest_x, dest_y, dir])

        return legal_moves

    def check_win(self, color):
        total = 0
        positions = []

        for x in range(8):
            for y in range(8):
                if self.board[x][y] == color:
                    positions.append([x, y])
                    total += 1

        visited = [[False]*8 for _ in range(8)]
        locations = [positions[0]]
        connected = 0

        while locations:
            x, y = locations.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            connected += 1

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny] and self.board[nx][ny] == color:
                        locations.append([nx, ny])

        return connected == total
