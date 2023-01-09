def data_types(type, num):
    if type == "int":
        num = int(num)
        return num * 2
    elif type == "real":
        num = float(num)
        return f"{num * 1.5:.2f}"
    else:
        return f"${num}$"


current_type = input()
current_num = input()
print(data_types(current_type, current_num))



