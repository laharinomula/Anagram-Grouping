def anagram_grouping(words):
    d = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]
    return list(d.values())
words = ["cat","dog","tac","god","act","Cat"]
words=[i.lower() for i in words]
words=list(set(words))
print(anagram_grouping(words))
