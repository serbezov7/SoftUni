from collections import deque

players_queue = deque(input().split())
tosses = int(input())
counter = 0

while len(players_queue) > 1:
    counter += 1
    player = players_queue.popleft()
    if tosses == counter:
        counter = 0
        print(f"Removed {player}")
    else:
        players_queue.append(player)
print(f"Last is {players_queue[0]}")
