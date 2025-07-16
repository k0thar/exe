# -*- coding: utf-8 -*-
import random

guess=-1
count=0
winn=False

def get_a_guess():
    guess=int(input('Give me your guess: '))
    return guess

computer_number=random.randint(1, 20)

def answer(g,c):
    if c<g:
        return 'Too high'
    elif g<c:
        return 'too low'
    return 'you won'

def win(g,c):
    return g==c

def finish(n,c):
    print(f'my number was {c} and you guessed it in {n} guesses')

def con():
    inp=input("wanna continue? Y/N: ").upper()
    if inp=='Y':
        return True,False
    
    return False,True   

continue_game=True

while (continue_game):
    while (not winn):
        count+=1
        guess=get_a_guess()
        print (answer(guess,computer_number))
        winn=win(guess,computer_number)
    finish(count,computer_number)
    continue_game,winn=con()