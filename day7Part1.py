inputInfo = open("day7/input", "r").readlines()
tree = {"/": {"sum": 0}}
path = "tree"
strNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
endNumberIndex = 0
endNumberIndexList = []
targetSums = []
for i in range(len(inputInfo)):
    if inputInfo[i][0] in strNum:
        endNumberIndex = 0
        for number in strNum:
            if inputInfo[i].rfind(number) > endNumberIndex:
                endNumberIndex = inputInfo[i].rfind(number)
        eval(path).update({f"{inputInfo[i][endNumberIndex+2:-1]}": int(inputInfo[i][:endNumberIndex+1])})
        eval(path)["sum"] += int(inputInfo[i][:endNumberIndex+1])
    elif inputInfo[i][2:7] == "cd ..":
        eval(path[:path.rfind("[")])["sum"] += eval(path)["sum"]
        if eval(path)["sum"] <= 100000:
            targetSums.append(eval(path)["sum"])
        path = path[:path.rfind("[")]
    elif inputInfo[i][2:4] == "cd":
        path += f"['{inputInfo[i][5:-1]}']"
    elif inputInfo[i][:3] == "dir":
        eval(path).update({f"{inputInfo[i][4:-1]}": {"sum": 0}})
depth = -1
for i in range(len(path)):
    if path[i] == "[":
        depth += 1
for i in range(depth):
    eval(path[:path.rfind("[")])["sum"] += eval(path)["sum"]
    if eval(path)["sum"] <= 100000:
        targetSums.append(eval(path)["sum"])
    path = path[:path.rfind("[")]
totalTargetSum = 0
for item in targetSums:
    totalTargetSum += item
print(totalTargetSum)