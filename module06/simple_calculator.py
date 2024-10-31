# A simple four point calculator
# It supports add, subtract, divide, multiply
# of two elements

EXIT = 0
ADD = 1
SUBTRACT = 2
DIVIDE = 3
MULTIPLY = 4
MODULUS = 5 
N_EXPONENT = 6
OPERATORS = ['?', '+', '-', '/', '*']

def take_user_input():
    # Take two integers as input
    number1 = int(input('Enter an integer: '))
    number2 = int(input('Enter another integer: '))
    # Return them as a tuple to the caller
    return number1, number2


def print_menu():
    # Print menu
    menu = """Select an operation
            1) Add          3) Divide
            2) Subtract     4) Multiply
            5) Modulus      6) N-Exponent
            0) Exit
            """
    choice = int(input(menu))
    # TODO: Validate input. 

    # return selected operation to the caller
    return choice


def execute_operation(choice, number1, number2):
    # Based on previous choice, execute operation
    total = 0
    if choice == ADD:
        total = add_numbers(number1,number2)
    elif choice == SUBTRACT:
        total = sub_numbers(number1,number2)
    elif choice == DIVIDE:
        total = div_numbers(number1,number2)
    elif choice == MULTIPLY:
        total = mul_numbers(number1,number2)
    elif choice == MODULUS:
        total = mod_numbers(number1,number2)
    elif choice == N_EXPONENT:
        total = exponent_numbers(number1,number2)
    else:
        print('Invalid choice')
    
    print(f'The total is {total}')
   

def add_numbers(number1, number2):
    total = number1 + number2
    return total


def sub_numbers(number1, number2):
    return number1 - number2


def div_numbers(number1, number2):
    # TODO: Check for divide by zero
    return number1/number2


def mul_numbers(number1, number2):
    return number1*number2


def mod_numbers(number1, number2):
    return number1 % number2


def exponent_numbers(number1, number2):
    # ** is the nth power
    return number1**number2


# Starting Point
# Program "Driver"
def main():
    # TASK: Keep it going until user quits
    while(True):
        choice = print_menu()
        # if not choice:
        if choice == EXIT:
            break
        num1, num2 = take_user_input()
        execute_operation(choice, num1, num2)
        # Task: Ask user if they want to do it again
    print('Thank you for using the super calculator')


if __name__ == '__main__':
    # Call main function
    main()