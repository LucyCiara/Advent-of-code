inputInfo = open("day8/input", "r").readlines()
grid = []
for item in inputInfo:
    grid.append(item[:-1])
visible = True
visibleAngle = 4
visibles = 0
visiblesList = []
for y in range(len(grid)-1):
    for x in range(len(grid[y])):
        if 0 < y < len(grid) and 0 < x < len(grid[y])-1:
            for i in range(len(grid)):
                if i < y:
                    if grid[i][x] >= grid[y][x]:
                        visible = False
                if i == y and visible == False:
                    visibleAngle += -1
                    visible = True
                if i > y:
                    if grid[i][x] >= grid[y][x]:
                        visible = False
                if i == len(grid)-1 and visible == False:
                    visibleAngle += -1
                    visible = True
            for i in range(len(grid[0])):
                if i < x:
                    if grid[y][i] >= grid[y][x]:
                        visible = False
                if i == x and visible == False:
                    visibleAngle += -1
                    visible = True
                if i > x:
                    if grid[y][i] >= grid[y][x]:
                        visible = False
                if i == len(grid[0])-1 and visible == False:
                    visibleAngle += -1
                    visible = True
            if visibleAngle > 0:
                visibles += 1
            visibleAngle = 4

visibles += len(grid)*2+len(grid[0])*2-4
print(visibles)