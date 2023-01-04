total_days = int(input())
days_won = 0
days_lose = 0
total_price = 0
for days in range(total_days):
    price = 0
    win_games = 0
    lose_games = 0
    command = input()
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            price += 20
            win_games += 1
        else:
            lose_games += 1
        command = input()
    if win_games > lose_games:
        price *= 1.10
        days_won += 1
    else:
        days_lose += 1
    total_price += price

if days_won > days_lose:
    total_price *= 1.20
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_price:.2f}")