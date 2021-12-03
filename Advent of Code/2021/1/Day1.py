def findSolution(list):
    count = 0
    print(range(len(list)))
    for i in range(len(list)-3):
        if i != 0 and int(list[i]) + int(list[i+1]) + int(list[i+2]) < int(list[i+1]) + int(list[i+2]) + int(list[i+3]):
            count = count + 1
    return count


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    print(len(list))
    print(list)
    print(findSolution(list))


