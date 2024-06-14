'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r'''

word1 = "abc"
word2 = "pqr"

oddWords = ""
evenWords = ""
#range(start, stop, step)
for i in range(0,len(word1),2):
    oddWords += word1[i]
    
for i in range(1,len(word1),2):
    evenWords += word2[i]


print(oddWords)
print(evenWords)