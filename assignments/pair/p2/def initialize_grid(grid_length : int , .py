grid_length=20
grid_width=20
precent_blu=.5
precent_red=.5
precent_clr=.1
def initialize_grid(grid_length : int , grid_width : int , precent_blu : int , precent_red : int , precent_clr : int) -> list[list[int]]:
	
    i = 0
    m=0
    grid = [None]* grid_length
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
            if random_num == 0 and num_red > 0:
                grid[i][j] = 0
                num_red -= 1
            if random_num == 1 and num_clr > 0:
                grid[i][j] = 1
                num_blu -= 1
            if random_num == 2 and num_clr > 0:
                grid[i][j] = 2
                num_clr -= 1
    return grid

initialize_grid(20,20,.5,.5,.1)