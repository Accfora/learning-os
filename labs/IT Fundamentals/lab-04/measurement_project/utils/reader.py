def read_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = []
        for line in file:
            numbers.append(float(line.strip()))
    return numbers
