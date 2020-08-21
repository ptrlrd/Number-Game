import random

name = input('Hello! What is your name? \n')
secret_number = random.randint(1,20)
print('Okay {}, I am thinking of a number between 1 and 20.\nYou will have 7 tries to guess the right number!'.format(name))

for guess_taken in range(1,7):

    if guess_taken <= 5:
        print("You have {} out of 7 tries!".format(guess_taken))
    elif guess_taken:
        print("This is your final time to guess a number!")

    while True: # Excludes non-integer answers from the loop
        try:
            guess = int(input('Take a guess. \n'))

            if guess < secret_number:
                print('Your guess is too low!')
                break
            elif guess > secret_number:
                print('Your guess is too high!')
                break
            else:
                break
        except ValueError:
            print("Sorry, you did not enter a number!")

if guess == secret_number:
    print('Great job {}! You guessed my number which was {}! It took you {} tries.'.format(name,secret_number,guess_taken))

if guess != secret_number:
    print('Unfortunately, the number I was thinking of {}!'.format(secret_number))
