def anagram_grouping(words):
    d = {}
    for word in words:
        sorted_word = ''.join(sorted(word))	
        if sorted_word in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]
    return list(d.values()) 
N=int(input("enter list size:"))
words=[]
for i in range(0,N):
	print("enter word:")
	word=input("")
	if len(word)>=1 and len(word)<=100:
		words.append(word)
	else:
		print("enter word length between 1 and 100")
words=[i.lower() for i in words]
words=list(set(words))
print(anagram_grouping(words))
