import re
keys = list(map(int, input().split()))
command = input()
treasure_pattern = "&(.+?)&"
coordinates_pattern = "<(.+?)>"

while command != "find":
    index = 0
    while index in range(len(keys)):
        message = ""
        treasure = ""
        coordinates = ""
        for letter in command:
            message += chr(ord(letter) - keys[index])
            if index + 1 not in range(len(keys)):
                index = 0
                continue
            index += 1
        treasure = re.findall(treasure_pattern, message)
        coordinates = re.findall(coordinates_pattern, message)
        print(f"Found {''.join(treasure)} at {''.join(coordinates)}")
        break

    command = input()
