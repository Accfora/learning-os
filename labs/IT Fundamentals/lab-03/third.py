def calculate_average(measurements):
    n = len(measurements)
    sum = 0
    for n in measurements:
        sum += n
    return sum / n if n > 0 else 0

def find_minimum(measurements):
    min = measurements[0]
    for n in measurements:
        if n < min:
            min = n
    return min

def find_maximum(measurements):
    max = measurements[0]
    for n in measurements:
        if n > max:
            max = n
    return max

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for n in measurements:
        if n > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i, n in enumerate(measurements):
        if n == target:
            return i
    return -1

def analyze_measurements(measurements):
    avg = calculate_average(measurements)
    return find_minimum(measurements), find_maximum(measurements), avg

measurements = [4, 6, 2, 8, 1, 5, 15, 3, 7, 9]
min, max, avg = analyze_measurements(measurements)

print(f'len = {len(measurements)}')
print(f'min = {min}')
print(f'max = {max}')
print(f'avg = {avg}')
print(f'count above avg = {count_above_average(measurements)}')

to_find = int(input("Enter a value to find: "))
print(f'index = {find_value(measurements, to_find)}')