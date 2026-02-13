"""
Program Name: Lab5_AntLampaca-1.py
Author Antoni Labsz
Purpose: Dice roll simulation that rolls two dice, which then gives a term corresponding to a table of dice combination names
Starter Code: None
Date: February 12, 2026
"""

import random

def get_term(die1, die2) :
    total = die1 + die2

    if die1 == die2 == 1:
        return "Snake Eyes"
    elif {die1, die2} == {1, 2}:
        return "Ace Caught a Deuce"
    elif die1 == die2 == 2:
        return "Little Joe from Kokomo"
    elif {die1, die2} == {1, 4}:
        return "Little Phoebe"
    elif {die1, die2} == {2, 3}:
        return "Little Phoebe"
    elif {die1, die2} == {3, 3}:
        return "Jimmy Hicks from the Sticks"
    elif {die1, die2} == {1, 6}:
        return "Six Ace"
    elif {die1, die2} == {4, 4}:
        return "Eighter from Devatur"
    elif {die1, die2} == {3, 6}:
        return "Nina from Pasadena"
    elif {die1, die2} == {4, 5}:
        return "Nina from Pasadena"
    elif {die1, die2} == {5, 5}:
        return "Puppy Paws"
    elif {die1, die2} == {5, 6}:
        return "Six Five no Jive"
    elif {die1, die2} == {6, 6}:
        return "Boxcars"
    else:
        return "no Special Term"

while True:

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

    term = get_term(die1, die2)
    print("Term: ", term)

    choice = input("Roll again? (y/n): ").lower()
    if choice != 'y':
        print("thanks for playing")
        break