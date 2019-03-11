#!/usr/local/bin/python3
import random

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)

names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
deck = [ ( name + ' of ' + suit, suits.index(suit), name, names.index(name) ) for suit in suits for name in names ] # CHANGED LINE: I added "name, names.index(name)"  
                                                                                                                    # it helps to compare cards  
random.shuffle(deck) # CHANGED LINE: I added this line because we need to mix our deck cards for the game. 

bonus, scoreA, scoreB = 0, 0, 0
# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:
 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 cardA, cardB = deck.pop(), deck.pop() 
 if cardA[3] == cardB[3]:  # CHANGED LINE: I changed [1] to [3], so the battle compares cards by names.   
  bonus += 1 # CHANGED LINE: I changed this line since we want to postpone the win if the same cards are drawn
  outcome = 'ties'
 elif cardA[3] > cardB[3]:
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
  scoreB += 1 + bonus  # CHANGED LINE: Because in this case we need to add point for scoreB
  bonus = 0 
  outcome = 'is beaten by'

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
 print ( '{:55.55} ${} to ${}, ${} left to win, {} cards left.'.format ( event, scoreA, scoreB, int(len(deck)/2), int(len(deck)) ) )
 #CHANGED LINE: some additional conditions are needed for the output, such as number of cards left 
