name_company = input()
count_adult_tickets = int(input())
count_child_tickets = int(input())
price_adult_ticket = float(input())
service_tax = float(input())
price_child_ticket = price_adult_ticket * 0.3
all_price_adult = price_adult_ticket + service_tax
all_price_child = price_child_ticket + service_tax
total_price = all_price_adult * count_adult_tickets + all_price_child * count_child_tickets
income = total_price * 0.2
print(f"The profit of your agency from {name_company} tickets is {income:.2f} lv.")