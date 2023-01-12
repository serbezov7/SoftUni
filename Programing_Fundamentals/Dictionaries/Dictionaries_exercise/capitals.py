countries = input().split(", ")
cities = input().split(", ")

countries_dict = {countries[index]: cities[index] for index in range(len(countries))}
# countries_dict = dict(zip(countries, cities))
for country, capital in countries_dict.items():
    print(f"{country} -> {capital}")