# Learn the basics of lists

# Use [ ] and CSV
fruits = ['apple', 'banana', 'mango']
print(fruits, type(fruits))
# Use INDEX notation: begins with '0'
print(f'First element is {fruits[0]}')
print(f'Second element is {fruits[1]}')
# print(f'Nth element is {fruits[10]}')  # keep track of indexes
print(f'Last element is {fruits[2]}')
print(f'Last element is {fruits[-1]}') # negative index

# Use the len() to get the number of elements
print(f'fruits, has {len(fruits)} elements')

more_fruits = ['lime', 'cherry']
# Add two lists
all_fruits = fruits + more_fruits
print(f'All fruits {all_fruits}')
# Multiplication
many_fruits = fruits * 3
print(f'Many fruits {many_fruits}')

# Define a list from "scratch"
grades = [] # empty list
print(grades)
# grades = list() # list constructor
# Add elements to a list with: append()
grades.append(89)
print(grades)
grades.append(87)
grades.append(92)
print(grades)
print(f'The sum of the elements is: {sum(grades)}') # sum() all elements

# Calculate the average of grades
average = sum(grades)/len(grades)
print(f'The avg of grades is: {average}')
print(f'Max grade: {max(grades)}')
print(f'Min grade: {min(grades)}')