# Introduction
while True:
    print('Instruction: This program creates new text files and categorizes '
          'the numbers from "numbers.txt" into even and odd numbers.')
    print('-------------------------------------------------------------')
    looping = input('Do you wish to continue? (y/n): ')
    print('-------------------------------------------------------------')
    if looping == 'y':
        print('Execution completed.\nThank you for using this program!')
        break
    else:
        print('End of program ...........')
        break

# Read integers from "number.txt" file
with open("numbers.txt", "r") as new_file:
    numbers = new_file.read().split()
    numbers = (int(num) for num in numbers)     # Assigning numbers to integer

# Separate even and odd
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Write the even numbers to a separate text file (even.txt)
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# Write the odd numbers to a separate text file (odd.txt)
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")
