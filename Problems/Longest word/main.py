# print(max(len(input()), len(input())))

word1 = input()
word2 = input()

len_word1 = len(word1)
len_word2 = len(word2)

if len_word1 > len_word2:
    print(len_word1)
else:
    print(len_word2)
