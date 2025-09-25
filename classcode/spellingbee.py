def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
        
    return True
        
        
def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    word = word.upper()
    available = available.upper()
    required = required.upper()
    if len(word) < 4:
        return False
    if required not in word:
        return False
    for letter in word:
        if letter not in available:
            return False
    return True

def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    if len(word) == 4: 
        return 1
    score = len(word)
    if uses_all(word, available):
        score += 7
    return score



available = 'ONGUPRI'
required = 'U'

total = 0

file_object = open('./words.txt')
for line in file_object:
    word = line.strip()
    if check_word(word, available, required):
        score = word_score(word, available)
        total = total + score
        print(word, score)

print("Total score", total)