def add_car(cars_dict_, number_of_cars_):
    for _ in range(number_of_cars_):
        current_car = input().split("|")
        car_ = current_car[0]
        mileage_ = int(current_car[1])
        fuel_ = int(current_car[2])
        cars_dict_[car_] = [mileage_, fuel_]
    return cars_dict_


def drive(cars_dict_, car_, distance_, needed_fuel_):
    if cars_dict_[car_][1] > needed_fuel_:
        cars_dict_[car_][0] += distance_
        cars_dict_[car_][1] -= needed_fuel_
        print(f"{car_} driven for {distance_} kilometers. {needed_fuel_} liters of fuel consumed.")
        if cars_dict_[car_][0] >= 100000:
            del cars_dict_[car_]
            print(f"Time to sell the {car_}!")
    else:
        print("Not enough fuel to make that ride")
    return cars_dict_


def refuel(cars_dict_, car_, fuel_):
    initial_fuel = cars_dict_[car_][1]
    cars_dict_[car_][1] += fuel_
    if cars_dict_[car_][1] > 75:
        cars_dict_[car_][1] = 75
        difference = 75 - initial_fuel
        print(f"{car_} refueled with {difference} liters")
    else:
        print(f"{car_} refueled with {fuel_} liters")
    return cars_dict_


def revert(cars_dict_, car_, kilometers_):
    cars_dict_[car_][0] -= kilometers_
    if cars_dict_[car_][0] < 10000:
        cars_dict_[car_][0] = 10000
    else:
        print(f"{car_} mileage decreased by {kilometers_} kilometers")
    return cars_dict_


number_of_cars = int(input())
cars_dict = {}
cars_dict = add_car(cars_dict, number_of_cars)

command = input().split(" : ")
while command[0] != "Stop":
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        needed_fuel = int(command[3])
        cars_dict = drive(cars_dict, car, distance, needed_fuel)
    elif command[0] == "Refuel":
        fuel = int(command[2])
        cars_dict = refuel(cars_dict, car, fuel)
    elif command[0] == "Revert":
        kilometers = int(command[2])
        cars_dict = revert(cars_dict, car, kilometers)

    command = input().split(" : ")

for car in cars_dict.keys():
    print(f"{car} -> Mileage: {cars_dict[car][0]} kms, Fuel in the tank: {cars_dict[car][1]} lt.")
