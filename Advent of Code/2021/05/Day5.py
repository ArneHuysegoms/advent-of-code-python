def isDiagonal(x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    return False

def markPath(x1, y1, x2, y2, diagram):
    if x1 == x2:
        if y1 < y2:
            diagram[y1][x1] += 1
            return markPath(x1, y1 + 1, x2, y2, diagram)
        if y1 > y2:
            diagram[y2][x1] += 1
            return markPath(x1, y1, x2, y2 + 1, diagram)
        if y1 == y2:
            diagram[y1][x1] += 1
            return diagram
    else:
        if y1 == y2:
            if x1 < x2:
                diagram[y1][x1] += 1
                return markPath(x1 + 1, y1, x2, y2, diagram)
            if x1 > x2:
                diagram[y1][x2] += 1
                return markPath(x1, y1, x2 + 1, y2, diagram)
            if x1 == x2:
                diagram[y1][x1] += 1
                return diagram
        else:
            if isDiagonal(x1, y1, x2, y2):
                if x1 < x2 and y1 < y2:
                    diagram[y1][x1] += 1
                    return markPath(x1+1, y1+1, x2, y2, diagram)
                if x1 < x2 and y1 > y2:
                    diagram[y1][x1] += 1
                    return markPath(x1+1, y1-1, x2, y2, diagram)
                if x1 > x2 and y1 < y2:
                    diagram[y1][x1] += 1
                    return markPath(x1-1, y1+1, x2, y2, diagram)
                if x1 > x2 and y1 > y2:
                    diagram[y1][x1] += 1
                    return markPath(x1-1, y1-1, x2, y2, diagram)
    return diagram


def countPath(diagram):
    count = 0
    for i in diagram:
        for j in i:
            if j > 1:
                count += 1
    return count


def findSolution(list):
    width = height = 1000
    diagram = [[0] * width for _ in range(height)]
    for i in list:
        [point1, point2] = i.split(' -> ', 1)
        [x1, y1] = point1.split(',')
        [x2, y2] = point2.split(',')
        diagram = markPath(int(x1), int(y1), int(x2), int(y2), diagram)
    return countPath(diagram)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
