import os

file_path = os.path.abspath('Advent-Of-Code-2023/Input/Day_01.txt')

SumOfLines=0

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()

        if line:
 
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            else:
   
                first_digit = None

   
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            else:
                last_digit = None
            combined_digits = first_digit + last_digit
            SumOfLines+= int(combined_digits)
print("Sum Part 1:", SumOfLines)




##### PART TWO
SumOfLines=0

with open(file_path, 'r') as file:
    for line in file:

        line = line.replace('one', 'one1one')
        line = line.replace('two', 'two2two')
        line = line.replace('three', 'three3three')
        line = line.replace('four', 'four4four')
        line = line.replace('five', 'five5five')
        line = line.replace('six', 'six6six')
        line = line.replace('seven', 'seven7seven')
        line = line.replace('eight', 'eight8eight')
        line = line.replace('nine', 'nine9nine')








        line = line.strip()
        

        if line:

            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            else:

                first_digit = None


            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            else:
                last_digit = None

            combined_digits = first_digit + last_digit

            SumOfLines+= int(combined_digits)
print("Sum Part 2:", SumOfLines)
