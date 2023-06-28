'''
GOAL: Given a set of letters, generate all possible English words using those letters once (min length of 3 letter words)
INPUT: letters by the user (all on one line)
OUTPUT: all possible English words
'''


ALLOWED_LETTERS = list(input("Enter the letters: "))


def is_legal_word(possible_word):
    TEMP_ALLOWED_LETTERS = ALLOWED_LETTERS.copy()  # since the ALLOWED_LETTERS are changed (removed) due to the algorithm,
                                                   # a copy must be passed through in order to keep ALLOWED_LETTERS untouched
    if len(possible_word) < 3:
        return False
    
    '''
    The algorithm loops over each letter in the possible word, if the letter is not in the list of allowed letters entered by
    the user, the word is invalid. If the letter is in the list of allowed letters, a single instance of that letter is removed
    from the list because it cannot be used again. If the algorithm makes it through each letter of the possible word, the word is legal
    '''
    for letter in possible_word:
        if letter not in TEMP_ALLOWED_LETTERS:
            return False 
        else:
            TEMP_ALLOWED_LETTERS.remove(letter)
    return True
    

LEGAL_WORDS = []
with open("english_words.txt") as f:
    for word in f:
        word = word.strip()
        if is_legal_word(word):
            LEGAL_WORDS.append(word)


# sorts and prints words by length (shortest to longest)
LEGAL_WORDS.sort(key=len)
print("Your words are:")
for legal_word in LEGAL_WORDS:
    print(legal_word)
