# Learn about strings

animal = 'dog'
print(animal, type(animal))

# Use string methods
print(animal, animal.capitalize()) # capitalize the first char
print(animal, animal.isdecimal())  # Test if the string is decimal
print(animal, animal.upper())  # make string ALL upper case

# Operators on strings
first_name = 'Waldo'
last_name = 'Weber'
full_name = first_name + ' ' + last_name
print(f'First name:{first_name}')
print(f'Last name:{last_name}')
print(f'Full name:{full_name}')
# Use formatted strings: f'{}'
w_number = 'W123456789'
full_name_new = f'{first_name} {last_name}, ID:{w_number}'
print(f'Full name:{full_name_new}')
# Declare strings with: 
# Single ''    # prefer way
# Double ""
# Triple """""" # Multi line strings
single_tick = 'This is a string'
double_tick = "This is a string"
triple_tick = """This is a string"""

# Multiplication
team = 'Real Madrid'
team_ucl = team * 15
print(team_ucl)
team_number_chars = len(team_ucl) # count number of elements
print(f'team_ucl is {team_number_chars} chars long')