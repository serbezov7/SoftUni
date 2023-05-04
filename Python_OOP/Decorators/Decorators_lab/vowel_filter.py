def vowel_filter(function):
    def wrapper():
        vowels = ["a", "e", "u", "i", "o", "y"]
        result = [v for v in function() if v in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
