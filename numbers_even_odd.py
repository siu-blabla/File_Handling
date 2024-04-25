# Introduction
print('Instruction: This program creates new text files and categorizes '
      'the numbers from "numbers.txt" into even and odd numbers.')

# Read integers from "number.txt" file
with open("numbers.txt", "r") as new_file:
    numbers = new_file.read().split()
    numbers = (int(num) for num in numbers)     # Assigning numbers to integer

# Separate even and odd
odd_numbers = (num for num in numbers if num % 2 == 1)
even_numbers = (num for num in numbers if num % 2 != 0)

# Write the even numbers to a separate text file (even.txt)
# Write the odd numbers to a separate text file (odd.txt)
