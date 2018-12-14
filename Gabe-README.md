Blackjack Final Project Report
==============================

HOW THE PROGRAM WORKS:

To start out, a menu pops up on the interface, having the user press 'p' to start. Other options on the menu include 'r' to see previous winnings, 'c' to clear those previous winnings and start fresh, and finally 'q' to quit. it prompts the user to enter how much money/chips they would start out with. Next, the user chooses how much they want to bet on the given hand, ranging in increments of 5 with a minimum bet of 5 chips, max of 100.  The program then outputs what the dealer is showing (1 card), and then what you are showing (2 cards). Based off of what the user has, they will decide, and type out, whether to Hit or Stay ('h' to hit). If they decide to hit, they will keep getting asked to hit until they bust (over 21) or decide to stay. Then, it's the dealer's turn. If the dealer has less than 17, he will hit until he reaches at least 17 or busts, determining who wins the hand. If the user wins he will gain his bet’s worth of money into his total; if the user loses they will lose their bet’s worth of money. This will be output.  At this point the option will be given to leave or play another hand. If the user chooses to leave, the program will output how much money they gained or lost. If they play another hand, the program will display the menu again, to which the user may choose what to do from there.

MEETING THE PROJECT REQUIREMENTS:

1. We used our own python class that has embedded function based of off the hand values, drawing a card, the dealer's cards, how hitting works, how you bust, and more.
2. We definitely went over the minimum of 3 functions for the project. The total amount of functions added up to be 15.
3. We used a dictionary for assigning all 52 cards in a deck to a value. We used lists to make sure the hand total calculations were correct given the values in the deck.
4. The only modules we used were "random" and "time", and I don't think we used "time" in class. So we only used one module from class.
5. We used a file to read and store winnings/losings from every hand played.
6. Exceptions using just the one deck includes the fact that the dealer stands on a soft 17.
7. One concept that we used that we did not learn in class was the usage of the time.sleep() method under the time module. This enabled the interface of the program to have a better feel and flow to it, and have it act more natural and realistic.

GROUP MEMBERS:

-Gabe Sorenson(me), Arik Parenteau

REFLECTION:

For this project, I really recreated our own version of a card game I enjoy playing, that is fairly simple for the average person to understand and play. Implimented the rules of the game into a program was confusing at times, but interesting to say the least.
Additionally, figuring out the flow and design of the text interface was fun to do as well. The discovery of the time.sleep() method in the time module was incredibily useful in that regard. It was also fun testing out the project itself.
As far as dislikes go, there weren't really any at all, other than the fact that the debugging took up a lot of time it seemed like.
It was frusturating at times, but that's programming for you! Overall, completing this project and having it run smoothly and successfully was a big accomplishment for me.


 

