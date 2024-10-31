# Print Student information


def student_name():
    print('Waldo Weber')


def school_info():
    print('Weber State University')
    print('located in Ogden UT')


def school_mascot():
    print('WSU has the wildcat')


# Starting Point
# Program "Driver"
def main():
    # Repeat the process three times
    for index in range(3):
        student_name() # call function
        #school_info()   # call function
        school_mascot()  # call function


if __name__ == '__main__':
    # Call main function
    main()
