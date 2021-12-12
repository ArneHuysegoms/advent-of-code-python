def visitedSmallCaveTwiceAlready(list):
    count = {}
    for item in list:
        count[item] = list.count(item)
    for item in count:
        if str.islower(item) and count[item] > 1:
            return True
    return False

def findPaths(paths, possibles):
    pathsToRemove = []
    pathsToAdd = []
    for path in paths:
        for possible in possibles:
            pathEnd = path.split(',')[-1]
            [begin, end] = possible.split(',')
            if not (str.islower(end) and end in path.split(',') and visitedSmallCaveTwiceAlready(path.split(','))):
                if begin == pathEnd:
                    pathsToRemove.append(path)
                    newPath = path
                    newPath += ',' + end
                    pathsToAdd.append(newPath)
        if len(pathsToAdd) == 0 and not path.split(',')[-1] == 'end':
            pathsToRemove.append(path)
    for p in set(pathsToRemove):
        paths.remove(p)
    for p in pathsToAdd:
        paths.append(p)
    print(len(paths))
    containsUnfinished = False
    for p in paths:
        if not p.split(',')[-1] == 'end':
            containsUnfinished = True
    if containsUnfinished:
        findPaths(paths, possibles)


def findSolution(list):
    paths = []
    possibles = []
    for i in list:
        [begin, end] = i.split('-')
        if begin == 'start':
            paths.append(begin + ',' + end)
        else:
            if end == 'start':
                paths.append(end + ',' + begin)
            else:
                if end == 'end':
                    possibles.append(begin + ',' + end)
                else:
                    if begin == 'end':
                        possibles.append(end + ',' + begin)
                    else:
                        possibles.append(begin + ',' + end)
                        possibles.append(end + ',' + begin)

    print(paths)
    findPaths(paths, possibles)
    result = len(paths)
    print('end')
    return result


alreadyFlashed = []

with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
