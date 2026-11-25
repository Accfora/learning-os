def calculate_average(numbers):
    total = 0
    if len(numbers) == 0:
        raise ValueError("List is empty")
    for number in numbers:
        total += number
    return total / len(numbers)


def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        max_value = max(max_value, number)
    return max_value


def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


def analyze(numbers):
    if not numbers:
        raise ValueError("List is empty")
    total = 0
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        total += number
        max_value = max(max_value, number)
        min_value = min(min_value, number)
    return min_value, max_value, total / len(numbers)
