from collections import deque

string_colors = deque(input().split())
founded_colors = []
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while string_colors:
    first = string_colors.popleft()
    second = string_colors.pop() if string_colors else ''

    for color in first + second, second + first:
        if color in colors:
            founded_colors.append(color)
            break
    else:
        string_colors.insert(len(string_colors) // 2, first[:-1]) if first[:-1] else None
        string_colors.insert(len(string_colors) // 2, second[:-1]) if second[:-1] else None
        # first = first[:-1]
        # second = second[:-1]
        # if first:
        #     string_colors.insert(len(string_colors) // 2, first)
        # if second:
        #     string_colors.insert(len(string_colors) // 2, second)

for color in founded_colors:
    if color in secondary_colors.keys():
        if not secondary_colors[color].issubset(set(founded_colors)):
            founded_colors.remove(color)
        # if we use list for secondary colors:
        # for sec_color in secondary_colors[color]:
        #     if sec_color not in founded_colors:
        #         founded_colors.remove(color)
print(founded_colors)
