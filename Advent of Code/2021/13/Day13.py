import matplotlib.pyplot as plt


def foldPaper(number, axis, inputList):
    result = []
    for (x,y) in inputList:
        if axis == "x" and x > number:
            nx = 2 * number - x
            ny = y
        elif axis == "y" and y > number:
            ny = 2 * number - y
            nx = x
        else:
            nx = x
            ny = y
        if (nx, ny) not in result:
            result.append((nx, ny))
    inputList.clear()
    for r in result:
        inputList.append(r)


def drawResult(resultList):
    for (x,y) in resultList:
        plt.scatter(int(x), -int(y))
    plt.show()


def findSolution(inputList, foldList):
    foldListActual = []
    for fold in foldList:
        foldListSplit = fold.split(' ')
        foldListActual.append(foldListSplit[2])
    tupleList = []
    for input in inputList:
        [x1, y1] = input.split(',')
        tupleList.append((int(x1), int(y1)))
    for foldi in foldListActual:
        [axis, number] = foldi.split("=")
        foldPaper(int(number), axis, tupleList)
    result = set(tupleList)
    drawResult(result)
    return len(result)


def splitArray(list):
    inputListt = []
    foldListt = []
    for i in range(len(list)):
        if list[i] == '':
            inputListt = list[:i]
            foldListt = list[i + 1:]
    return [inputListt, foldListt]


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    [inputList, foldList] = splitArray(list)
    print(findSolution(inputList, foldList))
