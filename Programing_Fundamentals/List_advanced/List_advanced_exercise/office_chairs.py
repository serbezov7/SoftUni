def check_rooms(room):
    needed_chairs = 0
    chairs_left = 0
    for current_room in range(1, room + 1):
        chairs, visitors = input().split()
        difference = int(visitors) - len(chairs)
        if len(chairs) < int(visitors):
            needed_chairs += difference
            print(f"{difference} more chairs needed in room {current_room}")
        else:
            chairs_left += abs(difference)
    return needed_chairs, chairs_left


number_of_rooms = int(input())
total_needed_chairs, total_chairs_left = check_rooms(number_of_rooms)
if total_chairs_left >= total_needed_chairs:
    print(f"Game On, {total_chairs_left} free chairs left")
    
