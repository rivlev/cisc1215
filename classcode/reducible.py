word_list = open('/workspaces/cisc1215/classcode/words.txt').read().split()
word_list.extend(["a", "i"])

reducible_memo = {'a':True, 'i':True}
def is_reducible(w):
    if len(w) == 0:
        return False
    if w in reducible_memo:
        return reducible_memo[w]
    for c in w:
        new_word = w.replace(c, "", 1)
        if new_word not in word_list:
            continue
        reducible_memo[new_word] = is_reducible(new_word)
        if reducible_memo[new_word]:
            return True
    return False

for w in sorted(word_list, key=lambda w: len(w), reverse=True):
    if is_reducible(w):
        print(w)
        break
    else:
        print(f"{w} is not reducible")

print(is_reducible("sprite"))
