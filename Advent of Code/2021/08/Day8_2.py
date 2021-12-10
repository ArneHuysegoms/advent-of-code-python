import numpy as np


def diffCharCount(word, characters):
    count = 0
    for char in characters:
        if char not in word:
            count += 1
    return count


def containsAllChars(word, characters):
    for char in characters:
        if char not in word:
            return False
    return True


def updateSignalMapping(signalMappings, inputListSplit):
    for signal in inputListSplit:
        if len(signal) == 2:  # can only be 1
            if signalMappings[1] == '':
                signalMappings[1] = "".join(sorted(signal))
        if len(signal) == 3:  # can only be 7
            if signalMappings[7] == '':
                signalMappings[7] = "".join(sorted(signal))
        if len(signal) == 4:  # can only be 4
            if signalMappings[4] == '':
                signalMappings[4] = "".join(sorted(signal))
        if len(signal) == 7:  # can only be 8
            if signalMappings[8] == '':
                signalMappings[8] = "".join(sorted(signal))
        if len(signal) == 6:  # can be 0, 6, 9
            if signalMappings[4] != '':
                if signalMappings[9] == '':
                    if containsAllChars(signal, signalMappings[4]):
                        signalMappings[9] = "".join(sorted(signal))
            if signalMappings[4] != '' and signalMappings[1] != '':
                if signalMappings[0] == '':
                    if not containsAllChars(signal, signalMappings[4]):
                        if containsAllChars(signal, signalMappings[1]):
                            signalMappings[0] = "".join(sorted(signal))
            if signalMappings[4] != '' and signalMappings[1] != '':
                if signalMappings[6] == '':
                    if not containsAllChars(signal, signalMappings[4]):
                        if not containsAllChars(signal, signalMappings[1]):
                            signalMappings[6] = "".join(sorted(signal))
        if len(signal) == 5:  # can be 2, 3, 5,
            if signalMappings[1] != '':
                if signalMappings[3] == '':
                    if containsAllChars(signal, signalMappings[1]):
                        signalMappings[3] = "".join(sorted(signal))
            if signalMappings[9] != '' and signalMappings[6] != '':
                if signalMappings[2] == '':
                    if diffCharCount(signal, signalMappings[9]) == 2 and diffCharCount(signal, signalMappings[6]) == 2:
                        signalMappings[2] = "".join(sorted(signal))
                if signalMappings[5] == '':
                    if diffCharCount(signal, signalMappings[9]) == 1 and diffCharCount(signal, signalMappings[6]) == 1:
                        signalMappings[5] = "".join(sorted(signal))
    return signalMappings


def findSolution(list):
    count = 0
    signalMappings = [''] * 10
    signalMappingsNpOld = np.array(signalMappings)
    for input in list:
        [inputList, outputList] = [s for s in input.split(' | ')]
        outputListSplit = [x for x in outputList.split(' ')]
        inputListSplit = [x for x in inputList.split(' ')]
        signalsChanged = True
        while signalsChanged:
            signalMappings = updateSignalMapping(signalMappings, inputListSplit)
            signalMappingsNp = np.array(signalMappings)
            if np.array_equal(signalMappingsNp, signalMappingsNpOld):
                signalsChanged = False
            signalMappingsNpOld = signalMappingsNp
        outputtxt = ''
        for output in outputListSplit:
            outputtxt += str(signalMappings.index("".join(sorted(output))))
        signalMappings = [''] * 10
        count += int(outputtxt)

    return count


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
