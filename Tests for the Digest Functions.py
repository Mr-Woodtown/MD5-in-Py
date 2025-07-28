from MD5 import *
import random

#The UTF-8 encoding of WSAD
myWord = 0x57415344
#print( hex(message) )

print(f"{hex(a)} {hex(b)} {hex(c)} {hex(d)}")
reset_tup = (a, b, c, d)
tempWord = 0

def reset_state():
    print( hex(reset_tup[0]) )
    return reset_tup[0], reset_tup[1], reset_tup[2], reset_tup[3]

# This variable will be used for tests 1-3.
itera = 0
# Test 1
cp = b
dp = c
ap = d
tempWord = combine(a, myWord, b, c, d, itera)
a = ap
b = tempWord
c = cp
d = dp
print(f"{hex(a)} {hex(b)} {hex(c)} {hex(d)}")
print(f"This is what the temporay word has changed into {hex(tempWord)}.\n\n")


# Test 2
a, b, c, d = reset_state()
print(f"{hex(a)} {hex(b)} {hex(c)} {hex(d)}")
# Breaking down the combine function into its individual steps to compare the end result. 
tempWord = bitwiseFunc(b, c, d, itera)
print(f"The expected word was 0x98BADCFE.\nThe calulated word was {hex(tempWord)}.\n\n")
tempWord = wordAdd(tempWord, a)
print(f"The expected word was 0xFFFFfff.\nThe calulated word was {hex(tempWord)}.\n\n")
tempWord = wordAdd(tempWord, myWord)
print(f"The expected word was 0x57415343.\nThe calulated word was {hex(tempWord)}.\n\n")
#myWord = redBox(tempWord, b, 1)
tempWord = wordAdd(tempWord, K[itera])
print(f"This is the current additive constant {hex(K[itera])}.\n")
print(f"The expected word was 0x2eabf7bb.\nThe calulated word was {hex(tempWord)}.\n\n")
tempWord = rotate(tempWord, itera)
print(f"The expected word was 0x55fbdd97.\nThe calulated word was {hex(tempWord)}.\n\n")
tempWord = wordAdd(tempWord, b)
print(f"The expected word was 0x45c98920.\nThe calulated word was {hex(tempWord)}.\n\n\n")

# Test 3
a, b, c, d = reset_state()
tempWord = combine(a, myWord, b, c, d, itera)
print(f"The result of the combine function with 0x57415344 as the word input and the first itteration was {hex(tempWord)}.\nThe expected output was 0x45c98920.\n\n")


# Variables used for tests 4 & 5.
word1 = 0x100003000
word2 = 0xf2
# Test 4
myResult = wordAdd(word1, word2)
print(f'I tried to add {hex(word1)} and {hex(word2)}. \nWith the add word function the result was {hex(myResult)}.\n\n')

# Test 5
rotation_index = 1
myResult = rotate(word1, rotation_index)
print(f"\nI tried to rotate {hex(word1)} left by {R[rotation_index]} bits. \nThe result of the rotate function was {hex(myResult)}.\n")
myResult = rotate(word2, rotation_index)
print(f"\nI tried to rotate {hex(word2)} left by {R[rotation_index]} bits. \nThe result of the rotate function was {hex(myResult)}.\n\n")

# Test 6
a, b, c, d = reset_state()
print(f"{hex(a)} {hex(b)} {hex(c)} {hex(d)}")
iterate(myWord, 1)
