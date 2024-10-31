# Iterate over strings

school = 'Weber State University in OGDEN UT 2024'

# Do you have a 'W' in string?
if 'W' in school:
    print(f'Your [{school}] string has the letter W')
else:
    print(f'Your [{school}] string does not have the letter W')
# How many vowel in string?
total_vowels = 0
for letter in school:
    # Count vowels, both Upper and Lower case
    if 'A' in letter or 'a' in letter or \
    'E' in letter or 'e' in letter or \
    'I' in letter or 'i' in letter or \
    'O' in letter or 'o' in letter or \
    'U' in letter or 'u' in letter :
        total_vowels += 1
print(f'1) Yours string has {total_vowels}')
# Another way
total_vowels = 0
for letter in school:
    # Count vowels, both Upper and Lower case
    if 'A' in letter.upper()  or \
    'E' in letter.upper() or \
    'I' in letter.upper() or \
    'O' in letter.upper() or \
    'U' in letter.upper():
        total_vowels += 1
print(f'2) Yours string has {total_vowels}')

# Another way
total_vowels = 0
vowels = 'AEIOU'
for letter in school:
    # Count vowels, both Upper and Lower case
    if letter.upper() in vowels:
        total_vowels += 1
print(f'3) Yours string has {total_vowels}')

# How many alpha characters in string?
# How many number characters in string?
total_letters = 0
total_digits = 0
total_other = 0
for letter in school:
    # Count vowels, both Upper and Lower case
    if letter.isalpha():
        total_letters += 1
    elif letter.isdigit():
        total_digits += 1
    else:
        total_other += 1
print(f'4) Yours string has {total_letters} letters')
print(f'4) Yours string has {total_digits} digits')
print(f'4) Yours string has {total_other} others')