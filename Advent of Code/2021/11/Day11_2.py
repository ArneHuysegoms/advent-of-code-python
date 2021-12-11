def getNeighbors(list, x, y):
    neighbors = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1], [x - 1, y - 1], [x - 1, y + 1], [x + 1, y - 1],
                 [x + 1, y + 1]]
    relevantNeighbors = []
    for [i, j] in neighbors:
        if not (i < 0 or i == len(list) or j < 0 or j == len(list)):
            relevantNeighbors.append([i, j])
    return relevantNeighbors


def calculateNeighborFlashes(list, x, y):
    neighborsToIncrement = getNeighbors(list, x, y)
    for [i, j] in neighborsToIncrement:
        if [i,j] not in alreadyFlashed:
            list[j][i] = list[j][i] + 1
            if list[j][i] > 9:
                alreadyFlashed.append([i,j])
                list[j][i] = 0
                calculateNeighborFlashes(list, i, j)


def doStep(list):
    for y in range(len(list)):
        for x in range(len(list[0])):
            if [x,y] not in alreadyFlashed:
                list[y][x] = list[y][x] + 1
                if list[y][x] > 9:
                    alreadyFlashed.append([x,y])
                    list[y][x] = 0
                    calculateNeighborFlashes(list, x, y)
    allZeroes = True
    for i in list:
        print(i)
        if not all(v == 0 for v in i):
            allZeroes = False
    if allZeroes:
        return True
    else:
        return False


def findSolution(list):
    i = 1
    while True:
        print("--- STEP " + str(i))
        output = doStep(list)
        if output:
            break
        alreadyFlashed.clear()
        print(len(alreadyFlashed))
        print("--- END STEP " + str(i))
        i += 1
    return i


alreadyFlashed = []

with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    integerList = [[0]*10]*10
    for i in range(0,9):
        integerList[i] = [0]*10
    for y in range(len(list)):
        for x in range(len(list[0])):
            integerList[y][x] = int(list[y][x])
    print(findSolution(integerList))
