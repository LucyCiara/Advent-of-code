inputInfo = open("day1/input", "r").readlines()
calories = []
for thing in inputInfo:
    if thing != '\n':
        calories.append(thing[:-1])
    else:
        calories.append('#')
sumList = []
sum = 0
for calorie in calories:
    if calorie != '#':
        sum += int(calorie)
    else:
        sumList.append(sum)
        sum = 0

sumList.sort()
top3Sum = sumList[-1] + sumList[-2] + sumList[-3]
print(top3Sum)

