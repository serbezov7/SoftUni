characters = input().split(", ")
my_dict = {key: ord(key) for key in characters}
print(my_dict)

# my_dict = {"a": 65, "k": 98, "f": 88, "z": 88}
# print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))