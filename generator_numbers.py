
import re

def generator_numbers(text):
    pattern = r'\b\d+\.\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text, func):
    return sum(func(text))
