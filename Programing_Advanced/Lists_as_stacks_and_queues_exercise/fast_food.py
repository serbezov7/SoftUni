from collections import deque

total_food = int(input())
my_queue = deque(int(x) for x in input().split())
my_queue_copy = my_queue.copy()
print(max(my_queue))

while my_queue_copy:
    current_order = my_queue_copy.popleft()
    if total_food - current_order >= 0:
        total_food -= current_order
        my_queue.popleft()

    else:
        print(f"Orders left: {' '.join(str(x) for x in my_queue)}")
        break
else:
    print("Orders complete")
