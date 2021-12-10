def findSolution(list):
    score = 0
    scoreList = []
    errorFrequencies = [0]*4
    count_parentheses = 0
    count_curly = 0
    count_braces = 0
    count_biggersmallerthan = 0
    stack = []
    for i in list:
        for index in range(len(i)):
            char = i[index]
            if char == '(':
                stack.append(char)
                count_parentheses += 1
            if char == ')':
                corresponding_char = stack.pop()
                if corresponding_char != '(':
                    errorFrequencies[0] += 1
                    break
                count_parentheses -= 1
            if char == '[':
                stack.append(char)
                count_braces += 1
            if char == ']':
                corresponding_char = stack.pop()
                if corresponding_char != '[':
                    errorFrequencies[1] += 1
                    break
                count_braces -= 1
            if char == '{':
                stack.append(char)
                count_curly += 1
            if char == '}':
                corresponding_char = stack.pop()
                if corresponding_char != '{':
                    errorFrequencies[2] += 1
                    break
                count_curly -= 1
            if char == '<':
                stack.append(char)
                count_biggersmallerthan += 1
            if char == '>':
                corresponding_char = stack.pop()
                if corresponding_char != '<':
                    errorFrequencies[3] += 1
                    break
                count_biggersmallerthan -= 1
            if index == len(i) - 1:
                nextelement = stack.pop()
                while True:
                    score = score * 5
                    if nextelement == '(':
                        score += 1
                    if nextelement == '[':
                        score += 2
                    if nextelement == '{':
                        score += 3
                    if nextelement == '<':
                        score += 4
                    if len(stack) == 0:
                        break
                    else:
                        nextelement = stack.pop()
                scoreList.append(score)
                score = 0
        count_parentheses = 0
        count_curly = 0
        count_braces = 0
        count_biggersmallerthan = 0
        stack = []
    scoreList = sorted(scoreList)
    return int(scoreList[len(scoreList) // 2])


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
