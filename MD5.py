#MD5 Hashing Algorithem personal python implimentation, by Mr. Wootown.

#Note: in this implimentaion most of the operations will be done with the int datatype. However, using the 'bytes' object instead for the calculations may be faster.
#Edgecase: This script cannot compute the hash of a string typed as input with the backtick or backquote. It would either have to be entered as an apostrophe or manually chopped into 4 character string lenghts before digest.
#Edgecase: This script cannot compute the hash of a message that is more than 4 GiB in size.

'''
References and Acreditaions:
The team at rare skills whom made this video, 'https://youtu.be/5MiMK45gkTY?si=19VO2srwlIyfElrs'.
The creators of the video are not directly listed. However these are the lead teachers listed on their website, 'rareskills.io'. 
Internet alais, Shung
Philippe Dumonet
João Paulo Morais
Daniel Cumming
Gonçalo Magalhães
Jeffrey Scholz

While it is unknown whether all of them contributed directly in this video essay many or all of their expertiese was likely consulted to make it possible.
A special thanks is given to the team at rare skills who made this possible with brilliant animations, editing, vocal presentation, technical writing, and a plethora of other skills needed to have this video explanation come to be.
It truely would not have been possible without them. 
'''

import math

#  Input handling functions


#This function's input must be a hexadecimal number
def initialPad(message):
    message = message << 8
    return message + 0x80

#May not be nessicary. 
#Bitshifts the number left by 8. Basically adds more 0's to the end of the number but in a binary and not decimal (normal number) format.
def padInput(hexNumber):
    return hexNumber << 8

#Breaks a message into 4 character "words" for the digest algorithm. 
def break_message(message):
    array = []
    #calculates how many times to run the loop based on the length of the message
    for i in range(math.ceil(len(message)/4)):
        #adds a '`' after the first four letters
        message = message.replace(message[:4], message[:4] + '`', 1)
        #turns the message into an array
        array.append(message.split('`', 1)[0])
        #removes the first four letters and the '`' and converts the message back to a string
        message = message.replace(message[:4] + '`', '', 1)
        #print(message)
    return array

#Loops through all the "words" in the array converting them to an integer data type. The message is broken into words by the function above.
def message_words_to_int():
    for i in range(array_length):
        #First converts each string in the array into a utf-8 encoded hexidecimal number. Then converts the hexidecimal number (incidentally also stored as a string, but different) to a integer and replaces the original string in the array at the current index with said integer. 
        message_array[i] = int(message_array[i].encode('utf-8').hex(), 16)
        
        #Below is a helpful debug statement
        #print(hex(message_array[i]))

#Takes the last word in a message_block array and the word's length to insert the binary sequence 10000000 at the end of the data. It also pads the neccicary 0's to compleatly fill the word. 
def word_buffer(length, last_word):
    word_length = length
    match word_length:
        case 0:
            last_word = initialPad(last_word)
            #Acomplishes the same task as running the padInput function 3 times. 
            last_word = last_word << 24
            return last_word
        case 1:
            last_word = initialPad(last_word)
            #See comment in case 0. Only does it twice. 
            last_word = last_word << 16            
            return last_word
        case 2:
            last_word = initialPad(last_word)
            #See previous case comments.
            last_word = last_word << 8
            return last_word
        case 3:
            last_word = initialPad(last_word)
            return last_word
        case 4:
            print("Somehow, you need to create a new element in the array. IDK.\n Hurray. You did that!")
            return last_word

        case _:
            print("What the hell did you do?!")

def padTo448Bits():
    length_to_go = 14 - array_length
    
    match length_to_go:
        case 0:
            pass #for now
        case _:
            for i in range(length_to_go):
                message_array.append(0x00000000)

          
#  Digest Functions
def wordAdd(word1, word2):
    tempWord = word1 + word2
    return tempWord % 0x100000000

def rotate(tempWord, i):
    # The most significant bits after the bits have been circularly left shifted.
    mostSigBits = (tempWord << R[i]) % 0x100000000
    # The least significant bits after the bits have been circularly left shifted. The Python "Order of Operations" makes parentisies unessicary  in this line. 
    leastSigBits = tempWord >> 32 - R[i]
    return mostSigBits | leastSigBits

def redBox(tempWord, b, i):
    tempWord = wordAdd(tempWord, K[i])
    tempWord = rotate(tempWord, i)
    tempWord = wordAdd(tempWord, b)
    return tempWord

def bitwiseFunc(b, c, d, i):
    try:
        if 0 <= i <= 15:
            return (b & c) | ((~b) & d)
        if 16 <= i <= 31:
            return (d & b) | ((~d) & c)
        if 32 <= i <= 47:
            return b ^ c ^ d
        else:
            return c ^ (b | (~d))
    except:
        print("An unexpected error has occured. The bitwise Funcion cannot be compleated.")

def combine(a, word, b, c, d, i):
    tempWord = bitwiseFunc(b, c, d, i)
    tempWord = wordAdd(tempWord, a)
    tempWord = wordAdd(tempWord, word) 
    tempWord = redBox(tempWord, b, i)
    return tempWord

