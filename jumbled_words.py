"""input a sentence and it will reorder to the 
words keeping the first and the last the same"""
import random

def jumbler(word):
    word1 = list(word[1:-1])
    f = word1.copy()
    random.shuffle(f)
    while f == word1:
        random.shuffle(f)
    shuffled_word = word[0] + ''.join(f) + word[-1]
    return shuffled_word
#print("enter sentence")
#sent = input()
sent = "method in Python is used to concatenate elements of an iterable"
print(sent)

#if its greater than 3 letters then jumble
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

print(len(sentence_list))

# now you need to get index n and decide wether the size is bigger than 4 or not
for i, s in enumerate(sentence_list):
    #now anything greater than get special jumbler treatment
    if len(s) > 3:
        sentence_list[i] = jumbler(s)

print(sentence_list)


    # f is shuffled now we want to 


