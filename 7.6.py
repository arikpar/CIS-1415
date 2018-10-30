#Arik Parenteau
#

theString = input('Enter input string:\n')

while theString != 'q':
    while theString.count(',') == 0:
        print('Error: No comma in string.\n')
        theString = input('Enter input string:\n')
    
    stringList = theString.split(',')
    print('First word: %s' % stringList[0].strip())
    print('Second word: %s\n' % stringList[1].strip())
    
    theString = input('Enter input string:\n')
