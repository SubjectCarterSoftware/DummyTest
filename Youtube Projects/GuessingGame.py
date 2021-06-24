import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry Guess Again to Low")
        elif guess > random_number:
            print("Sorry guess again to High")

    print(f"Yay you have guessed the random number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: 
            guess =random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} to high(H) or too low(L) or correct(c) !!!')
        if feedback == 'h':
            high = guess - 1     
        elif feedback == 'l':
            low = guess = 1
    print(f'Yay the computer guess your numeber, {guess}, correctly!!')

computer_guess(10)

exit()