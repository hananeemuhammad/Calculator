"""
Program: Simple Calculator 
Author: Hananee Bueraheng
Simple calculator help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

while True:
      try:
            number_1=int(input("Insert the first number: "))
            if number_1 == isinstance(number_1, int):
                  break
      except ValueError:
            print('Invalid input, You must enter a number')
            continue

      
      operation = input('Please type in the math operation you would like to complete: ')
            
      try:
            number_2=int(input("Insert the second number: "))
            if number_2 == isinstance(number_2, int):
                  break
      except ValueError:
            print('Invalid input, You must enter a number')
            continue


      



      if operation == '+':
            # print('{} + {} = '.format(number_1, number_2))
            print('{} + {} = '.format(number_1, number_2) ,(number_1 + number_2))

      elif operation == '-':
            # print('{} - {} = '.format(number_1, number_2))
            print('{} - {} = '.format(number_1, number_2) ,(number_1 - number_2))

      elif operation == '*':
            # print('{} * {} = '.format(number_1, number_2))
            print('{} * {} = '.format(number_1, number_2) ,(number_1 * number_2))

      elif operation == '/':
            # print('{} / {} = '.format(number_1, number_2))
            print('{} / {} = '.format(number_1, number_2) ,(number_1 / number_2))


      else:
            print('You have not typed a valid operator, please run the program again.')

      next_calculation = input("Let's do next calculation? (yes/no): ")
      if next_calculation == "no":
          break
      else :
            continue