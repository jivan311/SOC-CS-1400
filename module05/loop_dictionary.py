# Loop over dictionaries

teams = {'Real Madrid':'Spain',
         'Inter': 'Italy',
         'Bayer M.': 'Germany',
         'Chelsea': 'England',
         'Real Salt Lake': 'USA'
         }
        
# Loop over dictionary
# By default, a for loop will take the
# key, NOT the value associate to the key
for key in teams:
    print(f'Key: [{key}] Value: {teams[key]}')

# Get only the values
for value in teams.values():
    print(f'Values: [{value}]')

# Get both the values AND keys
for value in teams.items():
    print(f'{value} type {type(value)}')
    print(f'Key: [{value[0]}] Value: {value[1]}')

# Use tuple unpacking
for key, value in teams.items():
    print(f'Key: [{key}] Value: {value}')