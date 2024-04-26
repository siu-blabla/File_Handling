# Introduction
print("This program writes multiple line of text into a text file 'mylife.txt'")
# Open the text file
with open("mylife.txt", "a") as file:

    # Looping
    while True:
        enter_line = input("Enter Line: ")
        file.write(enter_line + "\n")
        more_lines = input("Are there more lines y/n? ")
        if more_lines != 'y':
            break
        print("Thank you for using this program. Come again sometime!")
