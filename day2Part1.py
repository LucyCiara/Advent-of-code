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
        enemyPoints += 1
    elif enemy[i] == 'B':
        enemyPoints += 2
    elif enemy[i] == 'C':
        enemyPoints += 3

    if hero[i] == 'X':
        heroPoints += 1
    elif hero[i] == 'Y':
        heroPoints += 2
    elif hero[i] == 'Z':
        heroPoints += 3

    if (enemy[i] == 'A' and hero[i] == 'X') or (enemy[i] == 'B' and hero[i] == 'Y') or (enemy[i] == 'C' and hero[i] == 'Z'):
        enemyPoints += 3
        heroPoints += 3
    elif (enemy[i] == 'A' and hero[i] == 'Z') or (enemy[i] == 'B' and hero[i] == 'X') or (enemy[i] == 'C' and hero[i] == 'Y'):
        enemyPoints += 6
    elif (enemy[i] == 'A' and hero[i] == 'Y') or (enemy[i] == 'B' and hero[i] == 'Z') or (enemy[i] == 'C' and hero[i] == 'X'):
        heroPoints += 6

print(f"Enemy: {enemyPoints}")
print(f"Hero: {heroPoints}")