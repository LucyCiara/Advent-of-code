inputInfo = open("day4/input", "r").readlines()
counter = 0
sel = []
sel2 = []
for item in inputInfo:
    sel.append([item[:item.find("-")], item[item.find("-")+1:item.find(",")]])
    sel2.append([item[item.find(",")+1:item.rfind("-")], item[item.rfind("-")+1:-1]])

selFull = []
selFull2 = []
for item in sel:
    tempList = []
    for i in range(int(item[0]), int(item[1])+1):
        tempList.append(i)
    selFull.append(tempList)
for item in sel2:
    tempList = []
    for i in range(int(item[0]), int(item[1])+1):
        tempList.append(i)
    selFull2.append(tempList)
for i in range(len(sel)):
    if any(item in selFull[i] for item in selFull2[i]):
        counter += 1

print(counter)