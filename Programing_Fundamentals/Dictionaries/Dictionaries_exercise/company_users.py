command = input()
company_dict = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_dict.keys():
        company_dict[company_name] = [employee_id]
    else:
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)
    command = input()

for company in company_dict.keys():
    print(f"{company}")
    for employees in company_dict[company]:
        print(f"-- {employees}")
