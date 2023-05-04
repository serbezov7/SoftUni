def even_odd_filter(**kwargs):
    result = {}
    if "even" in kwargs.keys():
        kwargs["even"] = [n for n in kwargs["even"] if n % 2 == 0]
    if "odd" in kwargs.keys():
        kwargs["odd"] = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))

    for key, value in sorted(kwargs.items(), key=lambda x: -len(x[1])):
        result[key] = value
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))