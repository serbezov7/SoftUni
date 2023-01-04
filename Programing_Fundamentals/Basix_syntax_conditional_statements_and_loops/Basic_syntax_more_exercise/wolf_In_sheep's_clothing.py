animals = input().split(", ")
wolf_position = animals.index("wolf")
sheep_position = len(animals) - wolf_position - 1
if len(animals) - 1 == wolf_position:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
