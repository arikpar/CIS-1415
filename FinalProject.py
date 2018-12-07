#Gabe Sorenson
#Arik Parenteau

import random
import time

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

deck_cards = card_value.copy()


#functions

def make_bet(chip_total):
    bet = 0
    print('What amount of chips would you like bet this hand?')
    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_total:
            bet = bet_comp
            chip_total = chip_total - bet
            print("You put in $" + str(bet_comp*5) + ".")
        else:
            print("You only have " + str(chip_total) + " chips remaining")
    return chip_total, bet


def play_round(chip_total):
    hit = ''
    chip_total, bet = make_bet(chip_total)
    user_hand = BlackjackHand()
    dealer_hand = BlackjackHand()
    print('\nYour cards:')
    print('----------------')
    user_hand.output_cards()
    print('\nDealer is showing:')
    print('----------------')
    dealer_hand.dealer_cards()
    while not user_hand.bust() and dealer_hand.hand_total != 21 and user_hand.hand_total != 21:
        hit = input("\nEnter 'h' to hit, anything else to stand.\n")
        if hit =='h':
            user_hand.hit()
            if user_hand.hand_total == 21:
                break
            if user_hand.hand_total > 21:
                print('You busted!')
        else:
            break
    print('\nDealer has:')
    if not user_hand.bust():
        dealer_hand.output_cards()
        while (not dealer_hand.bust()) and (dealer_hand.calculate_hand_val() < 17):
            print('\nDealer hits.')
            time.sleep(2)
            dealer_hand.hit()
            if dealer_hand.hand_total > 21:
                print('The dealer busted!')

    
    if user_hand.bust() or user_hand < dealer_hand:
        print('----------------')
        print('You lost: %s chips that hand.' % bet)
        print('New chip total: %s.' % chip_total)
        print('----------------')
        return chip_total
    elif user_hand == dealer_hand:
        print('You push!\n')
        chip_total = chip_total + bet
        print('You get your chips back.\nTotal: %s' % chip_total)
        return chip_total
    else:
        print('----------------')
        print('You won: %d chips that hand!' % bet)
        chip_total = chip_total + 2 * bet
        print('New chip total: %s' % chip_total)
        print('----------------')
        return chip_total
        

def play_again(chip_total):
    again = 'y'
    global deck_cards
    while again == 'y':
        if len(deck_cards.keys()) < 26:
            deck_cards = card_value.copy()
            print('Shuffling........')
        chip_total = play_round(chip_total)
        again = input("Do you want to play another hand? (Y/N): ").lower()
        if again != 'y':
            print('Goodbye! Thanks for playing!')
            print('----------------')
    return chip_total

 
#Blackjack Hand Class
class BlackjackHand:
    def __init__(self):
        self.hand_total = 0
        self.hand_vals = []
        self.hand_cards = []
        self.draw_card()
        self.draw_card()
   
    def draw_card(self):
        rand_val = random.randint(1,52)
        while rand_val not in deck_cards:
            rand_val = random.randint(1,52)
        self.hand_cards.append(rand_val)
        deck_cards.pop(rand_val)
        self.calculate_hand_val() 

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

    def output_cards(self):
        for x in range(len(self.hand_cards)):
            card = int(self.hand_cards[x])
            if card in card_value:
                cardval = card_value[card]
                print(cardval)
        print('Total: %d' % self.calculate_hand_val())
        if self.hand_total == 21:
            print('Blackjack!')

    def dealer_cards(self):
        print(card_value[self.hand_cards[0]])
        if self.hand_total == 21:
            print(card_value[self.hand_cards[1]])
            print('Dealer has a Blackjack.')
            
    def hit(self):
        self.draw_card()
        card = card_value[self.hand_cards[len(self.hand_cards) - 1]]
        print('%s is drawn' % card)
        print('Total: %s' % self.hand_total)

    def bust(self):
        if self.hand_total <= 21:
            return False
        else:
            return True

    def __lt__(self,other):
        if (self.hand_total < other.hand_total) and not other.bust():
            return True
        else:
            return False

    def __eq__(self,other):
        if self.hand_total == other.hand_total and not self.bust():
            return True
        else:
            return False
        
        
print('Welcome to the world of Blackjack!')
print('-----------------------------------')
chips = int(input('How many chips would you like to start out with? Each chip is worth $5.\n'))
while chips < 1 or chips > 100:
    chips = int(input('Invalid chip amount. Try again.\n'))
chips = play_again(chips)
print('Total winnings: %s chips' % chips)
                  
   
