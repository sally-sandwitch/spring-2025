l = 0

with open('assignments/pair/p1/maze.txt') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            l += 1
print(l)