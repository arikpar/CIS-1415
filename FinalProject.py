#Gabe Sorenson
#Arik Parenteau
#12/12/2018

import random
import time

#dictionary for a deck of cards
card_value = {
  1: 'Ace of Hearts', 2: 'Two of Hearts', 3: 'Three of Hearts', 4: 'Four of Hearts', 5: 'Five of Hearts', 6: 'Six of Hearts',
  7: 'Seven of Hearts', 8: 'Eight of Hearts', 9: 'Nine of Hearts', 10: 'Ten of Hearts', 11: 'Jack of Hearts', 12: 'Queen of Hearts', 
  13: 'King of Hearts', 14: 'Ace of Diamonds', 15: 'Two of Diamonds', 16: 'Three of Diamonds', 17: 'Four of Diamonds',
  18: 'Five of Diamonds', 19: 'Six of Diamonds', 20: 'Seven of Diamonds', 21: 'Eight of Diamonds', 22: 'Nine of Diamonds',
  23: 'Ten of Diamonds', 24: 'Jack of Diamonds', 25: 'Queen of Diamonds', 26: 'King of Diamonds', 27: 'Ace of Clubs',
  28: 'Two of Clubs', 29: 'Three of Clubs', 30: 'Four of Clubs', 31: 'Five of Clubs', 32: 'Six of Clubs', 33: 'Seven of Clubs',
  34: 'Eight of Clubs', 35: 'Nine of Clubs', 36: 'Ten of Clubs', 37: 'Jack of Clubs', 38: 'Queen of Clubs', 39: 'King of Clubs', 
  40: 'Ace of Spades', 41: 'Two of Spades', 42: 'Three of Spades', 43: 'Four of Spades', 44: 'Five of Spades', 45: 'Six of Spades',
  46: 'Seven of Spades', 47: 'Eight of Spades', 48: 'Nine of Spades', 49: 'Ten of Spades', 50: 'Jack of Spades', 51: 'Queen of Spades',
  52: 'King of Spades'
}

#create the deck of cards played with
deck_cards = card_value.copy()

#Blackjack Hand Class
class BlackjackHand:
    #initialized hand by drawing 2 cards
    def __init__(self):
        self.hand_total = 0
        self.hand_cards = []
        self.draw_card()
        self.draw_card()

    #adds a card to a hand through a random integer
    def draw_card(self):
        rand_val = random.randint(1,52)
        while rand_val not in deck_cards:
            rand_val = random.randint(1,52)
        self.hand_cards.append(rand_val)
        deck_cards.pop(rand_val)
        self.calculate_hand_val() 

    #calculates the total of a hand
    def calculate_hand_val(self):
        self.hand_total = 0
        for x in range(len(self.hand_cards)):
            if self.hand_cards[x] in [2,15,28,41]:
                self.hand_total = self.hand_total + 2
            if self.hand_cards[x] in [3,16,29,42]:
                self.hand_total = self.hand_total + 3
            if self.hand_cards[x] in [4,17,30,43]:
                self.hand_total = self.hand_total + 4
            if self.hand_cards[x] in [5,18,31,44]:
                self.hand_total = self.hand_total + 5
            if self.hand_cards[x] in [6,19,32,45]:
                self.hand_total = self.hand_total + 6
            if self.hand_cards[x] in [7,20,33,46]:
                self.hand_total = self.hand_total + 7
            if self.hand_cards[x] in [8,21,34,47]:
                self.hand_total = self.hand_total + 8
            if self.hand_cards[x] in [9,22,35,48]:
                self.hand_total = self.hand_total + 9
            if self.hand_cards[x] in [10,23,36,49]:
                self.hand_total = self.hand_total + 10
            if self.hand_cards[x] in [11,12,13,24,25,26,37,38,39,50,51,52]:
                self.hand_total = self.hand_total + 10
            if self.hand_cards[x] in [1,14,27,40]:
                self.hand_total = self.hand_total + 11
        for x in range(len(self.hand_cards)):
            if (self.hand_cards[x] in [1,14,27,40]) and (self.hand_total > 21):
                self.hand_total = self.hand_total - 10
        return self.hand_total

    #prints cards in a hand
    def output_cards(self):
        for x in range(len(self.hand_cards)):
            card = int(self.hand_cards[x])
            if card in card_value:
                cardval = card_value[card]
                print(cardval)
                time.sleep(1)
        print('Total: %d' % self.calculate_hand_val())
        if self.hand_total == 21:
            time.sleep(1)
            print('Blackjack!')

    #prints first card in hand for the dealer
    #and outputs when they have a blackjack
    def dealer_cards(self):
        time.sleep(.5)
        print(card_value[self.hand_cards[0]])
        if self.hand_total == 21:
            time.sleep(.5)
            print(card_value[self.hand_cards[1]])
            time.sleep(1)
            print('Dealer has a Blackjack.')
            
    #draws a card and outputs new hand total
    def hit(self):
        self.draw_card()
        card = card_value[self.hand_cards[len(self.hand_cards) - 1]]
        print('%s is drawn' % card)
        if self.hand_total == 21:
            time.sleep(1)
            print("Blackjack!")
        if self.bust():
            time.sleep(1)
            print("Bust!")   
        print('Total: %s' % self.hand_total)


    def bust(self):
        if self.hand_total <= 21:
            return False
        else:
            return True

    #compares two hands
    def __lt__(self,other):
        if (self.hand_total < other.hand_total) and not other.bust():
            return True
        else:
            return False

    #checks if hands are the same
    def __eq__(self,other):
        if self.hand_total == other.hand_total and not self.bust():
            return True
        else:
            return False


