count_bitcoins = int(input())
count_yuans = float(input())
commission_percent = float(input())

bitcoins = count_bitcoins * 1168 / 1.95
yuans = count_yuans * 0.15 * 1.76 / 1.95

all = bitcoins + yuans
total_commission = 1 - (commission_percent / 100)
total = all * total_commission
print(f"{total:.2f}")