def sort_func(numbers):
    positive = [num for num in numbers if num > 0]
    negative = [num for num in numbers if num < 0]

    print(sum(negative))
    print(sum(positive))

    if sum(positive) > abs(sum(negative)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
sort_func(numbers)
