# Introduction
print("Instruction: This program squares even numbers and cubes odd numbers from 'integer.txt'"
      "creating a new text file with the results.")
# Read numbers from integers.txt file
with open("integers.txt", "r") as new_file:
    integers = [int(line.strip()) for line in new_file]
# Separate the data/ get the even and odd numbers
even_numbers = [num for num in integers if num % 2 == 0]
odd_numbers = [num for num in integers if num % 2 != 0]
# Calculation: Square all the even numbers
squared_even = [number ** 2 for number in even_numbers]
# Calculations: Cube all the odd numbers
cubed_odd = [number ** 3 for number in odd_numbers]
# Creating squared even text file
with open("double.txt", "a") as new_file:
    for square in squared_even:
        new_file.write(f'{square}\n')
# Creating cubed odd text file
# Successful Execution Message
