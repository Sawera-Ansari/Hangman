#importing all the relevent function files

import hangman
import score
import word
import startGame
import game
import essential


guessed_letters=[]
vowels_letters=[]
guesses=6
warnings=3
SecretWord=word.word()     #chooses a random word
av=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
secword=[]
sec_word=[]
for i in SecretWord:
    secword+=i
    sec_word+='_'



startGame.startGame(SecretWord)      #prints the introductory interface

while True:

    essential.essentials(av,sec_word,guesses,warnings)    #displays player's progress

    ans=input('Please Guess a Letter:')
    ans=ans.lower()   #so if the player inputs any upper case letter,it can also be processed
    if ans!='':
        if ans in SecretWord:
            if ans in sec_word:
                print("You've Already Guessed It.") #warns the player
                
                if warnings!=0:

                    warnings-=1      #lessens a warning if the input has already been guessed before
                    hangman.hangman(guessed_letters,vowels_letters)

                else:
                    guesses-=1

                    guessed_letters+=[ans]

                    hangman.hangman(guessed_letters,vowels_letters)   #prints the respective "hanging man" diagram for loss due to having already that letter guessed

                
            else:
                print('Good Job!!')  #praises the player

                hangman.hangman(guessed_letters,vowels_letters)

                for l in range(len(secword)):

                    if secword[l]==ans:
                        sec_word[l]=ans
        else:
        
            if ans in av:

                print('Oops!! That letter is not in my word.')

                if ans in 'aeiou':
                    guesses-=2
                    guessed_letters+=[ans]
                    vowels_letters+=[ans]

                    hangman.hangman(guessed_letters,vowels_letters)  #prints the diagram representing double loss of guesses because of vowels
                    
                
                else:
                    guesses-=1
                    guessed_letters+=[ans]
                    hangman.hangman(guessed_letters,vowels_letters)   #prints the diagram represnting loss due to guessing the wrong letter
                
            else:

                print('Oops!! That is not a valid character.')   #warns the player

                if warnings!=0:
                    warnings-=1   #lessens a warning if the input is a special character,not a letter
                    hangman.hangman(guessed_letters,vowels_letters)
                else:
                    guesses-=1
                    guessed_letters+=[ans]
                    hangman.hangman(guessed_letters,vowels_letters)   #prints the diagram representing loss due to player's entering a special character, not a letter

    
        if ans in av:
            av.remove(ans)  #removes the guessed letter from available letters

        
        Game=game.game(SecretWord,sec_word,guesses)   #judges if the player LOST or WON or should continue playing
        if Game=='LOST':
            break
        elif Game=='WON':
            print('Your total score for this game is: ',score.score(guesses,SecretWord))  #calculates the score in winning case
            break



    print()
    print('-----------------------------------------------------------')

