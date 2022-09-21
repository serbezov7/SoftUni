budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())

price_video_card = video_cards * 250
price_cpu = cpu * (price_video_card * 0.35)
price_ram = ram * (price_video_card * 0.1)

total_sum = price_video_card + price_cpu + price_ram
if video_cards > cpu:
    total_sum = total_sum * 0.85
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
