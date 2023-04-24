inputInfo = open("day11/input", "r").readlines()
monkeys = {}
old, new = 0, 0
factorList = []
for line in inputInfo:
    if line[:6] == "Monkey":
        monkeys.update({line[:-2]: {"Activity": 0}})
    elif line[2:10] == "Starting":
        monkeys[list(monkeys)[-1]].update({line[2:16]: eval(f"[{line[18:-1]}]")})
    elif line[2:11] == "Operation":
        monkeys[list(monkeys)[-1]].update({line[2:11]: f"{line[13:-1]}"})
    elif line[2:6] == "Test":
        monkeys[list(monkeys)[-1]].update({line[2:6]: f"new%{line[21:-1]} == 0"})
        factorList.append(int(line[21:-1]))
    elif line[4:11] == "If true":
        monkeys[list(monkeys)[-1]].update({"If true": f"M{line[23:-1]}"})
    elif line[4:12] == "If false":
        monkeys[list(monkeys)[-1]].update({"If false": f"M{line[24:-1]}"})
commonFactor = 1
for factor in factorList:
    commonFactor *= factor
for i in range(10000):
    for key in monkeys:
        for ii in range(len(monkeys[key]["Starting items"])):
            monkeys[key]["Activity"] += 1
            old = monkeys[key]["Starting items"].pop(0)
            exec(monkeys[key]["Operation"])
            while new > commonFactor:
                new = new%commonFactor
            if eval(monkeys[key]["Test"]):
                monkeys[monkeys[key]["If true"]]["Starting items"].append(new)
            else:
                monkeys[monkeys[key]["If false"]]["Starting items"].append(new)
    # print(f"round {i+1}")
    # for key in monkeys:
    #     print(monkeys[key]["Starting items"])
    # print()
# sortOfDic = {}
sortOfList = []
for key in monkeys:
    sortOfList.append(monkeys[key]["Activity"])
    # sortOfDic.update({str(monkeys[key]["Activity"]): key})
sortOfList.sort()
print(sortOfList[-1] * sortOfList[-2])