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
for item in itemString:
    choppedItemString.append(item[:int(len(item)/2)])
    choppedItemString2.append(item[int(len(item)/2):])
# DIDNT READ THE FUCKING TASK OH MY GOD
# for item in choppedItemString:
#     run1, i = True, 0
#     while run1 and i < len(items):
#         run2 = True
#         x = 0
#         while run2 and x < len(item):
#             if item[x] == items[i]:
#                 item = item[0:x] + item[x+1:]
#                 run2 = False
#             else:
#                 x += 1
#         i += 1
#     lettuce.append(item)
sumList = []
for i in range(len(choppedItemString)):
    run = True
    x = 0
    while run == True and x < len(choppedItemString[i]):
        y = 0
        while run == True and y < len(choppedItemString2[i]):
            if choppedItemString[i][x] == choppedItemString2[i][y]:
                sumList.append(choppedItemString[i][x])
                run = False
            y += 1
        x += 1
sum = 0
for item in sumList:
    sum += itemDick[item]

print(sum)
