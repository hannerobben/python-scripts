# Run as python3 hangman.py

import random, os, time

def hangman():

    # load words and hangman drawing from file
    hangmanImgFile = open('hangmanImage.txt')
    hangmanImg = hangmanImgFile.read().split('next\n')
    hangmanImgFile.close()
    wordsFile = open('hangmanWords.txt')
    words = wordsFile.read().split('\n')
    wordsFile.close()

    # Variables
    word = words[ random.randint(0, len(words)-1) ]
    letters = [ l for l in word]
    to_guess = '.' * len(word)
    letters_guess = [ l for l in to_guess ]
    guessed_letters = []

    wrong_guesses = 8;
    score = 32
    drawing_index = 0
    ok = False;

    # loop until game is over
    while '.' in letters_guess and wrong_guesses != 0:

        # refresh terminal screen
        time.sleep(0.4); os.system('clear')

        # print layout    
        print('\n'+hangmanImg[drawing_index])
        print('\n\n'+ to_guess +'\n')
        if len(guessed_letters) > 0:
            print('You have already guessed: {}'.format(" - ".join(guessed_letters)))
        else:
            print('')           
        print("You have " + str(wrong_guesses) + " wrong guesses left!") 
        guessed_letter = input('Guess a letter: ')

        # check if guessed letter is valid. If not, ask again.
        while not ok:
            if not guessed_letter.isalpha() or not len(guessed_letter) == 1:
                print('This is not a valid letter, try again!')
                guessed_letter = input('Guess a letter: ')
            elif guessed_letter in guessed_letters:
                print('You already guessed this letter, try again!')
                guessed_letter = input('Guess a letter: ')
            else:
                ok = True;
                
        guessed_letters.append(guessed_letter)
        ok = False;

        # check if guessed letter is correct
        for i in range(len(word)):
            if letters[i] == guessed_letter:
                letters_guess[i] = guessed_letter
        # if not correct, update parameters
        if guessed_letter not in letters:
            wrong_guesses -= 1
            score -= 4
            drawing_index += 1
                
        to_guess = "".join(letters_guess)    

        # game over: win or lose
        if '.' not in letters_guess:
            time.sleep(0.4); os.system('clear')
            print('\n'+hangmanImg[drawing_index])
            print('\n\n'+ to_guess +'\n')
            print('\n-------------------------')
            print('Congratulations, you win!')
            print('Your score is: {}'.format(score))
            print('-------------------------')
        if wrong_guesses == 0:
            time.sleep(0.4); os.system('clear')
            print('\n'+hangmanImg[8])
            print('\n'+ to_guess +'\n')
            print('\n-------------------------')
            print('Game over, you lose!\nThe word was: {}'.format(word))
            print('-------------------------')

        



if __name__ == "__main__":
    hangman()
