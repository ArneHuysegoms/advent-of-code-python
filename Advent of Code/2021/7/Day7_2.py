import math


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


def getStepCost(index):
    accumulated = 0
    count = 0
    for i in range(index):
        count += accumulated + 1
        accumulated += 1
    return count


def getFuelCost(list, median):
    count = 0
    for i in list:
        count += getStepCost(abs(i - median))
    return count


def findSolution(list):
    input = list[0]
    inputList = [int(s) for s in input.strip().split(',')]
    average1 = math.ceil(cal_average(inputList))
    average2 = math.floor(cal_average(inputList))
    one = getFuelCost(inputList, average1)
    two = getFuelCost(inputList, average2)
    if one < two:
        return one
    else:
        return two


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
