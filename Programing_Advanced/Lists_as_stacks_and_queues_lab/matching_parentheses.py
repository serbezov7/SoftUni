expression = input()

indices = []

for i in range(len(expression)):
    if expression[i] == "(":
        indices.append(i)
    elif expression[i] == ")":
        current = indices.pop()
        print(expression[current: i + 1])
