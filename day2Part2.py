inputInfo = open("day2/input", "r").readlines()

enemy = []
hero = []
for item in inputInfo:
    enemy.append(item[0])
    hero.append(item[2])

enemyPoints = 0
heroPoints = 0

for i in range(len(enemy)):
    if enemy[i] == 'A':
        enemyPointGain = 1
    if enemy[i] == 'B':
        enemyPointGain = 2
    if enemy[i] == 'C':
        enemyPointGain = 3
    
    if hero[i] == 'X':
        if enemyPointGain != 1:
            heroPointGain = enemyPointGain-1
        else:
            heroPointGain = 3
        enemyPointGain += 6
    elif hero[i] == 'Y':
        heroPointGain = enemyPointGain
        heroPointGain += 3
        enemyPointGain += 3
    elif hero[i] == 'Z':
        if enemyPointGain != 3:
            heroPointGain = enemyPointGain+1
        else:
            heroPointGain = 1
        heroPointGain += 6
    heroPoints += heroPointGain
    enemyPoints += enemyPointGain

print(f"Hero: {heroPoints}")
print(f"Enemy: {enemyPoints}")