word1 = list(input())
word2 = list(input())

word1.sort()
word2.sort()

sorted_word1 = ''.join(word1)
sorted_word2 = ''.join(word2)

if word1 == word2:
    print("Yes")
else:
    print("No")
