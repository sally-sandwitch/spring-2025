import random as r
import graphics as g
import time as t

__author__ = 'James Cunningham, Adriana Jergusova'
win = None

def is_satisfied(x_pos: int, y_pos: int, value: int, grid: list[list[int]]) -> tuple[bool, float]:
    """
    Takes the surrounding positions and checks the ratio of like neighbors to determine if it is satisfied 
    or if it should move. 
    Note: `value` is the value stored in the grid (representing color).
    """
    count = 0
    neighbors = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # All 8 directions

    for dx, dy in directions:
        nx, ny = x_pos + dx, y_pos + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):  # Check if neighbor is within bounds
            if grid[nx][ny] != 2:  # Check if not an empty spot
                neighbors += 1
            if grid[nx][ny] == value:  # Check if neighbor matches the current value
                count += 1

    # Avoid division by zero and calculate satisfaction
    if neighbors == 0:
        satisfaction_percent = 100
    else:
        satisfaction_percent = count / neighbors

    if satisfaction_percent > 0.5:  # Satisfaction threshold
        return True, satisfaction_percent
    else:
        return False, satisfaction_percent


def find_random_position(board):
    empty_positions = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:  # Empty space is represented by 2
                empty_positions.append((i, j))
                
    if empty_positions:
        return r.choice(empty_positions)
    
    return None


def move_location(x_origin: int, y_origin: int, x_target: int, y_target: int, grid: list[list[int]]):
    """
    This function swaps the values of two locations allowing for exchange of data.
    It is used in the relocation function.
    """
    grid[x_origin][y_origin], grid[x_target][y_target] = grid[x_target][y_target], grid[x_origin][y_origin]


def initialize_grid(grid_length: int, grid_width: int, percent_blu: int, percent_red: int, percent_clr: int) -> list[list[int]]:
    """
    Initializes the grid with random values representing blue, red, and empty spaces based on provided percentages.
    """
    grid = [[2] * grid_width for _ in range(grid_length)]  # Initialize grid with empty spaces (2)
    size = grid_width * grid_length
    num_red = int(size * percent_red) // 100
    num_blu = int(size * percent_blu) // 100
    num_clr = int(size * percent_clr) // 100

    for i in range(grid_length):
        for j in range(grid_width):
            random_num = r.randint(1, 100)
            if random_num <= percent_red and num_red > 0:
                grid[i][j] = 0  
                num_red -= 1
            elif random_num <= percent_red + percent_blu and num_blu > 0:
                grid[i][j] = 1  
                num_blu -= 1
            elif num_clr > 0:
                grid[i][j] = 2  # Empty space represented by 2
                num_clr -= 1

    return grid

def print_grid(grid: list[list[int]]):
    global win  # Declare win as a global
    if win is None:
        win_width = 100 + 25 * len(grid[0]) 
        win_length = 100 + 25 * len(grid)    
        win = g.GraphWin('Simulation View', win_width, win_length)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Calculate pos
            x1 = 50 + 25 * i  
            y1 = 50 + 25 * j  
            x2 = 75 + 25 * i  
            y2 = 75 + 25 * j  
            
            r = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))

            if grid[i][j] == 0:
                r.setFill('red')  
            elif grid[i][j] == 1:
                r.setFill('blue')
            else:
                r.setFill('white')
            
            r.draw(win)


def main():
    grid = initialize_grid(20, 20, 45, 45, 10)  # Initialize the grid
    finished = False
    count = 0

    while not finished and count < 1000:
        finished = True  # Assume complete until an unsatisfied square is found
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                
                # Only check for satisfaction if the square is not empty
                if value != 2:
                    satisfied, _ = is_satisfied(i, j, value, grid)  # Pass grid here
                    
                    # If the square is unsatisfied, find the best location for it and move it
                    if not satisfied:
                        finished = False  # We're not finished, as there is an unsatisfied square
                        best_location = find_random_position(grid)  # Replace with random location
                        if best_location is not None:
                            move_location(i, j, best_location[0], best_location[1], grid)  # Pass grid here
        
        
        print_grid(grid)
        t.sleep(1)
        count += 1
    win.getMouse()
    print(f"Simulation complete. All squares are satisfied. \n{count} repetitions required to reach results")


if __name__ == '__main__':
    main()
