inputInfo = open("day9/test2", "r").readlines()
directionList, amountList, movementProgramming, xValues, yValues, x, y = [], [], [["U", "Y += -1"], ["D", "Y += 1"], ["L", "X += -1"], ["R", "X += 1"]], [0], [0], 0, 0
for item in inputInfo:
    directionList.append(item[0])
    amountList.append(int(item[2:-1]))
for i in range(len(directionList)):
    if directionList[i] == "U":
        y += amountList[i]
    elif directionList[i] == "D":
        y += -amountList[i]
    elif directionList[i] == "R":
        x += amountList[i]
    elif directionList[i] == "L":
        x += -amountList[i]
    xValues.append(x)
    yValues.append(y)
xValues.sort()
yValues.sort()
maxX, maxY, minX, minY = xValues[-1], yValues[-1], xValues[0], yValues[0]
maxX += -minX
maxY += -minY
gridH, grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, gridT, visualGrid, startX, startY = [], [], [], [], [], [], [], [], [], [], [], -minX, maxY+minY
ropeOrder = [["gridH", "XH", "YH", "#"], ["grid1", "X1", "Y1", "#"], ["grid2", "X2", "Y2", "#"], ["grid3", "X3", "Y3", "#"], ["grid4", "X4", "Y4", "#"], ["grid5", "X5", "Y5", "#"], ["grid6", "X6", "Y6", "#"], ["grid7", "X7", "Y7", "#"], ["grid8", "X8", "Y8", "#"], ["gridT", "XT", "YT", "-"]]
XH, YH, X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6, X7, Y7, X8, Y8, XT, YT = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in range(maxY+1):
    visualGrid.append([])
    for rope in ropeOrder:
        eval(rope[0]).append([])
    for ii in range(maxX+1):
        visualGrid[i].append("#")
        for rope in ropeOrder:
            eval(rope[0])[i].append("#")
for i in range(len(ropeOrder)-1, -1, -1):
    exec(f"visualGrid[{ropeOrder[i][2]}][{ropeOrder[i][1]}] = '{ropeOrder[i][0][-1]}'")
# for gridView in visualGrid:
#     print(gridView)
# print()
for rope in ropeOrder:
    exec(rope[1] + " = startX")
    exec(rope[2] + " = startY")
    exec(f"{rope[0]}[{rope[2]}][{rope[1]}] = '{rope[0][-1]}'")
yMove = 0
xMove = 0
for i in range(len(inputInfo)):
    for ii in range(amountList[i]):
        if amountList[i] == 20:
            pass
        for movement in movementProgramming:
            if directionList[i] == movement[0]:
                for iii in range(len(ropeOrder)):
                    if ropeOrder[iii] == ropeOrder[0]:
                        exec(f"{ropeOrder[iii][0]}[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][3]}'")
                        exec(f"{movement[1][:1]}{ropeOrder[iii][0][-1]}{movement[1][1:]}")
                        exec(f"{ropeOrder[iii][0]}[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][0][-1]}'")
                    else:
                        if eval(f"{ropeOrder[iii][1]} not in [{ropeOrder[iii-1][1]}, {ropeOrder[iii-1][1]}+1, {ropeOrder[iii-1][1]}-1] or {ropeOrder[iii][2]} not in [{ropeOrder[iii-1][2]}, {ropeOrder[iii-1][2]}+1, {ropeOrder[iii-1][2]}-1]"):
                            if eval(f"{ropeOrder[iii-1][1]} > {ropeOrder[iii][1]}"):
                                xMove = 1
                            if eval(f"{ropeOrder[iii-1][1]} < {ropeOrder[iii][1]}"):
                                xMove = -1
                            if eval(f"{ropeOrder[iii-1][1]} == {ropeOrder[iii][1]}"):
                                xMove = 0
                            if eval(f"{ropeOrder[iii-1][2]} > {ropeOrder[iii][2]}"):
                                yMove = 1
                            if eval(f"{ropeOrder[iii-1][2]} < {ropeOrder[iii][2]}"):
                                yMove = -1
                            if eval(f"{ropeOrder[iii-1][2]} == {ropeOrder[iii][2]}"):
                                yMove = 0
                            exec(f"{ropeOrder[iii][0]}[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][3]}'")
                            exec(f"{ropeOrder[iii][1]} += {xMove}")
                            exec(f"{ropeOrder[iii][2]} += {yMove}")
                            exec(f"{ropeOrder[iii][0]}[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][0][-1]}'")  
                for iii in range(len(ropeOrder)-1, -1, -1):
                    exec(f"visualGrid[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][0][-1]}'")
                visualGrid.clear()
                for iii in range(maxY+1):
                    visualGrid.append([])
                    for iv in range(maxX+1):
                        visualGrid[iii].append("#")
                for iii in range(len(ropeOrder)-1, -1, -1):
                    exec(f"visualGrid[{ropeOrder[iii][2]}][{ropeOrder[iii][1]}] = '{ropeOrder[iii][0][-1]}'")
                # for gridView in visualGrid:
                #     print(gridView)
                # print()  
sum = 0
for i in range(len(gridT)):
    for ii in range(len(gridT[i])):
        if gridT[i][ii] == "-" or gridT[i][ii] == "T":
            sum += 1
for gridInsight in gridT:
    print(gridInsight)
print(sum)