#FUNCTIONS:
#get bet for a hand from user
def make_bet(chip_total):
    bet = 0
    print('What amount of chips would you like to bet this hand?')
    while bet == 0:
        try:
            bet_comp = input()
            bet_comp = int(bet_comp)

            if bet_comp >= 1 and bet_comp <= chip_total:
                bet = bet_comp
                chip_total = chip_total - bet
                time.sleep(.5)
                print("You put in $" + str(bet_comp*5) + ".")
            else:
                time.sleep(.5)
                if bet_comp > chip_total:
                    print("You only have " + str(chip_total) + " chips remaining")
                else:
                    print('Enter an amount greater than 0.')
        except ValueError:
            print('Please enter an integer value.')
    return chip_total, bet


#plays one hand of blackjack
def play_hand(chip_total):
    hit = ''
    chip_total, bet = make_bet(chip_total)
    user_hand = BlackjackHand()
    dealer_hand = BlackjackHand()
    time.sleep(1)
    print('\nYour cards:')
    print('----------------')
    time.sleep(1)
    user_hand.output_cards()
    time.sleep(1)
    print('\nDealer is showing:')
    print('----------------')
    time.sleep(1)
    dealer_hand.dealer_cards()
    
    while not user_hand.bust() and dealer_hand.hand_total != 21 and user_hand.hand_total != 21:
        time.sleep(1)
        hit = input("\nEnter 'h' to hit, anything else to stand.\n")
        hit = hit.lower()
        if hit =='h':
            time.sleep(1)
            user_hand.hit()
            if user_hand.hand_total == 21:
                break
            if user_hand.hand_total > 21:
                time.sleep(1)
                print('You busted!')
        else:
            print('You stand\n')
            time.sleep(1)
            print('Dealer has:')
            time.sleep(1)
            break

    if user_hand.hand_total == 21:
        print('Dealer has:')
    
    if not user_hand.bust():
        if dealer_hand.hand_total != 21:
            dealer_hand.output_cards()
        while (not dealer_hand.bust()) and (dealer_hand.calculate_hand_val() < 17):
            time.sleep(1)
            print('\nDealer hits.')
            time.sleep(1.5)
            dealer_hand.hit()
            if dealer_hand.hand_total > 21:
                time.sleep(1)
                print('The dealer busted!')

    #determines who won the hand and adjusts chip total
    if user_hand.bust() or user_hand < dealer_hand:
        print('----------------')
        time.sleep(1)
        print('You lost %s chips that hand.' % bet)
        time.sleep(1)
        print('New chip total: %s.' % chip_total)
        print('----------------')
        return chip_total
    
    elif user_hand == dealer_hand:
        time.sleep(1)
        print('You push!\n')
        chip_total = chip_total + bet
        time.sleep(1)
        print('You get your chips back.\nTotal: %s' % chip_total)
        return chip_total
    
    else:
        print('----------------')
        time.sleep(1)
        print('You won %d chips that hand!' % bet)
        chip_total = chip_total + 2 * bet
        time.sleep(1)
        print('New chip total: %s' % chip_total)
        print('----------------')
        return chip_total
        
