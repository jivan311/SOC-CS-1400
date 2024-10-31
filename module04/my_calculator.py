# Create a basic four-point calculator
ADD = 1
SUBTRACT = 2
DIVIDE = 3
MULTIPLY = 4
OPERATORS = ['?', '+', '-', '/', '*']

# Capture two input floats from the user
number1 = float(input('Enter a number '))
number2 = float(input('Enter another number '))

# Present a menu of choices: 
menu = """Select an operation
        1) Add          3) Divide
        2) Subtract     4) Multiply
        """
choice = int(input(menu))

# Based on previous choice, execute operation
if choice == ADD:
    result = number1 + number2
elif choice == SUBTRACT:
    result = number1 - number2
elif choice == DIVIDE:
    # TODO: Check for divide by zero
    result = number1 / number2
elif choice == MULTIPLY:
    result = number1 * number2

# show the result
# Build final message
if choice >= ADD and choice <= MULTIPLY:   # Valid choice
    result_msg = f"""The result of:
        {number1} {OPERATORS[choice]} {number2}
        is {result}"""
else:  # Invalid choice
    result_msg = 'Unsupported Operation'

print(result_msg)