# Introduction
print('Instruction: This program reveals the student with the highest'
      'Grade Weighted Average (GWA) and their corresponding GWA.')
# Assign the variable
highest_general_weighted_average = float('inf')
name_of_student = ''
# Read the text file called, "student_data.txt"
with open("student_data.txt", "r") as file:
    datas = file.readlines()
# Identify the student with the highest GWA
for data in datas:      # Separate the data first
    name, general_weighted_average = data.strip().split(',')
    general_weighted_average = float(general_weighted_average)
# Get the highest result of GWA and the name of the student behind it.
