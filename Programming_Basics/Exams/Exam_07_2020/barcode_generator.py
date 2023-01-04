start_number = int(input())
finish_number = int(input())

start_fourth = start_number % 10
start_number = start_number // 10
start_third = start_number % 10
start_number = start_number // 10
start_second = start_number % 10
start_number = start_number // 10
start_first = start_number

end_fourth = finish_number % 10
finish_number = finish_number // 10
end_third = finish_number % 10
finish_number = finish_number // 10
end_second = finish_number % 10
finish_number = finish_number // 10
end_first = finish_number

for i in range(start_first, end_first + 1):
    for j in range(start_second, end_second + 1):
        for k in range(start_third, end_third + 1):
            for l in range(start_fourth, end_fourth + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")