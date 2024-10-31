# Use for loop in collections: list, dictionaries, strings, etc

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print each element, one per line
# print 1st element
index = 0
print(f'{index}) element: {numbers[index]}')
index = index + 1
print(f'{index}) element: {numbers[index]}')
index = index + 1
print(f'{index}) element: {numbers[index]}')

# Use a loop to access each element of my list
index = 0  # reset/start your counter/index
for number in numbers:
    print(f'{index}) the super element: {number}')
    index = index + 1

print('Done!')