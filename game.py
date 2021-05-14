
def game(SecretWord,sec_word,guesses):

    if '_' not in sec_word:
        for m in sec_word:
            print(m,end=' ')
        print()
        print('Good Job!! You Guessed the Word Right.')
        return "WON"

    elif guesses<=0:
        print('Game Over!! You Lost.')
        print('Word was',SecretWord)
        return "LOST"
