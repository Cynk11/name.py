# This program says hello and asks for my name.
print('Hello there!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print()
print('Do you know Python?')
answer = input()
print('Ohh okay, so ' + answer)

# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
print('Take a guess.') # There are four spaces in front of print.
guess = input()
guess = int(guess)

guessesTaken = guessesTaken + 1

if guess < number:
print('Your guess is too low.') # There are eight spaces in front
of print.

if guess > number:
