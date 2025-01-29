import os
import sys
import math
import random

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

def calculate_square_roots(numbers):
    return [math.sqrt(num) for num in numbers]

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def write_numbers_to_file(filename, numbers):
    with open(filename, "w") as file:
        file.write("\n".join(map(str, numbers)))

def read_numbers_from_file(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

def main():
    numbers = generate_random_numbers(10, 1, 100)
    square_roots = calculate_square_roots(numbers)
    directory = "output"
    create_directory(directory)
    file_path = os.path.join(directory, "numbers.txt")
    write_numbers_to_file(file_path, numbers)
    read_numbers = read_numbers_from_file(file_path)
    print("Original Numbers:", read_numbers)
    print("Square Roots:", square_roots)

if __name__ == "__main__":
    main()
