import re

command = input()
pattern = r"\%([A-Z][a-z]+)\%([^\|\$\%\.]*?)\<(\w+)\>([^\|\$\%\.]*?)\|([0-9]+)\|([^\|\$\%\.]*?)([0-9.]+[0-9])(?=\$)"
income = 0
while command != "end of shift":
    result = re.search(pattern, command)
    if result:
        price = int(result.group(5)) * float(result.group(7))
        print(f"{result.group(1)}: {result.group(3)} - {price:.2f}")
        income += price

    command = input()
print(f"Total income: {income:.2f}")