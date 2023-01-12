population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

needed = sum([minimum_wealth - x for x in population if x < minimum_wealth])
available = sum([x - minimum_wealth for x in population if x - minimum_wealth > 0])

if available >= needed:
    for people in population:
        if people < minimum_wealth:
            difference = minimum_wealth - people
            index_min = population.index(people)
            population[index_min] += difference
            max_population = max(population)
            index_max = population.index(max_population)
            if population[index_max] - difference >= minimum_wealth:
                population[index_max] -= difference
            else:
                difference_to_subtract = population[index_max] - minimum_wealth
                population[index_max] - difference_to_subtract
    print(population)
else:
    print("No equal distribution possible")
