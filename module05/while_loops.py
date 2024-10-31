# First look at while Loops

school = 'Weber State University'
# Print string 5 times, using while loop

counter = 5

while counter:  # while counter != 0, do the loop
    print(f'{counter}) {school}')
    counter = counter - 1


# Task: Create a loop that ask for the number GUESS
# Stay in the loop until the number GUESS is entered
GUESS = 9 # constant
number = 0
while number != GUESS:
    number = int(input('Guess which number I am thinking between 0 and 10: '))
    # TODO: Give Hints to the user: go higher, go lower
    # TODO: Change your GUESS value every time (automatically)
    # TODO: Have a fixed number of tries
    # TODO: Given Hints: super cold,cold, warmer, too hot, etc
    # TODO: Add level to the game: range, number of tries, etc

print(f'You got it')


print('Done')