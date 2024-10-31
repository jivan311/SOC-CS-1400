# Check Age Activities

ELEMENTARY_SCHOOL_AGE = 6
# MIDDLE_SCHOOL_AGE = 12
MIDDLE_SCHOOL_AGE = ELEMENTARY_SCHOOL_AGE + 6
HIGH_SCHOOL_AGE = MIDDLE_SCHOOL_AGE + 3
SCHOOL_AGE_MAX = 18
SCHOOL_AGE_MIN = 4

age = int(input('Enter your age: '))

# Check for school age, print school typ
if age >= SCHOOL_AGE_MIN and age <= SCHOOL_AGE_MAX:
    if age >= ELEMENTARY_SCHOOL_AGE and age < MIDDLE_SCHOOL_AGE:
        print('You are in elementary school')
    elif age >= MIDDLE_SCHOOL_AGE and age < HIGH_SCHOOL_AGE:
        print('You are in middle school')
    elif age >= HIGH_SCHOOL_AGE:
        print('You are in High school')
else:
    print('You are not in school')

print('Thank you')