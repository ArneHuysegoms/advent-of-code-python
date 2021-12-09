def isLowestPoint(list, x, y):
    if y == 0:
        if not int(list[y][x]) < int(list[y+1][x]):
            return False
    if x == 0:
        if not int(list[y][x]) < int(list[y][x+1]):
            return False
    if y == len(list)-1:
        if not int(list[y][x]) < int(list[y-1][x]):
            return False
    if x == len(list[0])-1:
        if not int(list[y][x]) < int(list[y][x-1]):
            return False
    if len(list)-1 > y > 0:
        if not int(list[y][x]) < int(list[y-1][x]):
            return False
        if not int(list[y][x]) < int(list[y+1][x]):
            return False
    if 0 < x < len(list[0])-1:
        if not int(list[y][x]) < int(list[y][x-1]):
            return False
        if not int(list[y][x]) < int(list[y][x+1]):
            return False
    return True



def findSolution(list):
    count = 0
    coordinates = []
    print(list)
    for y in range(len(list)):
        for x in range(len(list[0])):
            if isLowestPoint(list, x, y):
                print(list[y][x])
                count += int(list[y][x]) + 1
    return count


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
