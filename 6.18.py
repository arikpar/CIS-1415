#Arik Parenteau
#Gabe Sorenson

def get_num_of_characters(inputStr):
    return len(inputStr)
def output_without_whitespace(string):
    new_string = ''
    i = 0
    while i < len(string):
        if string[i] != ' ' and string[i] != '  ':
            new_string = new_string + string[i]
        i = i + 1
    return new_string

if __name__ == '__main__':
    sentence = input('Enter a sentence or phrase:\n')
    char_count = get_num_of_characters(sentence)
    nowhitespace = output_without_whitespace(sentence)
    
    print('\nYou entered:', sentence)
    print('\nNumber of characters:', char_count)
    print('String with no whitespace:', nowhitespace)
