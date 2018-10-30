#Gabe Sorenson
#Arik Parenteau

def main():
	mystr = input('Enter a string: ')
	mystr.lower()
	vowelSet = set(['a', 'e', 'i', 'o', 'u'])
	runVowels(mystr, vowelSet)
	runConsonants (mystr, vowelSet)
	
def runVowels(mystr, vowelSet):
	index = 0
	vowels = 0
	
	while index < len(mystr):
		if mystr[index] in vowelSet:
			vowels += 1
			
		index += 1
	print ('This string consists of ', vowels, 'vowels.')
		
def runConsonants(mystr, vowelSet):
	index = 0
	consonants = 0
	
	while index < len(mystr):
		if mystr[index] not in vowelSet:
			consonants += 1
			
		index += 1
	print ('This string consists of ', consonants, 'consonants.')
	
main()
