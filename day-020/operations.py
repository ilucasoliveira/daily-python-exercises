def sum_number(list_number):
    return sum(list_number)

def the_biggest(list_number):
    return max(list_number)

def even_numbers(list_number):
    even = [number for number in list_number if number % 2 == 0]
    return sorted(even)