# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
prompt = 'New game. Hit or stand?'

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + 
                          CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        string = 'Hand contains '
        for card in self.cards:
            string += str(card) + ' '
        return string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace = False
        value = 0
        for card in self.cards:
            if card.rank == 'A':
                ace = True
            value += VALUES[card.get_rank()]
        if value <= 11 and ace:
            value += 10
        return value
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 10

        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = [Card(suit, rank) for suit in SUITS for rank in RANKS]
                

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_list)

    def deal_card(self):
        return self.card_list.pop()
    
    def __str__(self):
        string = 'Deck contains '
        for card in self.card_list:
            string += str(card) + ' '
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, card_deck, score, prompt

    # your code goes here
    if in_play:
        score -= 1
        outcome = 'You lost the last game.'
    else:
        outcome = ''
    card_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    card_deck.shuffle()
    player_hand.add_card(card_deck.deal_card())
    dealer_hand.add_card(card_deck.deal_card())
    player_hand.add_card(card_deck.deal_card())
    dealer_hand.add_card(card_deck.deal_card())
    in_play = True
    prompt = 'New game. Hit or stand?'

def hit():
    global outcome, in_play, score, prompt
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(card_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = 'You have busted.'
            prompt = 'Deal a new game?'
            score -= 1
            in_play = False
        else:
            outcome = ''
            prompt = 'Hit or stand?'

def stand():
    global in_play, score, outcome, prompt
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(card_deck.deal_card())
    # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            score += 1
            outcome = 'Dealer busted! You win.'
        elif player_hand.get_value() > dealer_hand.get_value():
            score += 1
            outcome = 'You win.'
        else:
            outcome = 'Dealer wins.'
            score -= 1
    in_play = False
    prompt = 'Deal a new game?'

# draw handler    
def draw(canvas):
    canvas.draw_text('Blackjack', [100, 100], 40, 'Blue')
    canvas.draw_text('Score: ' + str(score), [350, 100], 30, "Black")
    canvas.draw_text('Dealer', [80, 170], 30, 'Black')
    canvas.draw_text('Player', [80, 370], 30, 'Black')
    canvas.draw_text(outcome, [230, 180], 30, 'Black')
    canvas.draw_text(prompt, [230, 380], 30, 'Black')
    # Draw cards from each hand
    dealer_hand.draw(canvas, [80, 200])
    player_hand.draw(canvas, [80, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [80 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric