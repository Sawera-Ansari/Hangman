
#prints the respective "hanging man" diagram

def hangman(guessed_letters,vowels_letters):
    HANGMANPICS = ['''

   +---+

   |   |

       |

       |

       |

       |


 =========''', '''

   +---+

   |   |

   O   |

       |

       |

       |


 =========''', '''

   +---+

   |   |

   O   |

   |   |

       |

       |


 =========''', '''

   +---+

   |   |

   O   |

  /|   |

       |

       |


 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

       |

       |


 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  /    |

       |


 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |


 =========''']

    check=len(guessed_letters)+len(vowels_letters)
    if check>=6:
        print(HANGMANPICS[6])
    else:
        print(HANGMANPICS[check])
