products = input().split()
searched_products = input().split()
my_dict = {}

for element in range(0, len(products), 2):
    key = products[element]
    value = products[element + 1]
    my_dict[key] = value

for product in searched_products:
    if product in my_dict.keys():
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
