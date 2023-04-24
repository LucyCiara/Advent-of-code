inputInfo = open("day8/input", "r").readlines()
grid = []
for item in inputInfo:
    grid.append(item[:-1])
visible = True
north, south, west, east = 0, 0, 0, 0
SVS = []
biggestSVS = 0
biggestSVSCoords = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == 2 and y == 3:
            pass
        if 0 < y < len(grid) and 0 < x < len(grid[y]):
            for i in range(len(grid)):
                if i < y:
                    if int(grid[i][x]) >= int(grid[y][x]):
                        north = 0
                    north += 1
                if i > y:
                    if visible:
                        south += 1
                    if int(grid[i][x]) >= int(grid[y][x]):
                        visible = False
            visible = True
            for i in range(len(grid[0])):
                if i < x:
                    if int(grid[y][i]) >= int(grid[y][x]):
                        west = 0
                    west += 1
                if i > x:
                    if visible:
                        east += 1
                    if int(grid[y][i]) >= int(grid[y][x]):
                        visible = False
            visible = True
            if (north*south*east*west) > biggestSVS:
                biggestSVS = (north*south*east*west)
                biggestSVSCoords = [x, y]
            north, south, west, east = 0, 0, 0, 0
print(biggestSVS)