def iterate(curr_state, word, i):
    curr_state()
    cp = b
    dp = c
    ap = d
    bp = combine(a, word, b, c, d, i)
    a = ap
    b = bp
    c = cp
    d = dp


'''
#  Global variable declearations


# The message that will be processed into an MD5 hash. This processing is called digesting in the context of a hash. 
message = ""

#The current part of the message we are digesting if the message is longer than 56 charachters is a called block. Otherwise, this "block" is the whole message. 
#message_block = [0x0, ...]
#This new message block will be an array of hexidecimal integers (or maybe normal integers) for easy indexing. 
message_block = []
#This must then be processed into a full 512 bit block depending on the whole length of the message. 
'''
'''
The starting values of each of the digest variables, for lack of a better term.
All of these memory locations combined is known as the "state" of the algorithm.
The state is updated each iteration of the digest.
'''


# Starting values

#start_state = 0x67452301efcdab8998badcfe10325476
a = 0x67452301
b = 0xefcdab89
c = 0x98badcfe
d = 0x10325476

#ap, a.k.a. a_prime, is the next iteration of "a" in the algorithm
ap = 0x00000000
#bp stands for b_prime and so on
bp = 0x00000000
cp = 0x00000000
dp = 0x00000000

# Addtitive constants array
K = (0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
     0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
     0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
     0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
     0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
     0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
     0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
     0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
     0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
     0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
     0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05,
     0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
     0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
     0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
     0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
     0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391)

# Rotation Array
R = []
subList1 = [7, 12, 17, 22]
subList2 = [5, 9, 14, 20]
subList3 = [4, 11, 16, 23]
subList4 = [6, 10, 15, 21]


#  Initial setup functions.

#This function is specific to the rotation array and is only called at the begining of the program
def unpackRotation(sublist):
    i = 0
    while i < 4:
        ii = 0
        while ii < 4:
            R.append(sublist[ii])
            ii += 1
        i += 1
        
#packages the previous function to run on one sublist after the other for easier use. 
def allRotationSublistUnpack(sublistA, sublistB, sublistC, sublistD):
    unpackRotation(sublistA)
    unpackRotation(sublistB)
    unpackRotation(sublistC)
    unpackRotation(sublistD)



#  End of data and function delcarations


'''
#i is the iteration, 0 to 63
i = 0
'''

'''
For the first full test of this algorithm I will not process more than one block at a time. 
'''



# Main program



#Note: add match case statement to switch between modes 

#Runs the program in a message typing mode. No other mode is currently developed.

allRotationSublistUnpack(subList1, subList2, subList3, subList4)
R = tuple(R)
#print(R)
#message = input("Please input the message to be hashed in normal characher form.\n")
#The code below this comment is for testing purposes only. 
message = "WASDWASD WASD   WASD"
#print(f"The message {message} was input.")
#Run input handling


message_array = break_message(message)
#Below is a helpful debug statement.
#print(message_array[-1])
    
'''
The if else block below needs to be part of a overarching block loop.
'''
#The number of elements in the array.
array_length = len(message_array)
#Checks if the array is shorter than 14 words as to allow the proper formating at the end of a 512 bit (16 word) block.
if array_length <= 14:
    #Local variables--so that they only have to be computed once. 
    last_word_leng = len(message_array[-1])
    prepad_bit_length = (array_length - 1) * 32 + (last_word_leng) * 8
    

    #Execution of the actual input handling functionality.
    
    message_words_to_int()
    
    #Takes the last word of a message_block array and formats it according to the padding algorithm.
    if last_word_leng == 4:
        message_array.append(0x80000000)
    else:
        message_array[-1] = word_buffer(last_word_leng, message_array[-1])

    #Below is a helpful debug statement. It uses the map function to apply the hex function to each element in the array. The result is then converted back into a list. 
    #print( list(map(hex, message_array)) )
    
    #Other input handling  Ex. Padding the input to be the correct length, Adding the correct length at the end. Goal: the array to be 16 words long.

    padTo448Bits()
    
    '''
    print( message_array )
    print( array_length ) 
    print( list(map(hex, message_array)) )
    #'''
    #print(prepad_bit_length)
    
    #The arimetic and logical opperations in this expression allow for the correct sequence of bits (internally stored as an integer type) to be added for the 448 - 480th bits (these bits being the second to last word in the message_array). This sequence being the little endian expression of the bit length of the message.
    message_array.append((prepad_bit_length << 8)%0xFFFF << 16)
    #Below possible fix for the 4 GiB message limit. Realistically impractical, but a fun concept none the less. 
    #message_array.append( ((prepad_bit_length << 8)%0xFFFF << 16)%0xFFFFffff << 32 )
    message_array.append(0x00000000)

    
    #Start iteration loop as normal. This might go outside of the if, else statement later, but would still have to be in the "block loop".
    #Celebration comment!! I have finally gotten to implimenting the iteration loop itself. Hurray!!
    
else:
    #The array needs to be split into two.

    
    #This opperation converts all the elements of the array into hex numbers. 
    message_words_to_int()
    
    message_block = []
    for i in range(14):
        message_block.append(message_array.pop(i))


    
    #array_length -= 14




    