#determines if user wants to play another hand
def play_again(chip_total):
    again = 'y'
    global deck_cards
    while again == 'y' and chip_total > 0:
        if len(deck_cards.keys()) < 26:
            deck_cards = card_value.copy()
            time.sleep(1)
            print('Shuffling........')
            time.sleep(2)
        chip_total = play_hand(chip_total)
        if chip_total == 0:
            print('You ran out of chips. Thanks for playing!')
            break
        again = input("Do you want to play another hand? (Y/N): ").lower()
        if again != 'y':
            time.sleep(1)
            print('----------------')
    return chip_total

#plays one 'game' where the user enters a chip total to start with
#then the final winnings/losings are output and saved in a text file
def play_game():
    print('Welcome to the world of Blackjack!')
    print('-----------------------------------')
    time.sleep(1)
    chips = 0
    print('How many chips would you like to start out with? Each chip is worth $5.')
    print('The maximum amount of chips to start with is 100')
    while chips == 0:
        time.sleep(1)
        try:
            chip_comp = input()
            chip_comp = int(chip_comp)
            if chip_comp >= 1 and chip_comp <= 100:
                chips = chip_comp
            else:
                if chip_comp > 100:
                    print("Enter an amount less than or equal to 100.")
                else:
                    print('Enter an amount greater than 0.')
        except ValueError:
            print('Please enter an integer value.')

    starting_chips = chips
    chips = int(play_again(chips))
    time.sleep(1)
    print('Total chips: %s' % chips)
    with open('gamewinnings.txt', 'a') as myfile:
        if chips > starting_chips:
            print('You came out $%d ahead' % (5 * (chips - starting_chips)))
            myfile.write('+$')
            myfile.write(str(5 * (chips - starting_chips)))
        elif chips == starting_chips:
            print('You came out even')
            myfile.write('$0')
        else:
            print('You lost $%d' % (5 * (starting_chips - chips)))
            myfile.write('-$')
            myfile.write(str(5 * (starting_chips - chips)))
        myfile.write('\n')
    print('----------------')
    time.sleep(1)

#reads the winnings/losings from previous games from a text file
def read_scores():
    try:
        f = open('gamewinnings.txt', 'r')
        doc = f.readlines()
        if len(doc) > 0:
            print('Total winnings from past games:')
            print()
            for row in doc:
                print(row,end='')
                time.sleep(.25)
            print()
        else:
            print('\nNo winnings saved.\n')
        f.close()
    except:
        print('\nUnable to find game winnings file. Please play a game first.\n')
    time.sleep(1)

#clears the text file winnings are saved int
def clear_scores():
    with open('gamewinnings.txt', 'w') as f:
        f.write('')
    print('\nPrevious game winnings cleared\n')
    time.sleep(1)


        
#Main part of program
menu = 'MENU:\n' \
       'p - play game\n' \
       'r - read previous winnings\n' \
       'c - clear scores\n' \
       'q - quit'
print('Welcome to the World of Blackjack')
print('Created by Arik Parenteau and Gabe Sorenson\n')
menu_selection = ''
while menu != 'q':
    print(menu)
    menu_selection = input('\nSelect an option:\n')
    menu_selection = menu_selection.lower()
    if menu_selection == 'p':
        play_game()
    elif menu_selection == 'r':
        read_scores()
    elif menu_selection == 'c':
        clear_scores()
    elif menu_selection == 'q':
        print('Goodbye! Thanks for playing!')
        break
    else:
        print('Invalid entry. Try again\n')

