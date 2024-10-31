# Write your first function


# Define function
def student_info():
    print(f'Inside {student_info.__name__}')
    name = 'Waldo Weber'
    print(f'Hi {name}')


# "Entry" point function
def main():
    print(f'Inside {main.__name__}')
    # Use/call it
    student_info()
    # Final msg
    print('Done')


# Execute main() if you are running
# the program directly
if __name__ == '__main__':
    # Run main function
    main()