import random as r
import graphics as g
import time as t

__author__ = 'James Cunningham, Adriana Jergusova'
win = None

def is_satisfied(x_pos: int, y_pos: int, value: float, grid: list[list[int]]) -> tuple[bool, float]:
    """
    Takes the surrounding positions and checks the ratio of like neighbors to determine if it is satisfied 
    or if it should move. 
    Note: `value` is the value stored in the grid (representing color).
    """
    count = 0
    neighbors = 0

    # Check the surrounding neighbors and count satisfaction
    if x_pos > 0:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos - 1][y_pos + 1] != 2:
                neighbors += 1
            if check_same(value, x_pos - 1, y_pos + 1, grid):
                count += 1
        if grid[x_pos - 1][y_pos] != 2:
            neighbors += 1
        if check_same(value, x_pos - 1, y_pos, grid):
            count += 1
        if y_pos > 0:
            if grid[x_pos - 1][y_pos - 1] != 2:
                neighbors += 1
            if check_same(value, x_pos - 1, y_pos - 1, grid):
                count += 1

    if y_pos < (len(grid[0]) - 1):
        if grid[x_pos][y_pos + 1] != 2:
            neighbors += 1
        if check_same(value, x_pos, y_pos + 1, grid):
            count += 1

    if y_pos > 0:
        if grid[x_pos][y_pos - 1] != 2:
            neighbors += 1
        if check_same(value, x_pos, y_pos - 1, grid):
            count += 1

    if x_pos < len(grid) - 1:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos + 1][y_pos + 1] != 2:
                neighbors += 1
            if check_same(value, x_pos + 1, y_pos + 1, grid):
                count += 1
        if grid[x_pos + 1][y_pos] != 2:
            neighbors += 1
        if check_same(value, x_pos + 1, y_pos, grid):
            count += 1
        if y_pos > 0:
            if grid[x_pos + 1][y_pos - 1] != 2:
                neighbors += 1
            if check_same(value, x_pos + 1, y_pos - 1, grid):
                count += 1

    if neighbors == 0:  # Avoid division by zero
        satisfaction_percent = 100
    else:
        satisfaction_percent = count / neighbors

    if satisfaction_percent > .3:  # Using given value of .3
        return True, satisfaction_percent
    else:
        return False, satisfaction_percent


def check_same(value_search: int, x_search: int, y_search: int, grid: list[list[int]]) -> bool:
    """
    Helper function for `is_satisfied`.
    Checks if the grid at (x_search, y_search) matches the target value.
    """
    if grid[x_search][y_search] == value_search:
        return True
    else:
        return False


def find_best_location(x_pos: int, y_pos: int, grid: list[list[int]]) -> tuple[int, int]:
    """
    This function is intended to find the best possible location for an unsatisfied square to move into.
    It can only select empty locations and should choose the most "satisfying" location for the move.
    """
    value = grid[x_pos][y_pos]
    best_location = (x_pos, y_pos)
    best_satisfaction = 0

    # Check all surrounding neighbors and find the best location, i assume the object cant jump over filled spaces, it wasnt super clear in the instructions but i assumed so
    if x_pos > 0:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos - 1][y_pos + 1] == 2:
                satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos + 1, value, grid)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos - 1, y_pos + 1)
        if grid[x_pos - 1][y_pos] == 2:
            satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos, value, grid)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos - 1, y_pos)
        if y_pos > 0:
            if grid[x_pos - 1][y_pos - 1] == 2:
                satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos - 1, value, grid)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos - 1, y_pos - 1)

    if y_pos < len(grid[0]) - 1:
        if grid[x_pos][y_pos + 1] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos, y_pos + 1, value, grid)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos, y_pos + 1)

    if y_pos > 0:
        if grid[x_pos][y_pos - 1] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos, y_pos - 1, value, grid)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos, y_pos - 1)

    if x_pos < len(grid) - 1:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos + 1][y_pos + 1] == 2: 
                satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos + 1, value, grid)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos + 1, y_pos + 1)
        if grid[x_pos + 1][y_pos] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos, value, grid)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos + 1, y_pos)
        if y_pos > 0:
            if grid[x_pos + 1][y_pos - 1] == 2: 
                satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos - 1, value, grid)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos + 1, y_pos - 1)

    return best_location


def move_location(x_origin: int, y_origin: int, x_target: int, y_target: int, grid: list[list[int]]):
    """
    This function swaps the values of two locations allowing for exchange of data.
    It is used in the relocation function.
    """
    hold_value = grid[x_origin][y_origin]
    grid[x_origin][y_origin] = grid[x_target][y_target]
    grid[x_target][y_target] = hold_value


def initialize_grid(grid_length: int, grid_width: int, percent_blu: int, percent_red: int, percent_clr: int) -> list[list[int]]:
    """
    Initializes the grid with random values representing blue, red, and empty spaces based on provided percentages.
    """
    number = 0
    grid = [[2] * grid_width for number in range(grid_length)]

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
                grid[i][j] = 2 
                num_clr -= 1

    return grid

def print_grid(grid: list[list[int]]):
    global win  # Declare win as a global, i dont know why this fixes it but it does
    if win is None:
        win_width = 100 + 25 * len(grid[0]) 
        win_length = 100 + 25 * len(grid)    
        win = g.GraphWin('Simulation View', win_width, win_length)

    # Loop through the grid and create rectangles
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Calculate pos
            x1 = 50 + 25 * i  
            y1 = 50 + 25 * j  
            x2 = 75 + 25 * i  
            y2 = 75 + 25 * j  
            
            r = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))

            # Set color
            if grid[i][j] == 0:
                r.setFill('red')  
            elif grid[i][j] == 1:
                r.setFill('blue')
            else:
                r.setFill('white')
            
            r.draw(win)


def main():
    
    # Initialize the grid before using it
    grid = initialize_grid(20, 20, 45, 45, 10)  # Initialize the grid
    
    finished = False
    count = 0

    while not finished and count < 1000:
        finished = True  # assume complete until an unsatisfied square is found
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                
                # Only check for satisfaction if the square is not empty
                if value != 2:
                    satisfied, _ = is_satisfied(i, j, value, grid)  # Pass grid here
                    
                    # If the square is unsatisfied, find the best location for it and move it
                    if not satisfied:
                        finished = False  # We're not finished, as there is an unsatisfied square
                        best_location = find_best_location(i, j, grid)  # Pass grid here
                        if best_location != (i, j):
                            # Move the square to the best location
                            move_location(i, j, best_location[0], best_location[1], grid)  # Pass grid here
        
        
        print_grid(grid)
        t.sleep(.5)
        count += 1
        
    print(f"Simulation complete. All squares are satisfied. \n{count} repetitions required to reach results")

if __name__ == '__main__':
    main()
