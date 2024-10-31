# Test IF statements
PASSING_GRADE = 75
A_GRADE = 90

B_GRADE_LOW = 80
B_GRADE_HIGH = 89

C_GRADE_LOW = PASSING_GRADE
C_GRADE_HIGH = 79

D_GRADE_LOW = 70
D_GRADE_HIGH = PASSING_GRADE - 1 

E_GRADE_LOW = 60
E_GRADE_HIGH = 69

F_GRADE_LOW = 50
F_GRADE_HIGH = 59


grade = int(input('Enter your current grade: '))
print(f'The grade is: {grade}')

# If the grade values is >= PASSING_GRADE
if grade >= PASSING_GRADE:
    print(f'You are passing the class')
    print('You are doing awesome!')
    # Implement Letter Grade logic
    if grade >= A_GRADE:
        print(f'You have an "A"')
    elif grade >= B_GRADE_LOW and grade <= B_GRADE_HIGH:
        print(f'You have an "B"')
    else:
        print(f'You have an "C"')
else:
    print(f'You are NOT passing the class')
    if grade >= D_GRADE_LOW and grade <= D_GRADE_HIGH:
        print(f'You have an "D". You have time')
    elif grade >= E_GRADE_LOW and grade <= E_GRADE_HIGH:
        print(f'You have an "E". Last Call')
    elif grade >= F_GRADE_LOW and grade <= F_GRADE_HIGH:
        print(f'You have an "F"')
        print('You need to contact your instructor')
    else:
        print('No hope :(')


# Done with program
print('Adios amigo')
