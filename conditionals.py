import random
guess = int(input('Guess a number: '))
print(guess)

magic_number = random.randint(0, 10)

if guess == magic_number:
    print('Congratulations! You won the lottery.')
else:
    print('Too bad! It was %d' % (magic_number))
