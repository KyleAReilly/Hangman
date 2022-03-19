import random
import string
from words import words

# get word that doesnt have invalid characters
def getValidWord(words):
    word = random.choice(words) # Takes list and chooses within range
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = getValidWord(words).upper()
    wordLetters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() # Letters guessed
    lives = 5


    while len(wordLetters) > 0 and lives > 0:
        #letters used
        print('you have', lives, 'lives left and You have used these letters: ', ' '.join(usedLetters))

        #what current word is but with dashes for unguessed letters
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print ('current word: ', ' '.join(wordList))

        userLetter = input('Type a letter :  ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1
                print('Letter not in the word :/')

        elif userLetter in usedLetters:
            print('You\'ve already guessed this letter. Try again')

        else:
            print('Invalid Character. Please try again.')
    if lives == 0:
        print('You died, get rekt kid')
    else:
        print(f'Yay you guessed the word {word}')


getValidWord(words)
hangman()
