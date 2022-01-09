import random

name = input("What is your name?:")
print("Good Luck!!", name)
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathmatics', 'player', 'condition', 'reverse',
         'water', 'board', 'geeks']
word = random.choice(words)
print("guess the characters:")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed = failed + 1
    if failed == 0:
        print("You Win:))")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses = guesses + guess
    if guess not in word:
        turns = turns - 1
        print("Wrong")
        print("You have", +turns, 'more guesses')
        if turns == 0:
            print("You Loose!!")
