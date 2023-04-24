inputInfo = open("day9/test", "r").readlines()
directionList = []
amountList = []
movementProgramming = [["U", "HY += -1", "TY += -1"], ["D", "HY += 1", "TY += 1"], ["L", "HX += -1", "TX += -1"], ["R", "HX += 1", "TX += 1"]]
for item in inputInfo:
    directionList.append(item[0])
    amountList.append(int(item[2:-1]))
xValues = [0]
yValues = [0]
x = 0
y = 0
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
maxX = xValues[-1]
maxY = yValues[-1]
minX = xValues[0]
minY = yValues[0]
maxX += -minX
maxY += -minY
startX = -minX
startY = maxY+minY
gridH = []
gridT = []
HX = startX
HY = startY
TX = HX
TY = HY
for i in range(maxY+1):
    gridH.append([])
    gridT.append([])
    for ii in range(maxX+1):
        gridH[i].append("#")
        gridT[i].append("#")
gridH[HY][HX] = "H"
gridT[TY][TX] = "T"
# for item in gridH:
#     print(item)
# print()
for item in gridT:
    print(item)
print()
for i in range(len(inputInfo)):
    for ii in range(amountList[i]):
        for item in movementProgramming:
            if directionList[i] == item[0]:
                gridH[HY][HX] = "#"
                exec(item[1])
                gridH[HY][HX] = "H"
                # for picture in gridH:
                #     print(picture)
                # print()
                if TX not in [HX, HX+1, HX-1] or TY not in [HY, HY+1, HY-1]:
                    gridT[TY][TX] = "-"
                    if HX > TX and HY > TY:
                        TX += 1
                        TY += 1
                    elif HX > TX and HY < TY:
                        TX += 1
                        TY += -1
                    elif HX < TX and HY > TY:
                        TX += -1
                        TY += 1
                    elif HX < TX and HY < TY:
                        TX += -1
                        TY += -1
                    else:
                        exec(item[2])
                    gridT[TY][TX] = "T"
                # for picture in gridT:
                #     print(picture)
                # print()
sum = 0
for i in range(len(gridT)):
    for ii in range(len(gridT[i])):
        if gridT[i][ii] == "-" or gridT[i][ii] == "T":
            sum += 1
print(sum)