open_tabs = int(input())
salary = int(input())
copy_salary = salary
for website in range (open_tabs):
    current_site = input()
    if current_site == "Facebook":
        copy_salary -= 150
    elif current_site == "Instagram":
        copy_salary -= 100
    elif current_site == "Reddit":
        copy_salary -= 50
    if copy_salary <=0:
        break
if copy_salary <= 0:
    print("You have lost your salary.")
else:
    print(copy_salary)
