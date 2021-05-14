
def essentials(av,sec_word,guesses,warnings):

    print('Available Words:',end=' ')
    for j in av:
        print(j,end=' ')
    print()
    print('Secret Word:',end=' ')
    for k in sec_word:
        print(k,end=' ')
    print()
    print('Your Guesses:',guesses)
    print('Your Warnings:',warnings)
