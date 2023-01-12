current_version = list(map(int, input().split(".")))
current_version[-1] += 1

for version in range(len(current_version) - 1, -1, -1):
    if current_version[version] > 9:
        current_version[version] = 0
        if current_version[version - 1] >= 0:
            current_version[version - 1] += 1
print(".".join(str(x) for x in current_version))

# current_version = list(map(int, input().split(".")))
#
# for version in range(len(current_version) - 1, -1, -1):
#     current_version[version] += 1
#     if current_version[version] > 9:
#         current_version[version] = 0
#         current_version[version - 1] += 1
#         if current_version[version - 1] > 9:
#             current_version[version - 1] = 0
#             current_version[version - 2] += 1
#     print(".".join(str(x) for x in current_version))
#     break