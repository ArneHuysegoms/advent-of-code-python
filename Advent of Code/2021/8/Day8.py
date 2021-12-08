def findSolution(list):
    count = 0
    signalMappings = [''] * 10
    for input in list:
        [inputList, outputList] = [s for s in input.split(' | ')]
        outputListSplit = [x for x in outputList.split(' ')]
        for output in outputListSplit:
            if len(output) == 2:
                if signalMappings[1] == '':
                    signalMappings[1] = "".join(sorted(output))
                count += 1
            if len(output) == 3:
                if signalMappings[7] == '':
                    signalMappings[7] = "".join(sorted(output))
                count += 1
            if len(output) == 4:
                if signalMappings[4] == '':
                    signalMappings[4] = "".join(sorted(output))
                count += 1
            if len(output) == 7:
                if signalMappings[0] == '':
                    signalMappings[0] = "".join(sorted(output))
                count += 1
    return count


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
