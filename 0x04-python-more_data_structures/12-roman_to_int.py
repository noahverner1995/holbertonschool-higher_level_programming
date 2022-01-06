#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or roman_string == None:     
        return 0
    values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}  
    """Convert from Roman numerals to an integer."""
    numbers = []
    for char in roman_string:
        numbers.append(values[char]) 
    total = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    return total + num2
