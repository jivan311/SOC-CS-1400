# Demo on basic use of Tuples

days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days_of_month, type(days_of_month))
# Access one element by: [index] notation
print(f'May has {days_of_month[4]} days')
# Use built-in functions as in list
print(f'The tuple has {len(days_of_month)} elements')

# Now convert this tuple() to a set()
unique_days_of_month = set(days_of_month)
print(f'Unique days of month {unique_days_of_month}')
print(f'The Tuple {days_of_month} has {len(unique_days_of_month)} unique values')
print(f'The Tuple {days_of_month} has {len(set(days_of_month))} unique values')

# Test for membership any collection: str(), list(), tuple(), set(), dict()
test = 30
result = test in days_of_month # get True or False
print(f'Does the {test} number exists in {days_of_month}?: {result}')
test = 36
result = test in days_of_month # get True or False
print(f'Does the {test} number exists in {days_of_month}?: {result}')
# Membership with reverse logic: not in
test = 30
result = test not in days_of_month # get True or False
print(f'Does the {test} number does not exists in {days_of_month}?: {result}')
test = 36
result = test not in days_of_month # get True or False
print(f'Does the {test} number does not exists in {days_of_month}?: {result}')
