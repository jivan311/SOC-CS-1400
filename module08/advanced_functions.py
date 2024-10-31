# Advanced Functions


def make_password(info):
    """Create a temp password

    Args:
        info (dict): user information

    Returns:
        str: temp password
    
    Note:   (first two characters) fname
            (last two characters) lname
            (all digits) age
    """
    password = info['fname'][0:2]   # from 0 to < 2 indexes
    password = password + info['lname'][-2:] # start at -2 until the end 
    password = password + str(info['age'])
    
    return password.lower()


def make_info(fname, lname, age):
    """Build a dictionary with the user info

    Args:
        fname (str): first name
        lname (str): last name
        age (int): age

    Returns:
        dict: User info
    """
    info = {}
    info['fname'] = fname
    info['lname'] = lname
    info['age'] = age
    
    return info


def all_needed_password(fname, lname, age):
    info = make_info(fname, lname, age)
    # Call you make_password()
    password = make_password(info)
    # return the value
    return password


# Positional Parameters are first
# Optional Parameters are last
def some_needed_password(fname, lname, age=18):
    info = make_info(fname, lname, age)
    # Call you make_password()
    return make_password(info)


def none_needed_password(fname='Waldo', lname='Weber', age=18):
    return make_password(make_info(fname, lname, age))


# Starting Point
# Program "Driver"
def main():
    # all_needed_password() # does not work
    # all_needed_password('Mario') # does not work
    # all_needed_password('Mario', 18) # does not work
    
    # You may use keyword arguments and avoid
    # the actual positional order
    passwd = all_needed_password(fname='Mario', lname='Weber', age=18) # does not work
    print(f'Your temp password is: [{passwd}]')
    passwd = all_needed_password(age=19, fname='Carlos', lname='Smith') # does not work
    print(f'Your temp password is: [{passwd}]')
    passwd = some_needed_password(fname='Maria', lname='Rodriguez') # does not work
    print(f'Your temp password is: [{passwd}]')
    passwd = none_needed_password() # does not work
    print(f'Your temp password is: [{passwd}]')


if __name__ == '__main__':
    # Call main function
    main()
