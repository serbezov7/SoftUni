def group_checker(numbers):
    group = 10
    while len(numbers) > 0:
        list_of_numbers = []
        copy_numbers = numbers.copy()
        for number in copy_numbers:
            if number <= group:
                list_of_numbers.append(number)
                numbers.remove(number)
        print(f"Group of {group}'s: {list_of_numbers}")
        group += 10


init_numbers = list(map(int, input().split(", ")))
group_checker(init_numbers)
