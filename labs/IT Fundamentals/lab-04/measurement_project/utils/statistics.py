def calculate_average(numbers):
    l = len(numbers)
    sum = 0
    for n in numbers:
        sum += n
    return sum / l if l > 0 else 0

def find_min(numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    return min

def find_max(numbers):
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n
    return max