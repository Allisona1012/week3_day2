# #Given two strings, return true if they are anagrams of eachother, and false otherwise.
# s1 = "anagram"
# t1 = "nagaram"
# # Output:
# # True
# s2 = "rat"
# t2 = "car"
# #Output:
# # False

word1 = 'listen'
word2 = 'silent'

def anagram(word1, word2):
    if sorted (word1) == sorted (word2):
        return True
    return False

anagram(word1,word2)

