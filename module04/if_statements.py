# Test IF statements
PASSING_GRADE = 74

grade = int(input('Enter your current grade: '))
print(f'The grade is: {grade}')

# If the grade values is > PASSING_GRADE
if grade > PASSING_GRADE:
    print(f'You are passing the class')
    print('You are doing awesome!')
else:
    print(f'You are NOT passing the class')
    print('You need to contact your instructor')

# Done with program
print('Adios amigo')