inputInfo = open("day5/input", "r").readlines()
L0, L1, L2, L3, L4, L5, L6, L7, L8 = [], [], [], [], [], [], [], [], []
cyberpunk2077 = [L0, L1, L2, L3, L4, L5, L6, L7, L8]
for i in range(8):
    for ii in range(len(inputInfo[i])):
        if inputInfo[i][ii] == "[":
            cyberpunk2077[int(ii/4)].append(inputInfo[i][ii:ii+3])
    # for inputInfo[i] in cyberpunk2077:
    #     if len(inputInfo[i]) < i+1:
    #         inputInfo[i].append("")
commands = []
run = True
i = 0
while run and i < len(inputInfo):
    if inputInfo[i].find("m") > -1:
        run = False
        lineStart = i
    i += 1
run = True
i = len(inputInfo)-1
while run and i >= 0:
    if inputInfo[i].find("m") > -1:
        run =  False
        lineEnd = i
    i += -1
for i in range(lineStart, lineEnd+1):
    commands.append(inputInfo[i])
amountList = []
destinationList = []
originList = []
strNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(len(commands)):
    if commands[i][6] in strNum:
        amountList.append(int(commands[i][5:7]))
    else:
        amountList.append(int(commands[i][5]))
    destinationList.append(int(commands[i][-2]))
    originList.append(int(commands[i][-7]))
# for i in range(len(commands)):
#     print(amountList[i], originList[i], destinationList[i])
i = 0
ii = 0
for i in range(len(commands)):
    for ii in range(amountList[i]-1, -1, -1):
        cyberpunk2077[destinationList[i]-1].insert(0, cyberpunk2077[originList[i]-1].pop(ii))
wordSalad = ""
for i in range(len(cyberpunk2077)):
    if len(cyberpunk2077[i]) > 0:
        wordSalad+=cyberpunk2077[i][0][1]
    else:
        wordSalad+="#"
print(wordSalad)
