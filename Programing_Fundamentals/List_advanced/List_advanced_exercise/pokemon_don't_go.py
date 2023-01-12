pokemons = list(map(int, input().split()))
sum_removed = 0

while len(pokemons) > 0:
    index = int(input())
    removed_element = 0
    if index < 0:
        removed_element = pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
    elif index > len(pokemons) - 1:
        removed_element = pokemons.pop(-1)
        pokemons.insert(len(pokemons), pokemons[0])
    else:
        removed_element = pokemons.pop(index)
    sum_removed += removed_element
    for index, current_digit in enumerate(pokemons):
        if current_digit <= removed_element:
            pokemons[index] += removed_element
        elif current_digit > removed_element:
            pokemons[index] -= removed_element
print(sum_removed)
