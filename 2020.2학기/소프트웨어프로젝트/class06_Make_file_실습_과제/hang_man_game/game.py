from hangman import Hangman
from guess import Guess
from word import Word

# 
def gameMain():
    word = Word('class06_Make_file_실습_과제/hang_man_game/words.txt')
    guess = Guess(word.randFromDB())
    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
        print("Secrect 단어는:",guess.secretWord,"였습니다")
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('total guess ',end = ' ')
        print(guess.guessedChars)
        print('Fail')


if __name__ == '__main__':
    gameMain()
