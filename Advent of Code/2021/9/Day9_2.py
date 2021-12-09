coordinatesAlreadySeen = []

def getNeighbors(list, x, y):
    neighbors = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    for [i, j] in neighbors:
        if i < 0 or i == len(list) or j < 0 or j == len(list):
            neighbors.remove([i, j])
    return neighbors


def findNextMembersOfBasil(list, x, y):
    count = 0
    originalValue = int(list[y][x])
    neighbors = getNeighbors(list, x, y)
    for [i, j] in neighbors:
        if int(list[j][i]) != 9 and int(list[j][i]) > originalValue and [i,j] not in coordinatesAlreadySeen:
            count += 1
            coordinatesAlreadySeen.append([i, j])
            count += findNextMembersOfBasil(list, i, j)
    return count


def findBasilSize(list, x, y):
    size = 1
    originalValue = int(list[y][x])
    neighbors = getNeighbors(list, x, y)
    for [i, j] in neighbors:
        if int(list[j][i]) != 9 and int(list[j][i]) > originalValue and [i,j] not in coordinatesAlreadySeen:
            size += 1
            coordinatesAlreadySeen.append([i, j])
            size += findNextMembersOfBasil(list, i, j)
    return size


def isLowestPoint(list, x, y):
    if y == 0:
        if not int(list[y][x]) < int(list[y + 1][x]):
            return False
    if x == 0:
        if not int(list[y][x]) < int(list[y][x + 1]):
            return False
    if y == len(list) - 1:
        if not int(list[y][x]) < int(list[y - 1][x]):
            return False
    if x == len(list[0]) - 1:
        if not int(list[y][x]) < int(list[y][x - 1]):
            return False
    if len(list) - 1 > y > 0:
        if not int(list[y][x]) < int(list[y - 1][x]):
            return False
        if not int(list[y][x]) < int(list[y + 1][x]):
            return False
    if 0 < x < len(list[0]) - 1:
        if not int(list[y][x]) < int(list[y][x - 1]):
            return False
        if not int(list[y][x]) < int(list[y][x + 1]):
            return False
    return True


def addToArrayIfInThreeLargest(basilSize, threeLargest):
    indexOfLowest = -1
    diff = 0
    replaceLowest = False
    for i in range(len(threeLargest)):
        if basilSize > threeLargest[i]:
            currDiff = basilSize - threeLargest[i]
            if currDiff > diff:
                diff = currDiff
                indexOfLowest = i
                replaceLowest = True
    if replaceLowest:
        threeLargest[indexOfLowest] = basilSize
    return threeLargest


def findSolution(list):
    threeLargest = [0] * 3
    for y in range(len(list)):
        for x in range(len(list[0])):
            if isLowestPoint(list, x, y):
                coordinatesAlreadySeen.append([x, y])
                basilSize = findBasilSize(list, x, y)
                threeLargest = addToArrayIfInThreeLargest(basilSize, threeLargest)
    result = threeLargest[0] * threeLargest[1] * threeLargest[2]
    return result


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
