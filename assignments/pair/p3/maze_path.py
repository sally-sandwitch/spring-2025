
"""authors == James & Adrianna"""

def move(y_pos : int , x_pos : int , maze : list[list[str]] , checkpoint):

    # if we have already used a checkpoint remove the used checkpoint so we dont spiral into an infinate loop
    if len(checkpoint) > 0:
        if (y_pos , x_pos) == checkpoint[-1]:
            checkpoint = checkpoint[:-1]


    #make sure we are not at exit, if so we are done
    if maze[y_pos + 1][x_pos] == 'O':
        return True

    #set up a check for dead ends
    deadend = True

    #check up
    if maze[y_pos - 1][x_pos] == ' ':

        #save checkpoint in furcation if there are branching paths
        if maze[y_pos][x_pos - 1] == ' ' or maze[y_pos][x_pos + 1] == ' ' or maze[y_pos + 1][x_pos] == ' ':
            checkpoint.append((y_pos , x_pos))

        maze[y_pos - 1][x_pos] = 'X' #mark as a used path
        deadend = False
        move(y_pos - 1 , x_pos , maze , checkpoint)

    #check down
    if maze[y_pos + 1][x_pos] == ' ':

        #save checkpoint in furcation if there are branching paths
        if maze[y_pos][x_pos - 1] == ' ' or maze[y_pos][x_pos + 1] == ' ' or maze[y_pos - 1][x_pos] == ' ':
            checkpoint.append((y_pos , x_pos))

        maze[y_pos+1][x_pos] = 'X' #mark as a used path
        deadend = False
        move(y_pos + 1 , x_pos , maze , checkpoint)
    

    #check left
    if maze[y_pos][x_pos - 1] == ' ':

        #save checkpoint in furcation if there are branching paths
        if maze[y_pos + 1][x_pos] == ' ' or maze[y_pos][x_pos + 1] == ' ' or maze[y_pos - 1][x_pos] == ' ':
            checkpoint.append((y_pos , x_pos))

        maze[y_pos][x_pos - 1] = 'X' #mark as a used path
        deadend = False
        move(y_pos , x_pos  - 1, maze , checkpoint)
    
    #check right
    if maze[y_pos][x_pos + 1] == ' ':

        #save checkpoint in furcation if there are branching paths
        if maze[y_pos + 1][x_pos] == ' ' or maze[y_pos][x_pos - 1] == ' ' or maze[y_pos - 1][x_pos] == ' ':
            checkpoint.append((y_pos , x_pos))

        maze[y_pos+1][x_pos] = 'X' #mark as a used path
        deadend = False
        move(y_pos , x_pos + 1 , maze , checkpoint)

    #make a code segment that changes the Xs to #s if we are in a dead end
    if deadend == True:
        maze[y_pos][x_pos] == '#'

        (y_pos , x_pos) = checkpoint[-1]

        move(y_pos , x_pos , maze , checkpoint)

    #if all this fails, solving the maze is impossible
    return False



def main():
    Filename='assignments/pair/p3/maze.txt'
    with open(Filename) as f:
        maze = []
        for line in f:
            row = []
            for c in line.strip():
                row.append(c)
            maze.append(row)
    y_pos = 0
    for i in range(len(maze[0])):
        if maze[0][i] == 'I':
            x_pos = i

    move(y_pos , x_pos , maze , [])
    #for row in range(len(maze_lines)):
    #    line = maze_lines[row].strip()  # remove excess lines
    print (maze)

if __name__=="__main__":
    main()