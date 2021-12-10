def findSolution(list):
    horpos = 0
    depth = 0
    aim = 0
    for i in list:
        [direction, units] = i.split(' ', 1)
        if direction == 'forward':
            horpos += int(units)
            depth += (int(units)*aim)
        if direction == 'up':
            aim -= int(units)
        if direction == 'down':
            aim += int(units)
    return depth * horpos


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    print(len(list))
    print(list)
    print(findSolution(list))


