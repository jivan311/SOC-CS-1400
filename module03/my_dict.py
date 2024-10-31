# Learn the basics of dictionaries

# days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
days_of_month = {'jan':31, 'feb':28, 'mar':31,
                 'apr':30, 'may':31, 'jun':30,
                 'jul':31, 'aug':31, 'sep':30,
                 'oct':31, 'nov':30, 'dec':31}

print(days_of_month, type(days_of_month))
# Print one element
print(f"You have {days_of_month['nov']} days in november")
# Add an element. It will create it if it does not exists
days_of_month['neb'] = 32
print(f'After adding an element {days_of_month}')
# Update a value
days_of_month['feb'] = 29
print(f'After updating an element {days_of_month}')