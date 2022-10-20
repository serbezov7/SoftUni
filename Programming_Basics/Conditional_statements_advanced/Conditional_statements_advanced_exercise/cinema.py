screening_type = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
price = 0
if screening_type == "Premiere":
    price = 12
elif screening_type == "Normal":
    price = 7.50
elif screening_type == "Discount":
    price = 5
total_income = price * capacity
print(f"{total_income:.2f}")

