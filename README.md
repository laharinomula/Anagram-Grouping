# Anagram-Grouping

An Anagram is a word formed by rearranging the letters of a different words,typically using all the original letters exactly once.

Lets have an example of list=["cat","dog","tac","god","act"]

output:[['dog', 'god'], ['tac', 'act', 'cat']]

Their may be duplicate words in list.First we lower all words in list and do working on unique words from list.


Here cat,tac,act and dog,god are anagrams.Lets have two strings dog and god
first we create Dictionary and then sort each word,then check whether its in Dictionary or not and append the word to Dictionary.

word1="dog"           
sorted(word1)                     ---->['d', 'g', 'o']
Then join these letters           ---->dgo

same goes for word2="god"
sorted(word2)                     ---->['d', 'g', 'o']
Then join these letters           ---->dgo

Here dog and god are different words but after rearranging both are same.As a result they are anagrams of each other.

similarlly tac,act,cat are different words but after rearranging they are same that is act.Therefore they are anagrams of each other.

Therefore the final output is [['dog', 'god'], ['tac', 'act', 'cat']]



