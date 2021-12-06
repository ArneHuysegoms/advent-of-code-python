def calculateSpawnedFish(fish, days):
    spawnedFish = [fish]
    for day in range(days):
        toSpawnCount = 0
        for index in range(len(spawnedFish)):
            if spawnedFish[index] != 0:
                spawnedFish[index] -= 1
            else:
                spawnedFish[index] += 6
                toSpawnCount += 1
        for newFish in range(toSpawnCount):
            spawnedFish.append(8)
    return len(spawnedFish)-1


def calculatePopulationAfterDays(initialstate, days):
    totalcount = 0
    for i in initialstate:
        totalcount += calculateSpawnedFish(i, days)
    return totalcount + len(initialstate)


def findSolution(list):
    completeFishList = []
    for i in list:
        fishList = [int(s) for s in i.strip().split(',')]
        completeFishList.append(fishList)
    print(completeFishList)
    return calculatePopulationAfterDays(completeFishList[0], 80)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
