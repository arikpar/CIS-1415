#Arik Parenteau
#Gabe Sorenson

import random

number = [2,3,4,5,6,7,8,9,10,11,12]
number_count = [0,0,0,0,0,0,0,0,0,0,0]
num_rolls = int(input('Enter number of rolls:\n'))

while num_rolls > 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
        number_count[roll_total-2] += 1
    print('Dice roll histogram:\n')
    for j in number:
        if j < 10:
             print('%s: ' % j, '*' * number_count[j-2])
        else:
             print('%s:' % j, '*' * number_count[j-2])		
    num_rolls = int(input('Enter number of rolls to add (enter negative number to be done):\n'))
