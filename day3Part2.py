import string
items = list(string.ascii_letters)

itemDick = {}
for i in range(len(items)):
    itemDick.update({items[i]: i+1})
inputInfo = open("day3/input", "r").readlines()
itemString = []
for item in inputInfo:
    itemString.append(item[:-1])
choppedItemString = []
choppedItemString2 = []
choppedItemString3 = []
for i in range(int(len((itemString))/3)):
    choppedItemString.append(itemString[i*3])
    choppedItemString2.append(itemString[i*3+1])
    choppedItemString3.append(itemString[i*3+2])


sumList = []
for i in range(len(choppedItemString)):
    run = True
    x = 0
    while run == True and x < len(choppedItemString[i]):
        y = 0
        while run == True and y < len(choppedItemString2[i]):
            z = 0
            while run == True and z < len(choppedItemString3[i]):
                if choppedItemString[i][x] == choppedItemString2[i][y] == choppedItemString3[i][z]:
                    sumList.append(choppedItemString[i][x])
                    run = False
                z += 1
            y += 1
        x += 1
sum = 0
for item in sumList:
    sum += itemDick[item]
print(sum)
