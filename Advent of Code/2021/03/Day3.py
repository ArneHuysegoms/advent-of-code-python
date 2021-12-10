import numpy as np


def split(word):
    return [int(char) for char in word]


def getSum(list, sum):
    for i in list:
        if len(sum) == 0:
            sum = split(i)
        else:
            new = split(i)
            sum = np.add(sum, new)
    return sum


def filterByValueOnIndex(list, index, value):
    newlist = []
    for i in list:
        if int(i[index]) == int(value):
            newlist.append(i)
    return newlist


def findSolution(list):
    listCopy = list
    sum = getSum(listCopy, [])
    for e in range(len(sum)):
        sum = getSum(listCopy, [])
        if sum[e] >= len(listCopy) / 2:
            listCopy = filterByValueOnIndex(listCopy, e, '1')
        else:
            listCopy = filterByValueOnIndex(listCopy, e, '0')
        if len(listCopy) == 1:
            break
    mostcommon = listCopy[0]
    print('mostcommon ' + mostcommon)

    listCopy = list
    for e in range(len(sum)):
        sum = getSum(listCopy, [])
        if sum[e] >= len(listCopy) / 2:
            listCopy = filterByValueOnIndex(listCopy, e, '0')
        else:
            listCopy = filterByValueOnIndex(listCopy, e, '1')
        if len(listCopy) == 1:
            break
    leastcommon = listCopy[0]
    print('leastcommon ' + mostcommon)
    return int(mostcommon, 2) * int(leastcommon, 2)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
