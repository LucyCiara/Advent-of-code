inputInfo = open("day6/input", "r").readline()
buffer = []
i = 0
run = True
while run and i < len(inputInfo):
    buffer.append(inputInfo[i])
    if len(buffer) > 14:
        buffer.pop(0)
        run = False
        for ii in range(len(buffer)):
            if buffer[ii] in buffer[:ii] or buffer[ii] in buffer[ii+1:]:
                run = True
    i += 1
print(i)