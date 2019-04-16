x = range(-10,11)

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    list_of_evens = [n for n in numbers if n > 0 and n % 2 == 0]

    print(list_of_evens)

filter_positive_even_numbers(x)