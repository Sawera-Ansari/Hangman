
#calculates the score in winning case.

def score(guesses,word):

    unique_letters=set(word)

    score= guesses*len(unique_letters)

    return score
