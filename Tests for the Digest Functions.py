from MD5 import *
import random

#The UTF-8 encoding of WSAD
myWord = 0x57415344
#print( hex(message) )

interal_state = Internal_St()

print(f"{hex(a)} {hex(b)} {hex(c)} {hex(d)}")
reset_tup = (a, b, c, d)
tempWord = 0

def is_expected(output, expected_out):
    if output == expected_out:
        print(f"The output matched what was ecpected. Test passed!\n\n")
    else:
        print(f"The output was not was expected. Test failed. :(\n\n")

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
print(f"Test 1\nThe sarting values for the internal state are as follows: a = {hex(a)}, b = {hex(b)}, c = {hex(c)}, and d = {hex(d)}" )
print(f"This is what the temporay word has changed into {hex(tempWord)}.\n\n")
testWord = tempWord

# Test 2
a, b, c, d = reset_state()
print(f"Test 2\nThe sarting values for the internal state are as follows: a = {hex(a)}, b = {hex(b)}, c = {hex(c)}, and d = {hex(d)}")
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
testWord2 = tempWord

# Test 2.1
if testWord == testWord2:
    print(f"The output of the combine function is correct!\n\n")
else:
    print(f"The output of the combine function is not correct. :(\n\n")

# Test 3
a, b, c, d = reset_state()
tempWord = combine(a, myWord, b, c, d, itera)
print(f"Test 3\nThe result of the combine function with 0x57415344 as the word input and the first itteration was {hex(tempWord)}.\nThe expected output was 0x45c98920.\n\n")
is_expected(0x45c98920, hex(tempWord))


# Variables used for tests 4 & 5.
word1 = 0x100003000
word2 = 0xf2
# Test 4
myResult = wordAdd(word1, word2)
print(f'Test 4\nI tried to add {hex(word1)} and {hex(word2)}. \nWith the add word function the result was {hex(myResult)}.\n\n')


# Test 5
rotation_index = 1
myResult = rotate(word1, rotation_index)
print(f"\nTest 5\nI tried to rotate {hex(word1)} left by {R[rotation_index]} bits. \nThe result of the rotate function was {hex(myResult)}.\n")
myResult = rotate(word2, rotation_index)
print(f"\nI tried to rotate {hex(word2)} left by {R[rotation_index]} bits. \nThe result of the rotate function was {hex(myResult)}.\n\n")

# Test 6
a, b, c, d = reset_state()
print(f"Test 6\nThese are the starting values for the internal state {hex(a)} {hex(b)} {hex(c)} {hex(d)}\n")
end_tuple = iterate(a, b, c, d, myWord, 0)
print( tuple(map(hex, end_tuple)) )
a = end_tuple[0]
b = end_tuple[1]
c = end_tuple[2]
d = end_tuple[3]
print(f"This is 'a' through 'd': {hex(a)}, {hex(b)}, {hex(c)}, and {hex(d)}.")

# Test 7
internal_state.wordAdd()

# Test 8
for i in range(64):
    if i <= 15:
        word = message_array[i]
    if 16 <= i <= 31:
        word = message_array[i%16]
    if 32 <= i <= 47 :
        word = message_array[(i*7)%16]
    else:
        word = message_array[(i*5)%16]
    internal_state.iterate()
