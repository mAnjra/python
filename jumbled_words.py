"""input a sentence and it will reorder the 
words keeping the first and the last the same

To test the phenomenon where if you mix the letters and keep the 
first and last the same our brains can still pick it up - quick
way to do it rather than to do it manually
"""
import random

def jumbler(word):
    word1 = list(word[1:-1])
    f = word1.copy()
    random.shuffle(f)
    while f == word1:
        random.shuffle(f)
    shuffled_word = word[0] + ''.join(f) + word[-1]
    return shuffled_word

print("Enter Sentence: ")
sent = input()
print("Original sentence: ", sent)

sentence_list = []
# separate words into a list of words
word = ""
for i , l in enumerate(sent):
    if l != " ":
        word = word + l
    elif l == " ":
        sentence_list.append(word)
        word = ""
    if i == len(sent)-1:
        sentence_list.append(word)

for i, s in enumerate(sentence_list):
    if len(s) > 3:
        sentence_list[i] = jumbler(s)

string_sentence = ' '.join(sentence_list)
print("Jumbled: ", string_sentence)