#Gabe Sorenson
#Arik Parenteau

def main():
    english = input('Enter your English here: ')
    pig = []
    for word in english.split():
        pig.append(word[1:]+word[0]+'AY')
    translated = 'Pig Latin: ' + ' '.join(pig)
    print(translated.upper())
main()
