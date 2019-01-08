def pig_latin(word):
    # Setup
    vowels = 'AaEeIiOoUu'
    consonantsCount = 0
    wordLength = len(word)

    # Only one letter word with a vowel
    # Example: "I" -> "Iway"
    if(wordLength == 1 and word in vowels):
        return '{}{}'.format(word, 'way')

    # Count number of consonants
    while(consonantsCount < wordLength and
            word[consonantsCount] not in vowels):
        consonantsCount += 1

    # If all chars are consonants, just return the word
    # Example: "thx" -> "thx"
    if(consonantsCount == wordLength):
        return word

    # Consonant clusters (multiple consonants that form one sound).
    # Example: "smile" -> "ilesmay"
    if(consonantsCount >= 2):
        return '{}{}{}'.format(
            word[consonantsCount:], word[:consonantsCount], "ay")

    # First char is a vowel.
    # Example "eat" -> "eatay"
    if(word[0] in vowels):
        return '{}{}'.format(word, "ay")

    # First char is a consonant.
    # Example: "car" -> "arcay"
    return'{0}{1}{2}'.format(word[1:], word[0], "ay")


def main():
    while(True):
        word = input("Insert word: ")
        print("Pig Latin word:", pig_latin(word), "\n")


if __name__ == '__main__':
    print()  # Blank space
    print("Welcome to the language game -> Pig Latin")
    print("Enjoy!")
    print()  # Blank space
    main()
