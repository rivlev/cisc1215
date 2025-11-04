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
            print("You guessed it!")
            break

        # guess is valid
        # now score it
        result = [''] * NUM_LETTERS
        guess_letter_counts = secret_word_letter_counts.copy()
        # find green letters
        for i, c in enumerate(guess):
            if guess[i] == secret_word[i]:
                result[i] = GREEN_PREFIX + guess[i] + COLOR_POSTFIX
                guess_letter_counts[c] -= 1
        for i, c in enumerate(guess):
            if result[i] != '':
                continue
            if c not in guess_letter_counts or guess_letter_counts[c] == 0:
                result[i] = GRAY_PREFIX + guess[i] + COLOR_POSTFIX
            else:
                result[i] = YELLOW_PREFIX + guess[i] + COLOR_POSTFIX

        # print result
        print(''.join(result) + "\n")

    print(f"No more guesses. The word was {secret_word}")





if __name__ == "__main__":
    wordle()