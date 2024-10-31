# Iterate over a range of integers
import random

# Case 1: One parameter, upper_limit
# Range: from 0 to < upper_limit
print('Range with one value')
upper_limit = 10
for index in range(upper_limit):
    print(index)

# Case 2: Two parameter, lower_limit AND upper_limit
# Range: from lower_limit to < upper_limit
print('Range with two values')
lower_limit = 3
upper_limit = 10
for index in range(lower_limit, upper_limit):
    print(index)

# Case 3: Three parameter, lower_limit, upper_limit, step_size
# Range: from lower_limit to < upper_limit, increments of step_size
print('Range with three values')
lower_limit = 20
upper_limit = 100
steps = 10
for index in range(lower_limit, upper_limit, steps):
    print(index)

# Task: Update each value by 2 using range()
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f'Original list {numbers}')
upper_limit = len(numbers) # get the number of elements of the list
for index in range(upper_limit):   # index >=0 AND index < upper_limit
    print(f'Index {index} = {numbers[index]}')
    numbers[index] += 2  # increment by 2
print(f'After list {numbers}')
# Another way
for index in range(len(numbers)):   # index >=0 AND index < len(numbers)
    numbers[index] += 2  # increment by 2
print(f'After 2 list {numbers}')

# Decrement by 5 the odd index values
# Increment by 7 the even index values
ODD = 1
for index in range(len(numbers)):   # index >=0 AND index < len(numbers)
    if index % 2 == ODD:   # odd?
        numbers[index] -= 5
    else:   # even
        numbers[index] += 7
print(f'After 3 list {numbers}')

# Generate a list of 10 integers with random numbers 
rand_numbers = []  # empty list
# Repeat 10 times
for index in range(10):
    # Generate a random number between 10 and 50
    number = random.randint(10,50)
    # Add it to the list
    rand_numbers.append(number)
# Print data
print(f'Random numbers are: {rand_numbers}')

