#!/usr/bin/python3
def calculator():
    print('you can calculate using two numbers and operator')
    number_1 = int(input('Enter your first number'))
    operator = input('''please type the math operator you wish to use
                        + for addition
                        - for subtraction
                        / for division
                        * for multiplication
                        ''')
    number_2 = int(input('Enter your second number'))

    if operator == '+':
        
        print(number_1 + number_2)

    elif operator == '*':
        print(number_1 * number_2)
    elif operator == '/':
        print(number_1 / number_2)
    elif operator == '-':
        print(number_1 - number_2)
calculator()
