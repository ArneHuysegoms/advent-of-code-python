def median(lst):
    lst.sort()  # Sort the list first
    if len(lst) % 2 == 0:  # Checking if the length is even
        # Applying formula which is sum of middle two divided by 2
        return (lst[len(lst) // 2] + lst[(len(lst) - 1) // 2]) / 2
    else:
        # If length is odd then get middle value
        return lst[len(lst) // 2]

def getFuelCost(list, median):
    count = 0
    for i in list:
        count += abs(i - median)
    return count

def findSolution(list):
    input = list[0]
    inputList = [int(s) for s in input.strip().split(',')]
    print(inputList)
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
