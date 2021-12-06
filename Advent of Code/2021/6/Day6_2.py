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
