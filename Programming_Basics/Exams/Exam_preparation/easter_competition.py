count_of_easter_cakes = int(input())
best_cooker = ""
points_best_cooker = 0

for cakes in range(count_of_easter_cakes):
    name_of_the_cooker = input()
    current_points = 0

    command = input()
    while command != "Stop":
        value_for_the_cake = int(command)
        current_points += value_for_the_cake

        command = input()
    print(f"{name_of_the_cooker} has {current_points} points.")
    if current_points > points_best_cooker:
        points_best_cooker = current_points
        best_cooker = name_of_the_cooker
        print(f"{name_of_the_cooker} is the new number 1!")
print(f"{best_cooker} won competition with {points_best_cooker} points!")
