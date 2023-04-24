import string
inputInfo = open("day12/input", "r").readlines()
letters = list(string.ascii_lowercase)
lettersBig = list(string.ascii_uppercase)
numbers = list(string.digits)
number = [int(i) for i in numbers]
newLine = []
newGrid = []


for y in range(len(inputInfo)):
    for x in range(len(inputInfo[y])-1):
        if any(item in inputInfo[y][x] for item in letters):
            newLine.append(letters.index(inputInfo[y][x]))
        elif inputInfo[y][x] == "S":
            newLine.append(0)
            startPosition = f"{y} {x}"
            for i in range(len(startPosition)):
                if startPosition[i] == " ":
                    startIndex = i
        else:
            newLine.append(25)
            endPosition = f"{y} {x}"
            for i in range(len(endPosition)):
                if endPosition[i] == " ":
                    endIndex = i
    newGrid.append(newLine)
    newLine = []
courseMap = []

x, y = 0, 0

# up, right, down, left

directionStr = ""

checkSequence = ["y > 0", "x < len(newGrid[y])-1", "y < len(newGrid)-1", "x > 0"]
checkSequence2 = ["newGrid[y-1][x]", "newGrid[y][x+1]", "newGrid[y+1][x]", "newGrid[y][x-1]"]

standValue = 0

for y in range (len(newGrid)):
    courseMap.append([])
    for x in range (len(newGrid[y])):
        if newGrid[y][x] != "E":
            if newGrid[y][x] == "S":
                standValue = 0
            else:
                standValue = newGrid[y][x]
            for i in range(4):
                if eval(checkSequence[i]):
                    if eval(f"{checkSequence2[i]} <= standValue + 1"):
                        directionStr += "1"
                    else:
                        directionStr += "0"
                else:
                    directionStr += "0"
            courseMap[y].append(directionStr)
            directionStr = ""
        else:
            courseMap[y].append("EEEE")

run = True
boolList = [False, False, False, False]

y, x = int(startPosition[:startIndex]), int(startPosition[startIndex+1:])

pathBuffer = [[courseMap[y][x], y, x]]
savedBufferNumber = 1
depth = 0

while run:
    bufferNumber = 0
    for position in pathBuffer:
        if position[1] == int(endPosition[:endIndex]) and position[2] == int(endPosition[endIndex+1:]):
            run = False
        if run:
            for i in range(4):
                if position[0][i] == str(1):
                    boolList[i] = True
                else:
                    boolList[i] = False
                if boolList[i] and i == 0:
                    if not [courseMap[position[1]-1][position[2]], position[1]-1, position[2]] in pathBuffer:
                        pathBuffer.append([courseMap[position[1]-1][position[2]], position[1]-1, position[2]])
                        bufferNumber += 1
                if boolList[i] and i == 1:
                    if not [courseMap[position[1]][position[2]+1], position[1], position[2]+1] in pathBuffer:
                        pathBuffer.append([courseMap[position[1]][position[2]+1], position[1], position[2]+1])
                        bufferNumber += 1
                if boolList[i] and i == 2:
                    if not [courseMap[position[1]+1][position[2]], position[1]+1, position[2]] in pathBuffer:
                        pathBuffer.append([courseMap[position[1]+1][position[2]], position[1]+1, position[2]])
                        bufferNumber += 1
                if boolList[i] and i == 3:
                    if not [courseMap[position[1]][position[2]-1], position[1], position[2]-1] in pathBuffer:
                        pathBuffer.append([courseMap[position[1]][position[2]-1], position[1], position[2]-1])
                        bufferNumber += 1
            savedBufferNumber += -1
            if savedBufferNumber == 0:
                savedBufferNumber = bufferNumber
                bufferNumber = 0
                depth += 1
print(depth)