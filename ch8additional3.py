#Arik Parenteau
#Gabe Sorenson

codes = {'A': '@', 'a': '9', 'B': '%', 'b': '#', 'C': 'A', 'c': 'B', 'D': 'C', 'd': 'E',
         'E': 'D', 'e': 'F', 'F': 'G', 'f': 'H', 'G': 'I', 'g': 'J', 'H': 'K', 'h': 'L',
         'I': 'M', 'i': 'N', 'J': 'O', 'j': 'P', 'K': 'Q', 'k': 'R', 'L': 'S', 'l': 'T',
	  'M': 'U', 'm': 'V', 'N': 'W', 'n': 'X', 'O': 'Y', 'o': 'Z', 'P': 'a', 'p': 'b',
	  'Q': 'c', 'q': 'd', 'R': 'e', 'r': 'f', 'S': 'g', 's': 'h', 'T': 'i', 't': 'j',
	  'U': 'k', 'u': 'l', 'V': 'm', 'v': 'n', 'W': 'o', 'w': 'p', 'X': 'q', 'x': 'r',
	  'Y': 's', 'y': 't', 'Z': 'u', 'z': 'v' }
		 
		 
		 
def getSentence():
	sentence = input('Enter a sentence to translate:\n')
	return sentence
	
def encryptSentence(sentence):
	encryptedSent = ''
	for char in sentence:
		if char in codes:
			encryptedSent = encryptedSent + codes[char]
		else:
			encryptedSent = encryptedSent + char
	return encryptedSent

def decryptSentence(sentence):
	decrypted = ''
	keyList = []
	valList = []
	for key in codes:
	    keyList.append(key)
	for val in codes.values():
	    valList.append(val)
	
	for char in sentence:
	    if char in valList:
	        for x in range(len(valList)):
	            if char == valList[x]:
	                decrypted = decrypted + keyList[x]
	    else:
	        decrypted = decrypted + char
	return decrypted


sentence = getSentence()
encryptedSent = encryptSentence(sentence)
print('Encrypted: %s' % encryptedSent)
decryptedSent = decryptSentence(encryptedSent)
print('Decrypted: %s' % decryptedSent)
