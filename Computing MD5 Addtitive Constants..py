'''
This code was written to help to test portions of the fully compleated MD5 Hashing Algorithem implimentation.
Originally, it was used to just compute the MD5 Additive constants used as a part of the digest.
It has morphed into a notekeeping of sorts to hap-hasardly document the process of designing the module. 
'''

import math
import sys

i = 0
K = []

'''
while (i < 64):
    print(hex(
        math.floor(pow(2, 32) * abs(math.sin(i + 1) ))
    ))
    i += 1
'''
'''
while (i < 64):
    K.append(hex(
        math.floor(pow(2, 32) * abs(math.sin(i + 1) ))
    ))
    i += 1

print(K)

#add 16 as the second arguemnt to specify base 16. 
print(hex(int(K[0], 16)))
'''

'''
x = 45
print(x + 0xFF)
'''

'''
R = list()
# s stands for sequence. Each one of the rotaions is a sequence that repeates every four values. 
s1 = [7, 12, 17, 22]
s2 = [5, 9, 14, 20]
s3 = [4, 11, 16, 23]
s4 = [6, 10, 15, 21]

i = 0
while i < 4:
    ii = 0
    while ii < 4:
        R.append(s2[ii])
        ii += 1
    i += 1

i = 0
while i < 4:
    ii = 0
    while ii < 4:
        R.append(s3[ii])
        ii += 1
    i += 1

i = 0
while i < 4:
    ii = 0
    while ii < 4:
        R.append(s4[ii])
        ii += 1
    i += 1
'''    

'''
while i < 16:
    R.append(f)
    f = (f + 5) % 32
    i += 1
'''

#print(R)
'''
x, y = 4, 7
z = x << 2
print('The length of the integer 16 is: ' + str(sys.getsizeof(x << 2)) + ' in python.')
print(x << 8)
print(y << 2)
print(y << 8)
print("This is the length of 1024 in system memory is " + str(sys.getsizeof(x << 30)) + ' in python.\n' )
print("This is the obcene number " + str(x << 128)+ ".\nIt takes up " + str(sys.getsizeof(x << 128)) + ' bytes of memory in python.')
print("The length of the integer 16 is " + str(z.bit_length()) + " bits long without the setup overhead from python.")
'''
'''
x = 0xE7993074
print(hex(x))
print(bin(x))
print(hex(x << 8))
print(bin((x << 8) % 0xFFFFffff))
'''
''''
print(4 % 2)
print(256 % 256)
print(256 % 255)
print(255 % 256)
print(pow(2,32))
print(hex(pow(2,32)))
'''
'''
#print( ("Example String".encode('utf-8').hex() ))

a = 0x83 + 0xB5
print(a)

'''
'''
#message = "This is an example messeage."
tiny_message = "age"
#print(len(message)*8)
long_message = "This is a long message. It is meant to be longer than 512 bits. If it is a scucess!"
#print(len(long_message)*8)
#print(int(message.encode('utf-8').hex(), 16) )
'''
'''
print(type(23 in range(0, 447) ))
print(long_message[:56])

print(long_message[5]) # prints the 'i' in is
print(long_message.replace(long_message[:4], long_message[:4] + '`', 1 ))

print(long_message[:5])# prints to the space after 'this'
'''
#input an element of an array 
#def padWord():
'''
def formatIn(message):
    #the length of the message in bits is the length in charaters multiplied by eight. Assume we are using the UTF-8 encoding. 
    message_length = len(message) * 8
    initialPad(message)
    while(lengthInBits(message) <= 448):
        padInput(message)
    
'''
'''
#Note: match statements in python are basically switch statements in C++
print(tiny_message[:4])

processed_message = long_message.replace(long_message[:56], long_message[:56] + '`', 1)
message_blocks = processed_message.split('`', 1)
print(message_blocks)
print(message_blocks[0])
#try to impliment the following in a for or while loops to process the entire current block
current_block = message_blocks[0]
for i in range(14):
    #because of the added charachter the multiplier needs to be 5 instead of the number of charachers we would like to jump forward.
    index = i * 5
    current_block = current_block.replace(current_block[index : index + 4], current_block[index : index + 4] + '`', 1)
print(current_block)
current_block = current_block.split('`', 1)
message_word = current_block.pop(0)
print(message_word)
#message_word_array = chopped_message[0].replace(chopped_message[:4], chopped_message[:4] + '`', 1)
#print(message_word_array)
#chopped_message = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
#chopped_message[index] = message_blocks[block_index]
'''
'''
def message_to_word(message, array):
    for i in range(math.floor(len(message)/4)):
        #because of the added charachter the multiplier needs to be 5 instead of the number of charachers we would like to jump forward.
        index = i * 5
        message = message.replace(message[index: index + 4], message[index: index + 4] + '`', 1)
        message = message.split('`', 1)
        print(message)
        array = array.append(message.pop(0))
        print(message)
        print(array)
        message = message[0]
        print(message)
    return message
print(message_to_word(test_case, chopped_message))   
'''
'''
#Pytohn would need to be able to pass the message by reference for the below to be in a function. As far as I know there is no equivenat in Python. 

#Check the size of the array
def block_construction
    if len(message_array) <= 14:
        for i in message_array:
            message_array[i] = messageToHex(message_array[i])
        #start iteration loop as normal
    else:
        #The array needs to be split into two
        #This opperation converts all the elements of the array into hex numbers. 
        for i in message_array:
            message_array[i] = messageToHex(message_array[i])
        message_block = []
        for i in range(14):
            message_block.append(message_array.pop(i))
'''
'''
#Turns the last element of message_array into a 4 char string.
def word_buffer(x):
    match len(x):
        case 1:
            return '   '
        case 2:
            return '  '
        case 3:
            return ' '
        case 4:
            print("You done messed up. This function didn't need to be called.")
            return ''
        case 0:
            print("You need to get rid of the last index in this array.")
            return ''
        case _:
            print("What the hell did you do?!")
            return ''
'''



