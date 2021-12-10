def getFuelCost(crabs, median):
    count = 0
    for i in crabs:
        count += abs(i - median)
    return count


def findSolution(list):
    input = list[0]
    inputList = [int(s) for s in input.strip().split(',')]
    #16,1,2,0,4,2,7,1,2,14
    #0,1,1,2,2,2,4,7,14,16
    inputList.sort()
    median = inputList[len(inputList) // 2]
    return getFuelCost(inputList, median)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
