def calculateOffspring(days):
    totalcount = 0
    childCount = int((days-2) / 7)
    totalcount += childCount
    if childCount > 0:
        for child in range(1,childCount):
            totalcount += calculateOffspring(days-2 - ((child) * 7))
    return totalcount


def calculatePopulationAfterDays(initialstate, days):
    totalcount = 0
    for i in initialstate:
        print(i)
        if i < days:
            firstChildDaysLeft = days - (i+1) #days left when parent is back at 6
            childCount = int(firstChildDaysLeft / 7) + 1 #number of children the parent will have
            totalcount += childCount
            if childCount > 0:
                for child in range(childCount):
                    totalcount += calculateOffspring(firstChildDaysLeft - (child * 7))
    return totalcount + len(initialstate)


def findSolution(list):
    fishOccurences = []
    for i in list:
        fishList = [s for s in i.strip().split(',')]
        fishOccurencesMap = map(i.count, '012345678')
        fishOccurences = [item for item in fishOccurencesMap]

    print(fishOccurences)
    for day in range(256):
        toAdd = [0] * 9
        for index in range(len(fishOccurences)):
            if index == 0:
                toAdd[len(fishOccurences)-1] += fishOccurences[index]
                toAdd[6] += fishOccurences[index]
            else:
                toAdd[index-1] += fishOccurences[index]
        fishOccurences = toAdd
        print(fishOccurences)
    return sum(fishOccurences)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
