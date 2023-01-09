def loading_bar(num):
    if num == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{num}% [{num // 10 * '%'}{'.' * ((100 - num) // 10)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
