initial_deck = input().split()
shuffles = int(input())
deck_half = len(initial_deck) // 2

for shuffle in range(shuffles):
    final_deck = []
    first_half = initial_deck[:deck_half]
    second_half = initial_deck[deck_half:]
    for index in range(len(first_half)):
        final_deck.append(first_half[index])
        final_deck.append(second_half[index])
    initial_deck = final_deck
print(initial_deck)
