happiness = list(map(int, input().split()))
factor = int(input())
happiness_factor = [x * factor for x in happiness]
happiness_middle = sum(happiness_factor) / len(happiness)
avg_happiness = len([x for x in happiness_factor if x >= happiness_middle])

if avg_happiness >= len(happiness) / 2:
    print(f"Score: {avg_happiness}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {avg_happiness}/{len(happiness)}. Employees are not happy!")


# happiness = input().split()
# factor = int(input())
# happiness_factor = list(map(lambda x: int(x) * factor, happiness))
# filtered = list(filter(lambda x: x >= sum(happiness_factor) / len(happiness_factor), happiness_factor))
#
# if len(filtered) >= len(happiness) / 2:
#     print(f"Score: {len(filtered)}/{len(happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")
