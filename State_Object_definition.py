#stands for internal state
class Internal_St:
	self.i = 0

	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	
	# Defines what gets printed when the object is passed as an argument. Instead of the default.
	def __str__(self):
		return f"The internal state is {hex(self.a)}, {hex(self.b)}, {hex(self.c)}, and {hex(self.d)}."

	#  Digest Functions
	def wordAdd(self, word1, word2):
	    tempWord = word1 + word2
	    return tempWord % 0x100000000

	def rotate(self, tempWord):
	    # The most significant bits after the bits have been circularly left shifted.
	    mostSigBits = (tempWord << R[i]) % 0x100000000
	    # The least significant bits after the bits have been circularly left shifted. The Python "Order of Operations" makes parentisies unessicary  in this line. 
	    leastSigBits = tempWord >> 32 - R[i]
	    return mostSigBits | leastSigBits

	def redBox(self, tempWord, b, i):
	    tempWord = wordAdd(tempWord, K[i])
	    tempWord = rotate(tempWord)
	    tempWord = wordAdd(tempWord, b)
	    return tempWord

	def bitwiseFunc(self, b, c, d, i):
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

	def iterate(a, b, c, d, word, i):
	    cp = b
	    dp = c
	    ap = d
	    bp = combine(a, word, b, c, d, i)
	    a = ap
	    b = bp
	    c = cp
	    d = dp
	    i += 1

	def new_round():
		i = 0


