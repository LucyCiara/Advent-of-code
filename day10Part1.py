inputInfo = open("day10/input", "r").readlines()
numbers = []
number = -20
for i in range(6):
    number += 40
    numbers.append(number)
cycle = 1
endCycle = cycle
x = 1
sums = []
current = inputInfo.pop(0)
addx = 0
run = True
while run:
    if cycle >= endCycle:
        x += addx
        if current[:4] == "addx":
            endCycle = cycle + 2
            addx = int(current[5:-1])
        elif current[:4] == "noop":
            endCycle = cycle + 1
            addx = 0
        if len(inputInfo) > 0:
            current = inputInfo.pop(0)
        else:
            run = False
    if cycle in numbers:
        sums.append(x*cycle)
    cycle += 1
sum = 0
for item in sums:
    sum += item
print(sum)
    