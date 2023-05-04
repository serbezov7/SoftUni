rows, cols = [int(x) for x in input().split()]
word = input()

idx = 0
elements = [None] * cols
for row in range(rows):
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        elements[col] = word[idx % len(word)]
        idx += 1
    print("".join(elements))

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# word = list(input())
# word_copy = deque(word.copy())
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#     if row % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")

