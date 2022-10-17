town = input()
sales = float(input())
commission = 0
valid_town = True
valid_sales = True

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
    else:
        valid_sales = False
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13
    else:
        valid_sales = False
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    else:
        valid_sales = False
else:
    valid_town = False

if valid_sales and valid_town:
    total_commission = sales * commission
    print(f"{total_commission:.2f}")
else:
    print("error")








# town = input()
# sales = float(input())
# commission = 0
#
# if town == "Sofia":
#     if 0 <= sales <= 500:
#         commission = 0.05
#     elif 500 < sales <= 1000:
#         commission = 0.07
#     elif 1000 < sales <= 10000:
#         commission = 0.08
#     elif sales > 10000:
#         commission = 0.12
# elif town == "Varna":
#     if 0 <= sales <= 500:
#         commission = 0.045
#     elif 500 < sales <= 1000:
#         commission = 0.075
#     elif 1000 < sales <= 10000:
#         commission = 0.10
#     elif sales > 10000:
#         commission = 0.13
# elif town == "Plovdiv":
#     if 0 <= sales <= 500:
#         commission = 0.055
#     elif 500 < sales <= 1000:
#         commission = 0.08
#     elif 1000 < sales <= 10000:
#         commission = 0.12
#     elif sales > 10000:
#         commission = 0.145
# if commission == 0:
#     print("error")
# else:
#     total_commission = sales * commission
#     print(f"{total_commission:.2f}")
#
