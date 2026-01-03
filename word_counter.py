Sentence = (input("Enter a sentence: ")) 
Words = Sentence.lower().split() 
word_count = {} 
for word in Words: 
    if word in word_count:
        word_count[word] += 1 
    else: 
        word_count[word] = 1

print("Word Count:", word_count)