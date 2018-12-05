#Gabe Sorenson
#Arik Parenteau

card_value = {
  1: 'Ace of Hearts', 2: 'Two of Hearts', 3: 'Three of Hearts', 4: 'Four of Hearts', 5: 'Five of Hearts', 6: 'Six of Hearts',
  7: 'Seven of Hearts', 8: 'Eight of Hearts', 9: 'Nine of Hearts', 10: 'Ten of Hearts', 11: 'Jack of Hearts', 12: 'Queen of Hearts', 
  13: 'King of Hearts', 14: 'Ace of Diamonds', 15: 'Two of Diamonds', 16: 'Three of Diamonds', 17: 'Four of Diamonds',
  18: 'Five of Diamonds', 19: 'Six of Diamonds', 20: 'Seven of Diamonds', 21: 'Eight of Diamonds', 22: 'Nine of Diamonds',
  23: 'Ten of Diamonds', 24: 'Jack of Diamonds', 25: 'Queen of Diamonds', 26: 'King of Diamonds', 27: 'Ace of Clubs',
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
   print('What amount of chips would you like bet?')
  
   while bet == 0:
      bet_comp = input()
      bet_comp = int(bet_comp)
      
      if bet_comp >= 1 and bet_comp <= chip_total:
         bet = bet_comp
      else:
         print("You only have " + str(chip_total) + " remaining")
