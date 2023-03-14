intersection_set = set()

for _ in range(int(input())):
    data = input().split("-")
    first, second = [int(x) for x in data[0].split(",")]
    third, fourth = [int(x) for x in data[1].split(",")]

    first_set = set(range(first, second + 1))
    second_set = set(range(third, fourth + 1))

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(intersection_set):
        intersection_set = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in intersection_set)}] with length {len(intersection_set)}")
