inputInfo = open("day10/input", "r").readlines()
width = 40
height = 6
mapMen = []
screen = []
numbers = []
number = 1
for i in range(height):
    number += 40
    numbers.append(number)
cycle = 1
endCycle = cycle
x = 1
current = inputInfo.pop(0)
addx = 0
run = True
line = ""
while run:
    if cycle >= endCycle:
        x += addx
        mapMen.clear()
        for item in range (width):
            mapMen.append(".")
        mapMen[(x-1)%width], mapMen[x%width], mapMen[(x+1)%width] = "#", "#", "#"
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
        screen.append(line)
        line = ""
    line += mapMen[(cycle-1)%width]
    cycle += 1
screen.append(line)
for item in screen:
    print(item)
    