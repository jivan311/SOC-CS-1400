# Update elements of a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f'Original list {numbers}')
# TODO: Increment each element of the list by 1
index = 0
# for _ in numbers:   # You may use the dummy '_' variable if you access elements by index
for number in numbers:
    # Access each element by index instead of value
    # print(f'{index}) the super element: {numbers[index]}')
    numbers[index] = numbers[index] + 1
    index = index + 1
print(f'After list {numbers}')
# Another way
index = 0
for number in numbers:
    numbers[index] = number + 1
    index = index + 1
print(f'After 2 list {numbers}')

# Another way
index = 0
for number in numbers:
    numbers[index] += 1 # increment current value by 1
    index += 1 # increment index
    # index++;  # C++ way to increment index
print(f'After 3 list {numbers}')
