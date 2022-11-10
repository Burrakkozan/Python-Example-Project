import random
num =  random.randint(1, 10)

players_name = input('Hello! What is your name? ')
Whonum_of_guesses = 0   
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:'.format(players_name))

while Whonum_of_guesses < 3:
    guess = int(input())
    Whonum_of_guesses += 1
    if guess < num:
        print('Your estimate is too low, go up a little!')
    if guess > num:
       print('Your estimate is too high, go down a bit!')
    if guess == num:
        break
if guess == num:
    print('Congratulations! You guessed the number in {} guesses!'.format(players_name,Whonum_of_guesses ))
else:
    print('You have lost! The number I was thinking was {}.'.format(num))