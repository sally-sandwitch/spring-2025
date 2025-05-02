import random as r

__author__ = 'James Cunningham, Adriana Jergusova'
win=None
grid=None

def is_satisfied(x_pos: int, y_pos: int, value: float) -> (bool, float):
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
            if check_same(value, x_pos - 1, y_pos + 1):
                count += 1
        if grid[x_pos - 1][y_pos] != 2:
            neighbors += 1
        if check_same(value, x_pos - 1, y_pos):
            count += 1
        if y_pos > 0:
            if grid[x_pos - 1][y_pos - 1] != 2:
                neighbors += 1
            if check_same(value, x_pos - 1, y_pos - 1):
                count += 1

    if y_pos < len(grid[0]) - 1:
        if grid[x_pos][y_pos + 1] != 2:
            neighbors += 1
        if check_same(value, x_pos, y_pos + 1):
            count += 1

    if y_pos > 0:
        if grid[x_pos][y_pos - 1] != 2:
            neighbors += 1
        if check_same(value, x_pos, y_pos - 1):
            count += 1

    if x_pos < len(grid) - 1:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos + 1][y_pos + 1] != 2:
                neighbors += 1
            if check_same(value, x_pos + 1, y_pos + 1):
                count += 1
        if grid[x_pos + 1][y_pos] != 2:
            neighbors += 1
        if check_same(value, x_pos + 1, y_pos):
            count += 1
        if y_pos > 0:
            if grid[x_pos + 1][y_pos - 1] != 2:
                neighbors += 1
            if check_same(value, x_pos + 1, y_pos - 1):
                count += 1

    if neighbors == 0:  # Avoid division by zero
        satisfaction_percent = 100
    else:
        satisfaction_percent = count / neighbors

    if satisfaction_percent > 1:  # using 1 for placeholder
        return True, satisfaction_percent
    else:
        return False, satisfaction_percent


def check_same(value_search: int, x_search: int, y_search: int) -> bool:
    """
    Helper function for `is_satisfied`.
    Checks if the grid at (x_search, y_search) matches the target value.
    """
    if grid[x_search][y_search] == value_search:
        return True
    else:
        return False


def find_best_location(x_pos: int, y_pos: int) -> (int, int):
    """
    This function is intended to find the best possible location for an unsatisfied square to move into.
    It can only select empty locations and should choose the most "satisfying" location for the move.
    """
    value = grid[x_pos][y_pos]
    best_location = (x_pos, y_pos)
    best_satisfaction = 0

    # Check all surrounding neighbors and find the best location
    if x_pos > 0:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos - 1][y_pos + 1] == 2:
                satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos + 1, value)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos - 1, y_pos + 1)
        if grid[x_pos - 1][y_pos] == 2:
            satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos, value)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos - 1, y_pos)
        if y_pos > 0:
            if grid[x_pos - 1][y_pos - 1] == 2:
                satisfied, satisfaction_percent = is_satisfied(x_pos - 1, y_pos - 1, value)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos - 1, y_pos - 1)

    if y_pos < len(grid[0]) - 1:
        if grid[x_pos][y_pos + 1] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos, y_pos + 1, value)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos, y_pos + 1)

    if y_pos > 0:
        if grid[x_pos][y_pos - 1] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos, y_pos - 1, value)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos, y_pos - 1)

    if x_pos < len(grid) - 1:
        if y_pos < len(grid[0]) - 1:
            if grid[x_pos + 1][y_pos + 1] == 2: 
                satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos + 1, value)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos + 1, y_pos + 1)
        if grid[x_pos + 1][y_pos] == 2: 
            satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos, value)
            if satisfied and satisfaction_percent > best_satisfaction:
                best_location = (x_pos + 1, y_pos)
        if y_pos > 0:
            if grid[x_pos + 1][y_pos - 1] == 2: 
                satisfied, satisfaction_percent = is_satisfied(x_pos + 1, y_pos - 1, value)
                if satisfied and satisfaction_percent > best_satisfaction:
                    best_location = (x_pos + 1, y_pos - 1)

    return best_location



def move_location(x_origin: int, y_origin: int, x_target: int, y_target: int):
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
    grid = [[None] * grid_width for _ in range(grid_length)]

    size = grid_width * grid_length
    num_red = int(size * percent_red)/100
    num_blu = int(size * percent_blu)/100
    num_clr = int(size * percent_clr)/100

    for i in range(grid_length):
        for j in range(grid_width):
            random_num = r.randint(1, 100)
            if random_num <= percent_red and num_red > 0:
                grid[i][j] = 0  # count red
                num_red -= 1
            elif random_num <= percent_red + percent_blu and num_blu > 0:
                grid[i][j] = 1  # count blue
                num_blu -= 1
            elif num_clr > 0:
                grid[i][j] = 2  # count empty
                num_clr -= 1

    return grid

def main():
    grid = initialize_grid(20, 20, 45, 45, 10)  # Initialize the grid
    finished = False
    count = 0

    while not finished and count < 100000:
        finished = True  # assume complete untill a unsatisfied square found
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                
                # Only check for satisfaction if the square is not empty
                if value != 2:
                    satisfied, _ = is_satisfied(i, j, value,)
                    
                    # If the square is unsatisfied, find the best location for it and move it
                    if not satisfied:
                        finished = False  # We're not finished, as there is an unsatisfied square
                        best_location = find_best_location(i, j)
                        if best_location != (i, j):
                            # Move the square to the best location
                            move_location(i, j, best_location[0], best_location[1])
        
        print (grid)
        count += 1
        
    print("Simulation complete. All squares are satisfied.\n %i repitions requited to reach results")