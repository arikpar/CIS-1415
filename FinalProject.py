#Gabe Sorenson
#Arik Parenteau

card_value = {
  1: 'Ace of Hearts', 2: '2 of Hearts', 3: '3 of Hearts', 4: '4 of Hearts', 5: '5 of Hearts', 6: '6 of Hearts',
  7: '7 of Hearts', 8: '8 of Hearts', 9: '9 of Hearts', 10: '10 of Hearts', 11: 'Jack of Hearts', 12: 'Queen of Hearts', 
  13: 'King of Hearts', 14: 'Ace of Diamonds', 15: '2 of Diamonds', 16: '3 of Diamonds', 17: '4 of Diamonds',
  18: '5 of Diamonds', 19: '6 of Diamonds', 20: '7 of Diamonds', 21: '8 of Diamonds', 22: '9 of Diamonds',
  23: '10 of Diamonds', 24: 'Jack of Diamonds', 25: 'Queen of Diamonds', 26: 'King of Diamonds', 27: 'Ace of Clubs',
  28: '2 of Clubs', 29: '3 of Clubs', 30: '4 of Clubs', 31: '5 of Clubs', 32: '6 of Clubs', 33: '7 of Clubs',
  34: '8 of Clubs', 35: '9 of Clubs', 36: '10 of Clubs', 37: 'Jack of Clubs', 38: 'Queen of Clubs', 39: 'King of Clubs', 
  40: 'Ace of Spades', 41: '2 of Spades', 42: '3 of Spades', 43: '4 of Spades', 44: '5 of Spades', 45: '6 of Spades',
  46: '7 of Spades', 47: '8 of Spades', 48: '9 of Spades', 49: '10 of Spades', 50: 'Jack of Spades', 51: 'Queen of Spades',
  52: 'King of Spades'
}


def calc_score(card_list):
total = 0
   for card in card_list:
      if total >=11 and card == 'A':
         total += 1
      else:
        total += card_value[card]
   return total

def make_bet():
   bet = 0
   print('What amount of chips would you like bet? Each chip is worth $5.')
  
   while bet == 0:
      bet_comp = input()
      bet_comp = int(bet_comp)
      chip_total = 100
      
      if bet_comp >= 1 and bet_comp <= chip_total:
         bet = bet_comp
         print("You put in $" + str(bet_comp*5) + ".")
      else:
         print("You only have " + str(chip_total) + " remaining")
          
import random

deck_cards = card_value.copy()
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
            if self.hand_cards[x] in [1,14,27,40] and self.hand_total <= 10:
                self.hand_total = self.hand_total + 11
            if self.hand_cards[x] in [1,14,27,40] and self.hand_total > 10:
                self.hand_total = self.hand_total + 1
        return self.hand_total

    def output_cards(self):
        print('Cards in hand:')
        for x in range(len(self.hand_cards)):
            card = int(self.hand_cards[x])
            if card in card_value:
                
                cardval = card_value[card]
                print(cardval)
        print('Total: %d' % self.calculate_hand_val())

    def bust(self):
        if self.hand_total <= 21:
            return false
        else:
            return true

    def __lt__(self,other):
        if (self.hand_total < other.hand_total) and not self.bust():
            return true
        else:
            return false

    def __eq__(self,other):
        if self.hand_total == other.hand_total and not self.bust():
            return true
        else:
            return false
        
        
make_bet()		
BJH = BlackjackHand()
BJH.output_cards()
