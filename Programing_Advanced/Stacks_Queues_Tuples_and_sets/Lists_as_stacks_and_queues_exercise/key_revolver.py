from collections import deque

bullet_price = int(input())
barrel_size = int(input())
init_barrel_size = barrel_size
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    intelligence -= bullet_price
    barrel_size -= 1
    if barrel_size == 0 and bullets:
        print("Reloading!")
        barrel_size = init_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")