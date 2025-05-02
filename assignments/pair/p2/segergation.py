# 30% similarity (satisfaction ratio of colors around agent)
# 50% color ratio
# 10% empty
# show rounds
# show 100%


#precent=

#while percent!=100:
    
    
import random as r

__author__ = 'James Cunningham, Adriana Jergusova'

def is_satisfied(x_pos : int , y_pos : int, value :  float) -> True/False , float:
    """
    Takes the surrouding positions and checks ratio of like neighbboirs to determine if it is satisfied / if it should move
    note: __value is the value stored in the grio aka colour__
    """
	count = 0
	neighbors = 0

    '''
    The sturcture in the if statmentes are as folows
    make sure the x - posistion is valid
    make sure the y - posistion is valid
    if the grid location isnt empty add to the neighbors count
    if the grid location is the same colour then add to the counter count (i should have used a different name, mb)
    '''

	if x_pos > 1:
		if y_pos < len(grid[0]):
            if grid[x_pos - 1][y_pos + 1] != 2:
                neighbors += 1
            if check_same(value , x_pos-1 , y_pos+1) == True:
                count += 1
        if grid[x_pos - 1][y_pos] != 2:
            neighbors += 1
		if check_same(value , x_pos-1 , y_pos) == True:
            count += 1
        if y_pos > 1:
            if grid[x_pos - 1][y_pos - 1] != 2:
                neighbors += 1
			if check_same(value , x_pos-1 , y_pos-1) == True:
                count += 1
        
    if y_pos < len(grid[0]):
        if grid[x_pos][y_pos + 1] != 2:
            neighbors += 1
        if check_same(value , x_pos , y_pos+1) == True:
            count += 1
    if y_pos > 1:
        if grid[x_pos][y_pos - 1] != 2:
            neighbors += 1
        if check_same(value , x_pos , y_pos-1) == True:
            count += 1

    if x_pos < len(grid):
        if y_pos < len(grid[0]):
            if grid[x_pos + 1][y_pos + 1] != 2:
            neighbors += 1
            if check(value , x_pos+1 , y_pos+1) == True:
                count += 1
        if grid[x_pos + 1][y_pos] != 2:
            neighbors += 1
        if check_same(value , x_pos+1 , y_pos) == True:
            count += 1
		if y_pos > 1:
            if grid[x_pos + 1][y_pos - 1] != 2:
                neighbors += 1
			if check_same(value , x_pos+1 , y_pos-1) == True:
                count += 1
    '''
    calculate the precent of like neighbors
    check to see if the location is good
    return T/F and the value of the satisfaction (for use in determineing where to move, see find_best_location
    '''
    count / neighbors = satisfaction_precent

    if satisfaction_precent < min_precent_for_satisfaction:
        return True , satisfaction_precent
        else:
            return False , satisfaction_precent
	

def check_same(value_search : int , x_search : int, y_search : int) -> True/False:
    """
    Helper function for is_satisfied
    """
    if grid[x_search][y_search] == value_search:
        return True
    else:
        return False

def find_best_location(x_pos : int , y_pos :int) -> (int , int):
    """
    This functions purpose is to find the best possable location for an unsatisfied square to move into.
    It can only select empty locations and shoule chose the most "satisfying" location for the move.
    unfinished, hopefully will be finished sometime 2/27/2025
    """
    value = grid[x_pos][y_pos]
    
    if x > 1:
		if y < len(grid[0]):
            if grid[x_pos-1][y_pos+1] == 2:
                is_satisfied(x_pos - 1 , y_pos + 1 , value)

		if grid[x_pos-1][y_pos] == 2:
            is_satisfied(x_pos-1 , y_pos , value)
        if y > 1:
			if grid[x_pos-1][y_pos - 1] == 2:
                is_satisfied(x_pos-1 , y_pos - 1 , value)
        
    if y < len(grid[0]):
        if grid[x_pos][y_pos + 1] == 2:
            is_satisfied(x_pos , y_pos +1 , value)
    if y > 1:
        if grid[x_pos][y_pos-1] == 2:
            is_satisfied(x_pos , y_pos - 1, value)

    if x < len(grid):
        if y < len(grid[0]):
            if grid[x_pos + 1][y_pos+1] == 2:
                is_satisfied(x_pos + 1, y_pos + 1, value)
        if grid[x_pos + 1][y_pos] == 2:
            is_satisfied(x_pos + 1 , y_pos , value)
		if y > 1:
			if grid[x_pos + 1][y_pos-1] == 2:
                is_satisfied(x_pos + 1, y_pos - 1 , value)
        #save greatest satisfaction, impliment through adding a section to each location search to check if new satisfaction rate is > old rate


def move_location(x_origin : int, y_origin : int, x_target : int, y_target : int):
    """
    This function swaps the values of two locarions allowing for excange of data, used in the relocation function
    """
    hold_value = grid[x_origin][y_origin]
    grid[x_origin][y_origin] = grid[x_target][y_target]
    grid[x_target][y_target] = hold_value




def initialize_grid(grid_length : int , grid_width : int , precent_blu : int , precent_red : int , precent_clr : int) -> list[list[int]]:
	'''
    it initalizes the grid, explination probably unnessicary but redundant
    '''
    i = 0
    grid = [None] grid_length
    for i in range < grid_width:
        row = [0.0] * len(m)
        grid[i] = row

    size = grid_width * grid_length
    num_red = size * precent_red
    num_blu = size * precent_blu
    num_clr = size * precent_clr
    
    i = 0
    for i in range < grid_length:
        j = 0
        for j in range < grid_width:
            random_num = r.randint(1,100)
            if random_num = 0 and num_red > 0:
                grid[i][j] = 0
                num_red -= 1
            if raandom_num = 1 and num_clr > 0:
                grid[i][j] = 1
                num_blu -= 1
            if random_num = 2 and num_clr > 0:
                grid[i][j] = 2
                num_clr -= 1
	
	return grid