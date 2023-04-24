inputInfo = open("day1/input", "r").readlines()
calories = []
for line in inputInfo:
    if line != '\n':
        calories.append(line[:-1])
    else:
        calories.append('#')
sumList = []
sum = 0
for thing in calories:
    if thing != '#':
        sum += int(thing)
    else:
        sumList.append(sum)
        sum = 0

#Here I realized I could get this result using an easier method, which I employed in the second part of this task
big = 0
for sum in sumList:
    if sum > big:
        big = sum
print(big)

