# Print the information of ALL students
# from a list of names


def student_name(name):
    print(f'Student name here: {name}')


def school_info(school_name, school_mascot):
    print(f'Your school is: {school_name}')
    print(f'Your school mascot: {school_mascot}')


# Starting Point
# Program "Driver"
def main():
    # List of student names
    names = ['Waldo', 'Maria', 'John', 'Sarah', 'Dipah']
    # loop over names
    for name in names:
        student_name(name)
    # Dictionary of schools and mascots
    schools = {'WSU':'Waldo', 
                'UU': 'Utes',
                'UT': 'Long horns',
                'UCLA': 'Rams'}
    # loop over dict and print school info            
    for key, value in schools.items():
        school_info(key, value)


if __name__ == '__main__':
    # Call main function
    main()
