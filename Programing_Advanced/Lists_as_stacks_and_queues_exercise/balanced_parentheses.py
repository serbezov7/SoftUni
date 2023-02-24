my_queue = list(input())
open_brackets = []

for bracket in my_queue:
    if bracket in "{[(":
        open_brackets.append(bracket)
    else:
        if open_brackets:
            current_bracket = open_brackets.pop()
            if current_bracket + bracket not in "(){}[]":
                print("NO")
                break
        else:
            print("NO")
            break
else:
    print("YES")
