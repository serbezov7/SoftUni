lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height
volume_lt = volume / 1000

fill_volume = percent / 100
total_lt = volume_lt * (1 - fill_volume)

print(total_lt)
