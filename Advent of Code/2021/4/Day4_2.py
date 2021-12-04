def isBingoRow(row, givenNumbers):
    for e in row:
        if e not in givenNumbers:
            return False
    return True


def findBingoInRows(board, givenNumbers):
    for row in board:
        if isBingoRow(row, givenNumbers):
            return True
    return False


def findBingoInColumn(board, givenNumbers, index):
    for row in board:
        if row[index] not in givenNumbers:
            return False
    return True


def findBingoInColumns(board, givenNumbers):
    for i in range(len(board)):
        if findBingoInColumn(board, givenNumbers, i):
            return True
    return False


def findBingo(board, givenNumbers):
    if len(givenNumbers) < 5:
        return False
    if findBingoInColumns(board, givenNumbers) or findBingoInRows(board, givenNumbers):
        return True
    return False


def getSumOfAllUnmarkedNumbers(board, givenNumbers):
    sum = 0
    for row in board:
        for e in row:
            if e not in givenNumbers:
                sum += int(e)
    return sum


def findSolution(list):
    inputstream = []
    boards = []
    currentboard = []
    for line in list:
        if ',' in line:
            inputstream = line.split(',')
        else:
            if line == '':
                if not not currentboard:
                    boards.append(currentboard)
                    currentboard = []
            else:
                boardLine = line.split(' ')
                boardLine = [i for i in boardLine if i != '']
                currentboard.append(boardLine)
    boards.append(currentboard)
    currentNumberInput = []
    for number in inputstream:
        currentNumberInput.append(number)
        for board in boards:
            if findBingo(board, currentNumberInput):
                if len(boards) == 1:
                    return int(getSumOfAllUnmarkedNumbers(board, currentNumberInput)) * int(
                        currentNumberInput[len(currentNumberInput) - 1])
                boards.remove(board)
    return 0


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
