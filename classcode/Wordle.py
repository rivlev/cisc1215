from random import choice

NUM_GUESSES = 6
NUM_LETTERS = 5

GREEN_PREFIX = "\033[42m"
YELLOW_PREFIX = "\033[43m"
GRAY_PREFIX = "\033[100m"
COLOR_POSTFIX = "\033[0m"

def loadDictionary():
    # load legal words that are exactly five letters long
    legal_words = set()
    for line in open("classcode/words.txt"):
        w = line.strip().lower()
        if len(w) == NUM_LETTERS:
            legal_words.add(w)

    return legal_words

def count_letters(word):
    letter_counts = {}
    for c in word:
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1
    return letter_counts


def wordle():
    legal_words = loadDictionary()
    secret_word = choice(list(legal_words))
    secret_word_letter_counts = count_letters(secret_word)

    for g in range(NUM_GUESSES):
        guess = input(f"Enter a {NUM_LETTERS}-letter word (guess {g+1}/{NUM_GUESSES}):\n")
        while len(guess.strip()) != NUM_LETTERS or guess not in legal_words:
            guess = input(f"{guess} is not a valid word, try again (guess {g+1}/{NUM_GUESSES}):\n")

        if guess == secret_word:
            print(GREEN_PREFIX + guess + COLOR_POSTFIX)
            print(f"You guessed it in {g+1} tr{"y" if g == 0 else "ies"}!")
            return

        # guess is valid
        # now score it
        # initially, all letters are by default gray
        result = [GRAY_PREFIX + c + COLOR_POSTFIX for c in list(guess)]
        guess_letter_counts = secret_word_letter_counts.copy()
        # find green letters
        for i, c in enumerate(guess):
            # if a letter is not in secret word: it stays gray, check next letter
            if guess[i] not in secret_word:
                continue

            # else the letter must be in secret word
            # if it's at the correct location, it's green, decrement frequency dict
            elif guess[i] == secret_word[i]:
                result[i] = GREEN_PREFIX + guess[i] + COLOR_POSTFIX
                guess_letter_counts[c] -= 1

            # else the letter is in secret word, but not at the right location
            # if frequency dict still have letters, color letter yellow and decrement count
            elif guess_letter_counts[c] > 0:
                result[i] = YELLOW_PREFIX + guess[i] + COLOR_POSTFIX
                guess_letter_counts[c] -= 1
            
            # else: letter is in secret word, incorrect location, no more count in freq dict
            # color would be gray, no change from default color gray

        # print result
        print(''.join(result) + "\n")

    print(f"No more guesses. The word was {secret_word}")





if __name__ == "__main__":
    wordle()