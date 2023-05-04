def math_operations(*args, **kwargs):
    result = []
    for i in range(len(args)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += args[i]
        elif key == "s":
            kwargs[key] -= args[i]
        elif key == "d":
            if args[i] != 0:
                kwargs[key] /= args[i]
        elif key == "m":
            kwargs[key] *= args[i]

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     numbers = deque(args)
#     result = []
#     while numbers:
#         for key in kwargs.keys():
#             if key == "a" and numbers:
#                 number = numbers.popleft()
#                 kwargs[key] += number
#             elif key == "s" and numbers:
#                 number = numbers.popleft()
#                 kwargs[key] -= number
#             elif key == "d" and numbers:
#                 number = numbers.popleft()
#                 if number > 0:
#                     kwargs[key] /= number
#             elif key == "m" and numbers:
#                 number = numbers.popleft()
#                 kwargs[key] *= number
#
#     for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
#         result.append(f"{key}: {value:.1f}")
#     return "\n".join(result)
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
