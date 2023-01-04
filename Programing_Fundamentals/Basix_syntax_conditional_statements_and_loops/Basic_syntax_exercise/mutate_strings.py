first_string = input()
second_string = input()
last_string = first_string
for word in range(1, len(first_string) + 1):
    left_part = second_string[:word]
    right_part = first_string[word:]
    mutated_string = left_part + right_part
    if last_string != mutated_string:
        last_string = mutated_string
        print(last_string)
