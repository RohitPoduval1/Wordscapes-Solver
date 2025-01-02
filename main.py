from sys import argv


MIN_LENGTH = 3
# No args given
if len(argv) == 1:
    ALLOWED_LETTERS = list(input("Enter the letters: "))
    MIN_LENGTH = int(input("Enter the minimum length of a valid word: "))

# Only letters given, get MIN_LENGTH by input
elif len(argv) == 2:
    ALLOWED_LETTERS = list(argv[1])

# Letters and MIN_LENGTH given
elif len(argv) == 3:
    ALLOWED_LETTERS = list(argv[1])
    try:
        MIN_LENGTH = int(argv[2])
    except ValueError:
        print("Invalid value for MIN_LENGTH, must be an integer. Will use the default of 3")

else:
    raise OSError("Too many arguments")


def is_legal_word(possible_word: str) -> bool:
    """
    Check whether the possible_word is a valid english word
    """
    # Since the ALLOWED_LETTERS are changed (removed) due to the algorithm,
    # a copy must be passed through in order to keep ALLOWED_LETTERS untouched.
    TEMP_ALLOWED_LETTERS = ALLOWED_LETTERS.copy()

    if len(possible_word) < MIN_LENGTH:
        return False

    for letter in possible_word:
        if letter not in TEMP_ALLOWED_LETTERS:
            return False
        else:
            TEMP_ALLOWED_LETTERS.remove(letter)
    return True


def main():
    LEGAL_WORDS = []
    with open("english_words.txt") as f:
        for word in f:
            word = word.strip()
            if len(word) >= MIN_LENGTH and is_legal_word(word):
                LEGAL_WORDS.append(word)

    # sort and print words by length (shortest to longest)
    LEGAL_WORDS.sort(key=len)
    if len(LEGAL_WORDS) > 0:
        print("Your words are:")
        for legal_word in LEGAL_WORDS:
            print(legal_word)
    else:
        print("No possible words")


if __name__ == "__main__":
    main()
