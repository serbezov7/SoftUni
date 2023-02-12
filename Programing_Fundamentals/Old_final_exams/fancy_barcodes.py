import re

barcodes_count = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for _ in range(barcodes_count):
    barcode = input()
    result = re.search(pattern, barcode)
    group = ""
    if result:
        for char in result.group():
            if char.isdigit():
                group += char
        if group == "":
            group = "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
