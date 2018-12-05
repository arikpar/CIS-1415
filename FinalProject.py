#Gabe Sorenson
#Arik Parenteau

card_value = {
  1: 'Ace of Hearts', 2: 'Two of Hearts', 3, 'Three of Hearts', 4, 'Four of Hearts', 5, 'Five of Hearts', 6, 'Six of Hearts',
  7, 'Seven of Hearts', 8, 'Eight of Hearts', 9, 'Nine of Hearts', 10, 'Ten of Hearts', 11, 'Jack of Hearts', 12, 'Queen of Hearts', 
  13, 'King of Hearts', 14, 'Ace of Diamonds', 15, 'Two of Diamonds', 16, 'Three of Diamonds', 17, 'Four of Diamonds',
  18, 'Five of Diamonds', 19, 'Six of Diamonds', 20, 'Seven of Diamonds', 21, 'Eight of Diamonds', 22, 'Nine of Diamonds',
  23, 'Ten of Diamonds', 24, 'Jack of Diamonds', 25, 'Queen of Diamonds', 26, 'King of Diamonds',
 
}


def calc_score(card_list):
  total = 0
  for card in card_list:
    if total >=11 and card == 'A':
      total += 1
    else:
      total += card_value[card]
  return total
