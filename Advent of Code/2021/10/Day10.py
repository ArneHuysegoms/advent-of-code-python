

def findSolution(list):
    count = 0
    errorFrequencies = [0]*4
    count_parentheses = 0
    count_curly = 0
    count_braces = 0
    count_biggersmallerthan = 0
    stack = []
    for i in list:
        for char in i:
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

            # if count_parentheses < 0:
            #     errorFrequencies[0] += 1
            #     break
            # if count_braces < 0:
            #     errorFrequencies[1] += 1
            #     break
            # if count_curly < 0:
            #     errorFrequencies[2] += 1
            #     break
            # if count_biggersmallerthan < 0:
            #     errorFrequencies[3] += 1
            #     break
        count_parentheses = 0
        count_curly = 0
        count_braces = 0
        count_biggersmallerthan = 0
        stack = []
    count = errorFrequencies[0]*3 + errorFrequencies[1]*57 + errorFrequencies[2]*1197 + errorFrequencies[3]*25137
    return count


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    print(findSolution(list))
