print("Welcome to the calculator program! This program is a simple calculator based on user input.\n Let's start!")

def split_expression(expression):
    for operator in "+-*/":
        if operator in expression:
            num_1, num_2 = expression.split(operator)
            return int(num_1), operator, int(num_2)

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

operation = input("What is the desired operation? E.g: 100/2\n")

while operation!= 'n':
    number_1, expression_operator, number_2 = split_expression(operation)

    if expression_operator=='+':
        print(f"= {sum(number_1, number_2)}")
    elif expression_operator=='-':
        print(f"= {subtract(number_1, number_2)}")
    elif expression_operator == '*':
        print(f"= {multiply(number_1, number_2)}")
    elif expression_operator == '/':
        print(f"= {divide(number_1, number_2)}")

    operation = input("Do you wish to continue?\nType 'n' to end program\nor insert new operation.\n")

print("Thanks for using the calculator!")
