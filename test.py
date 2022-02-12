#Declare the variable
number1 = number2= result= new_num= 0
operator = ''

#initializing values for variable
try:
    number1=int(input('Insert your first number: '))
except:
    print('must be a number')

try:
    number2=int(input('Insert your second number: '))
except:
    print('must be a number')

operator= input('select the operator: ')
try:
    if operator == '+':
        result = number1 + number2
        print('{} + {} ='.format(number1,number2), result)
    elif operator == '-':
        result = number1 - number2
        print('{} - {} ='.format(number1,number2), result)
    elif operator == '*':
        result = number1 * number2
        print('{} * {} ='.format(number1,number2), result)
    elif operator == '/':
        result = number1 / number2
        print('{} / {} ='.format(number1,number2), result)
except:
    print('something was wrong')