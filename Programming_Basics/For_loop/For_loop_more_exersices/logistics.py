loads = int(input())
all_loads_tons = 0
price_minibus = 0
price_truck = 0
price_train = 0
microbus_load = 0
truck_load = 0
train_load = 0

for load in range(loads):
    tons = int(input())
    all_loads_tons += tons
    if tons <= 3:
        price_minibus += tons * 200
        microbus_load += tons
    elif tons <= 11:
        price_truck += tons * 175
        truck_load += tons
    else:
        price_train += tons * 120
        train_load += tons
average_price = (price_minibus + price_truck + price_train) / all_loads_tons
percent_microbus = microbus_load / all_loads_tons * 100
percent_truck = truck_load / all_loads_tons * 100
percent_train = train_load / all_loads_tons * 100

print(f"{average_price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
