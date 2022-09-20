deposit_amount = float(input())
deposit_months = int(input())
annual_percent = float(input())

interest = deposit_amount * (annual_percent / 100)
interest_month = interest / 12
total_sum=deposit_amount+(deposit_months*interest_month)
print(total_sum)
