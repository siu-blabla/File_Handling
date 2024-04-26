# Introduction
print("Instruction: This program squares even numbers and cubes odd numbers from 'integer.txt'"
      "creating a new text file with the results.")
# Read numbers from integers.txt file
with open("integers.txt", "r") as new_file:
    integers = [int(line.strip()) for line in new_file]
# Separate the data/ get the even and odd numbers
# Calculation: Square all the even numbers
# Calculations: Cube all the odd numbers
# Creating squared even text file
# Creating cubed odd text file
# Successful Execution Message
