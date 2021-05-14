
#chooses a random word

import random

def word():

    with open('words.txt') as f:
        
        contents=f.read()
        
    words=contents.split()
        
    word=random.choice(words)

    return word