test_case = 'WASDWASD WASD   WASD'
long_test = "Disruptive shanks think sandels chapters that likely shows thoughts"

#breaks a message into 4 character "words" for the digest algorithim. 
def break_mesg(message):
    array = []
    for i in range(math.ceil(len(message)/4)):
        message = message.replace(message[:4], message[:4] + '`', 1)
        array.append(message.split('`', 1)[0])
        message = message.replace(message[:4] + '`', '', 1)
        #print(message)
    return array
'''
chopped_message = list()
test_case = test_case.replace(test_case[:4], test_case[:4] + '`', 1)
chopped_message = test_case.split('`', 1)
print(chopped_message)
'''
'''
print(test_case)
print(break_mesg(test_case)[-1])

print(long_test)
print(break_mesg(long_test)[-1])
print(break_mesg(long_test))
'''
'''
def word_buffer(x):
    match x:
        case 1:
            return '   '
        case 2:
            return '  '
        case 3:
            return ' '
        case 4:
            print("You done messed up.")
            return ''
        case 0:
            print("You need to get rid of the last index in this array.")
            return ''
        case _:
            print("What the hell did you do?!")
            return ''
'''
        
'''
#Below is a helpful debug statement
message_array_hex = list(map(hex, message_array))
print(message_array_hex) 
#'''

new_array = break_mesg(long_test)
'''
#new_array[-1] = new_array[-1].replace(new_array[-1], new_array[-1] + word_buffer(len(new_array[-1])) )
print(new_array[-1])
#print(len(new_array))


def padInput(hexNumber):
    hexNumber << 8

#Turns a string into a utf-8 encoded hexideximal number. 
def messageToHexInteger(String):
    return int(String.encode('utf-8').hex(), 16)
#The above could be a lambda function. ( lambda x: int(x.encode('utf-8').hex(), 16) )

print(new_array)
new_array = list(map(messageToHexInteger, new_array))
print(new_array[-1])
print( hex(new_array[-1]) )
last_hex_num = list(map(hex,new_array))[-1]
print(last_hex_num)
print( int(last_hex_num, 16) )
print( hex(int(last_hex_num, 16)) )
pearl = 0
for i in range(1):
    pearl += 1
print( pearl )
'''

'''
#This test works!


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

R = []
subList1 = [7, 12, 17, 22]
subList2 = [5, 9, 14, 20]
subList3 = [4, 11, 16, 23]
subList4 = [6, 10, 15, 21]


allRotationSublistUnpack(subList1, subList2, subList3, subList4)
R = tuple(R)
print(R)
'''
'''
#print(len(test_case) * 8)
prepad_bit_length = 444
print( hex(prepad_bit_length) )
print( hex((prepad_bit_length << 8)%0xFFFF << 16) )
'''
'''
# Rotate algorithm redo, Atempt 1
numberToRotate = 0xFFFEffff
rotate_by = 8
#print( hex(0xFFFFffff << (32 - rotate_by) ) )
leftShift = numberToRotate << rotate_by
print(f"This is the logical left shift output {hex(leftShift)}.\n")
baseMask = 0xFFFFffff
higherOrderBits = leftShift & baseMask
print(f"This is the base mask applied to the left shift output is {hex(higherOrderBits)}.\n")
newMask = baseMask << (32 - rotate_by)
print(f"This is the new mask {hex(newMask)}.\n")
lowerOrderBits = newMask & leftShift 
print(f"This is the lower order of bits {hex(lowerOrderBits)}.\n")
#The subtraction opperator in python is evaluate before the bitshift. 
shiftedLowBits = lowerOrderBits >> 32 - rotate_by
print(f"This is the lowest order bits shifted into the correct place {hex(shiftedLowBits)}.\n")
rotated = higherOrderBits | shiftedLowBits
print(f"This is the final 32 cyclic rotation of the bits {hex(rotated)}.\n")
'''
